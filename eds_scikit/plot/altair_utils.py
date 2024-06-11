from typing import List

import altair as alt

from eds_scikit.utils.checks import check_columns

from ..utils.typing import DataFrame


def generate_cyclic_colors(N: int) -> List[str]:
    """Given an interger of N values, return a cyclic list
    of size N with repeated 20 altair standards colors.

    Parameters
    ----------
    N : int

    Returns
    -------
    List[str]

    """
    category20_colors = [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
        "#aec7e8",
        "#ffbb78",
        "#98df8a",
        "#ff9896",
        "#c5b0d5",
        "#c49c94",
        "#f7b6d2",
        "#c7c7c7",
        "#dbdb8d",
        "#9edae5",
    ]
    num_colors = len(category20_colors)
    return [category20_colors[i % num_colors] for i in range(N)]


def generate_color_map(df: DataFrame, col: str) -> alt.Scale:
    """Given a dataframe and a column name,
    generate an altair color scale for visualization purpose.

    Parameters
    ----------
    df : DataFrame
    col : str

    Returns
    -------
    alt.Scale
    """

    check_columns(
        df,
        required_columns=[col],
    )

    category_values = df[col].fillna("NaN").unique().tolist()
    if "NaN" in category_values:
        category_colors = generate_cyclic_colors(len(category_values) - 1)
        category_values = [
            category_value
            for category_value in category_values
            if category_value != "NaN"
        ]
        domain = [*category_values, "NaN"]
        range = [*category_colors, "black"]
    else:
        category_colors = generate_cyclic_colors(len(category_values))
        domain = category_values
        range = category_colors

    color_scale = alt.Scale(domain=domain, range=range)
    return color_scale
