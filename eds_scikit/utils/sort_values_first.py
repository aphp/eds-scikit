from typing import List

from eds_scikit.utils.typing import DataFrame


def sort_values_first(
    df: DataFrame, by_cols: List[str], cols: List[str], ascending: bool = False
):
    """
    Replace dataframe.sort_value(cols).groupby(by_cols).first()

    Parameters
    ----------
    df : DataFrame
    by_cols : List[str]
        columns to groupby
    cols : List[str]
        columns to sort
    ascending : bool
    """

    return (
        df.groupby(by_cols)
        .apply(
            lambda group: group.sort_values(
                by=cols, ascending=[ascending for i in cols]
            ).head(1)
        )
        .reset_index(drop=True)
    )
