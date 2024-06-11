import numpy as np


def sort_values_first_koalas(
    dataframe,
    by_cols,
    cols,
    disambiguate_col,
    ascending,
):
    """Use this function to obtain in koalas the same ouput as dataframe.sort_values([*cols, disambiguate_col]).groupby(by_cols).first() in pandas.
    disambiguate_col must be provided to make sure the output is deterministic
    Parameters
    ----------
    dataframe : DataFrame
    by_cols : List[str]
    cols : List[str]
    disambiguate_col : List[str]
    ascending : bool, optional
    Returns
    -------
    DataFrame
    """
    cols = [*cols, disambiguate_col]
    dataframe = dataframe[[*by_cols, *cols]]

    _dtypes = dataframe.dtypes
    _dtypes = _dtypes[_dtypes.values != "O"].to_dict()

    dataframe = dataframe.fillna("NaT").replace("NaT", np.nan)

    for col in cols:
        dataframe_min_max = dataframe.groupby(by_cols, as_index=False)[col]
        dataframe_min_max = (
            dataframe_min_max.min() if ascending else dataframe_min_max.max()
        )
        dataframe = dataframe.merge(dataframe_min_max, on=[*by_cols, col], how="right")

    dataframe = dataframe.astype(_dtypes)

    return dataframe
