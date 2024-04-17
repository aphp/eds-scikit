from typing import List

from eds_scikit.utils.typing import DataFrame


def sort_values_first_koalas(
    dataframe: DataFrame,
    by_cols: List[str],
    cols: List[str],
    ascending: bool = True,
) -> DataFrame:
    """Use this function to obtain in koalas the same ouput as dataframe.sort_values([*cols, disambiguate_col]).groupby(by_cols).first() in pandas.
    disambiguate_col must be provided to make sure the output is deterministic
    Parameters
    ----------
    dataframe : DataFrame
    by_cols : List[str]
    cols : List[str]
    ascending : bool, optional
    Returns
    -------
    DataFrame
    """

    return dataframe.sort_values(cols, ascending=ascending).drop_duplicates(by_cols)
