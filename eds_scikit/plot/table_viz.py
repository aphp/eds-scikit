from functools import reduce
from typing import List

import altair as alt
import pandas as pd
from loguru import logger

from eds_scikit.plot.altair_utils import generate_color_map
from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.framework import get_framework, to

from ..utils.typing import DataFrame


def map_column(
    table: DataFrame,
    mapping: dict,
    src_column: str,
    target_column: str,
    drop: bool = True,
) -> DataFrame:
    """Map a dataframe column given a mapping dictionnary (of regex).
    If ```src_column == target_column```, src_column will be renamed.

    Parameter"
    ----------
    table : DataFrame
    mapping : dict
        **EXAMPLE**: `{"column name" : {"CR" : r"^CR", "CRH" : r"^CRH"}}`
    src_column : str
    target_column : str

    Returns
    -------
    DataFrame
        Dataframe with mapped column
    """
    check_columns(
        table,
        required_columns=[src_column],
    )

    remove_columns = []

    if src_column == target_column:
        table[src_column + "_src"] = table[src_column]
        src_column = src_column + "_src"
        remove_columns += [src_column]
    table[target_column] = "Other"
    table.loc[table[src_column].isna(), target_column] = "NaN"
    for target, regex in mapping.items():
        table.loc[
            table[src_column].str.contains(regex, case=False, regex=True, na=False),
            target_column,
        ] = target

    if drop:
        table = table[set(table.columns).difference(remove_columns)]

    return table


def preprocess_table(
    table: DataFrame,
    category_columns: List[str],
    date_column: str,
    start_date: str,
    end_date: str,
    mapper: dict = None,
) -> DataFrame:
    """

    Parameters
    ----------
    table : DataFrame
        Input dataframe to be reduced.
    category_columns : List[str]
        Columns to perform reduction on.
    date_column : str
        Date column.
    start_date : str
        start date
    end_date : str
        end date
    mapper : dict
        **EXAMPLE**: `{"column 1" : {"CR" : r"^CR", "CRH" : r"^CRH"}, "column 2" : {"code a" : r"^A", "code b" : r"^B"}}`

    Returns
    -------
    DataFrame
        Formated and preprocessed table

    Raises
    ------
    ValueError
    """

    # Check and format to string category columns

    remove_colums = []

    for col in category_columns:
        if not (col in table.columns):
            logger.info(f"Column {col} not in table.")
            remove_colums += [col]
        else:
            table[col] = table[col].astype(str)

    for col in remove_colums:
        category_columns.remove(col)

    if category_columns == []:
        raise Exception("No columns from category_columns in input table.")

    category_columns = [*category_columns, date_column]

    table = table[category_columns]

    # Filter table on dates

    framework = get_framework(table)

    table = table[(table[date_column] >= start_date) & (table[date_column] <= end_date)]
    table["datetime"] = framework.to_datetime(table[date_column].dt.strftime("%Y-%m"))
    table = table.drop(columns=[date_column])

    # Map category columns

    if mapper:
        for col, mapping in mapper.items():
            if col in category_columns:
                table = map_column(table, mapping, col, col)

    return table


def reduce_table(
    table: DataFrame,
    start_date: str,
    end_date: str,
    category_columns: List[str],
    date_column: str,
    mapper: dict = None,
) -> DataFrame:
    """
    Reduce input table by counting each cartesian product values (col1, col2, ..., date_col) for each columns in category_columns and each date.
    Columns values must be under 50 . Use mapper to reduce this size.

    Parameters
    ----------
    table : DataFrame
        Input dataframe to be reduced.
    start_date : str
        start date
    end_date : str
        end date
    category_columns : List[str]
        Columns to perform reduction on.
    date_column : str
        Date column.
    mapper : dict
        **EXAMPLE**: `{"column 1" : {"CR" : r"^CR", "CRH" : r"^CRH"}, "column 2" : {"code a" : r"^A", "code b" : r"^B"}}`

    Returns
    -------
    DataFrame
        Reducted DataFrame with columns category_columns, date_column and count.

    Raises
    ------
    ValueError
    """

    check_columns(
        table,
        required_columns=[date_column],
    )
    table = preprocess_table(
        table, category_columns, date_column, start_date, end_date, mapper
    )
    # to prevent computation issues
    shape = table.shape  # noqa

    # raise error it too much categorical values
    nunique = table.nunique()
    oversized_columns = nunique[(nunique.index != "datetime") & (nunique > 50)].index
    if len(oversized_columns) > 0:
        raise ValueError(
            f"Input table columns can't have more then 50 values. Consider using eds_scikit.plot.map_column. Oversized columns: {oversized_columns}",
        )
    # compute reducted table
    table_count = (
        table.fillna("NaN")
        .groupby(["datetime", *category_columns])
        .size()
        .reset_index(name="count")
    )

    # to prevent computation issues
    shape = table_count.shape  # noqa

    # final formatting
    table_count = to("pandas", table_count)
    table_count["datetime"] = pd.to_datetime(table_count["datetime"])
    date_dataframe = pd.DataFrame(
        pd.date_range(start=start_date, end=end_date, freq="MS"), columns=["datetime"]
    )
    table_count = table_count.merge(date_dataframe, on="datetime", how="right")

    table_count["count"] = table_count["count"].fillna(0)
    table_count = table_count.fillna("NaN")

    return table_count


def visualize_table(
    table_count: DataFrame,
    title: str = "table exploration dashboard",
    description=True,
) -> alt.Chart:

    """Generate reduced table dashboard.

    Parameters
    ----------
    table_count : DataFrame
        Output from eds_scikit.plot.table_viz.reduce_table
    title : str
        Chart title

    Returns
    -------
    alt.Chart
        reduce_table dashboard

    Raises
    ------
    ValueError
        _description_
    """

    check_columns = ["count", "datetime"]
    for check_column in check_columns:
        if not (check_column in table_count.columns):
            raise ValueError(f"Input table must have a {check_column} column.")

    selections = {}
    columns = [col for col in table_count.columns if not (col in ["datetime", "count"])]
    for col in columns:
        selections[col] = alt.selection_point(
            fields=[col], on="click", bind="legend", clear="dblclick"
        )

    charts = []

    width, height = 300, 50

    # Two charts per column
    for i, col in enumerate(columns):
        color_scale = generate_color_map(table_count, col)
        selection_col = [selections[s] for s in selections if (s != col)]
        # Global volumetry chart
        chart = (
            alt.Chart(table_count)
            .mark_bar()
            .encode(
                x=col + ":N",
                y="sum(count):Q",
                color=alt.Color(col + ":N", scale=color_scale),
                opacity=alt.condition(selections[col], alt.value(1), alt.value(0.3)),
                tooltip=[col],
            )
            .add_params(selections[col])
        )

        if len(selection_col) > 0:
            chart = chart.add_params(selections[col]).transform_filter(
                reduce(
                    (lambda x, y: x & y),
                    selection_col,
                )
            )

        # Temporal volumetry chart
        base_t = (
            alt.Chart(table_count)
            .mark_line()
            .encode(
                x=alt.X("yearmonth(datetime):T"),
                y=alt.Y("sum(count):Q", axis=alt.Axis(format="s")),
                color=alt.Color(col + ":N", scale=color_scale),
                opacity=alt.condition(selections[col], alt.value(1), alt.value(0.3)),
            )
            .add_params(selections[col])
        )
        if len(selection_col) > 0:
            base_t = base_t.transform_filter(
                reduce(
                    (lambda x, y: x & y),
                    selection_col,
                )
            )
        base_t = base_t.properties(width=width, height=height)
        chart = chart.properties(width=width, height=height)

        chart = (chart | base_t).properties(title=col)

        charts.append(chart)

    charts = alt.vconcat(*charts).resolve_scale(color="independent")

    if description:
        title = {
            "text": [title],
            "subtitle": [
                "ALT + SHIFT to select multiple categories",
                "Double-click on legend to unselect",
                "Reduce table column and values size for better interactivity",
            ],
            "fontSize": 25,
            "subtitleFontSize": 15,
            "offset": 30,
            "subtitlePadding": 20,
        }

        charts = charts.properties(
            padding={"left": 50, "top": 50, "right": 50, "bottom": 50},
            title=title,
        ).configure_legend(columns=4, symbolLimit=0)

    return charts
