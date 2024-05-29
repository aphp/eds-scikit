from typing import List
import numpy as np
from eds_scikit.utils.typing import DataFrame


def sort_values_first_koalas(
    dataframe: DataFrame,
    by_cols: List[str],
    cols: List[str],
    disambiguate_col: str,
    ascending: bool = True,
) -> DataFrame:
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
    
    if "O" in _dtypes.values:
        object_col = _dtypes[_dtypes == "O"].index.tolist()
        raise TypeError(f"Found unsupported object type in data types : {object_col}")
    else:
        _dtypes = _dtypes.to_dict()
    
    dataframe[by_cols] = dataframe[by_cols].fillna("NA")
    for col in cols:
        dataframe_min_max = dataframe.groupby(by_cols, as_index=False)[col]
        dataframe_min_max = (
            dataframe_min_max.min() if ascending else dataframe_min_max.max()
        )
        dataframe[col] = dataframe[col].fillna("NA")
        dataframe_min_max = dataframe_min_max.fillna("NA")
        dataframe = dataframe.merge(dataframe_min_max, on=[*by_cols, col], how="right")
        
    dataframe = dataframe.replace("NA", np.nan)
    dataframe = dataframe.astype(_dtypes)

    return dataframe