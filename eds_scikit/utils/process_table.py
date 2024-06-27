from datetime import timedelta
from typing import Dict, List, Union

import numpy as np
from loguru import logger

from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.typing import DataFrame


def tag_table_by_type(
    table: DataFrame,
    type_groups: Union[str, Dict],
    source_col: str,
    target_col: str,
    filter_table: bool = False,
):
    """Add tag column to table based on their value (ex : condition_occurrence -> "DIABETIC", "NOT DIABETIC)

    Parameters
    ----------
    table : DataFrame
        Table (must contain columns source_col, target_col)
    type_groups : Union[str, Dict]
        Regex or Dict of regex to define tags and associated regex.
    source_col : str
        Column on which the tagging is applied.
    target_col : str
        Label column name
    remove_other : bool
        If True, remove untagged columns

    Returns
    -------
    DataFrame
        Input dataframe with tag column `target_col`

    Output
    -------
    | person_id                   |   condition_source_value | DIABETIC_CONDITION    |
    |:---------------------------:|-------------------------:|:---------------------:|
    | 001                         |                     E100 | DIABETES_TYPE_I       |
    | 002                         |                     E101 | DIABETES_TYPE_I       |
    | 003                         |                     E110 | DIABETES_TYPE_II      |
    | 004                         |                     E113 | DIABETES_TYPE_II      |
    | 005                         |                     A001 | OTHER                 |


    """
    if isinstance(type_groups, str):
        type_groups = {type_groups: type_groups}
    table[target_col] = "OTHER"

    for type_name, type_value in type_groups.items():

        table.loc[
            table[source_col]
            .astype(str)
            .str.contains(
                type_value,
                case=False,
                regex=True,
                na=False,
            ),
            target_col,
        ] = type_name

    logger.debug(
        "The following {} : {} have been tagged on table.",
        target_col,
        type_groups,
    )

    table = table[table[target_col] != "OTHER"] if filter_table else table

    return table


def tag_table_period_length(
    table: DataFrame,
    length_of_stays: List[float],
    start_date_col: str = "visit_start_datetime",
    end_date_col: str = "visit_end_datetime",
) -> DataFrame:
    """Tag table by length of stays (can be applied to visit_occurrence table)

    Example : length_of_stays = [7, 14]

    Output
    -------
    | person_id                   |   visit_start_datetime   | visit_end_datetime    | length_of_stay        |
    |:---------------------------:|-------------------------:|:---------------------:|:---------------------:|
    | 001                         |               2020-04-01 | 2020-04-12            | "7 days - 14 days"    |
    | 002                         |               2020-04-01 | 2020-04-03            | "<= 7 days "          |
    | 003                         |               2020-04-01 | 2020-04-09            | ">= 7 days "          |


    Parameters
    ----------
    table : DataFrame
    length_of_stays : List[float]
        Example : [7 , 14]
    start_date_col : str, optional
        by default "visit_start_datetime"
    end_date_col : str, optional
        by default "visit_end_datetime"

    Returns
    -------
    DataFrame
    """
    table = table.assign(
        length=(table[end_date_col] - table[start_date_col])
        / np.timedelta64(timedelta(days=1))
    )

    # Incomplete stays
    table = table.assign(length_of_stay="Not specified")
    table["length_of_stay"] = table.length_of_stay.mask(
        table[end_date_col].isna(),
        "Incomplete stay",
    )

    # Complete stays
    min_duration = length_of_stays[0]
    max_duration = length_of_stays[-1]
    table["length_of_stay"] = table["length_of_stay"].mask(
        (table["length"] <= min_duration),
        "<= {} days".format(min_duration),
    )
    table["length_of_stay"] = table["length_of_stay"].mask(
        (table["length"] >= max_duration),
        ">= {} days".format(max_duration),
    )
    for min_length, max_length in zip(length_of_stays[:-1], length_of_stays[1:]):
        table["length_of_stay"] = table["length_of_stay"].mask(
            (table["length"] >= min_length) & (table["length"] < max_length),
            "{} days - {} days".format(min_length, max_length),
        )
    table = table.drop(columns="length")

    return table


def tag_table_with_age(
    table: DataFrame, date_col: str, person: DataFrame, age_ranges: List[int] = None
):
    """Tag table with person age

    Parameters
    ----------
    table : DataFrame
        must contain person_id and date_col
    date_column: str
        date column from table on which to compute age
    person : DataFrame
        must contain person_id
    age_ranges : List[int]
        if None, simply compute age.
        example : None, [18], [18, 60]

    Returns
    -------
    DataFrame
    """
    check_columns(df=person, required_columns=["person_id", "birth_datetime"])
    check_columns(df=table, required_columns=[date_col, "person_id"])

    table = table.merge(person[["person_id", "birth_datetime"]], on="person_id")

    table["age"] = (table[date_col] - table["birth_datetime"]) / (
        np.timedelta64(timedelta(days=1)) * 356
    )
    table["age"] = table["age"].astype(int)

    table["age_range"] = "Not specified"
    if age_ranges:
        age_ranges.sort()
        table.loc[table.age <= age_ranges[0], "age_range"] = f"age <= {age_ranges[0]}"

        for age_min, age_max in zip(age_ranges[:-1], age_ranges[1:]):
            in_range = (table.age > age_min) & (table.age <= age_max)
            table.loc[in_range, "age_range"] = f"{age_min} < age <= {age_max}"

        table.loc[table.age > age_ranges[-1], "age_range"] = f"age > {age_ranges[-1]}"

    return table
