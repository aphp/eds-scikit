from datetime import timedelta

import numpy as np

from .framework import is_koalas, is_pandas
from .typing import Series


def add_timedelta(series: Series, **kwargs) -> Series:
    """
    Adds a unique timedelta to a Pandas or Koalas Series
    """
    return series.map(lambda d: d + timedelta(**kwargs))


def substract_datetime(
    series_1: Series,
    series_2: Series,
    out: str = "seconds",
) -> Series:
    """
    Substract 2 datetime series and return the number of seconds or hours
    between them.
    """

    if out not in ["seconds", "hours"]:
        raise ValueError("the 'out' parameter should be in ['hours','seconds']")
    if not (
        np.issubdtype(series_1.dtype, np.datetime64)
        and np.issubdtype(series_2.dtype, np.datetime64)
    ):
        raise TypeError("One of the provided Serie isn't a datetime Serie")

    if is_pandas(series_1) and is_pandas(series_2):
        diff = (series_1 - series_2).dt.total_seconds()

    elif is_koalas(series_1) and is_koalas(series_2):
        diff = series_1 - series_2

    else:
        raise TypeError("Both series should either be a Koalas or Pandas Serie")

    if out == "hours":
        return diff / 3600
    return diff
