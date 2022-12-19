from typing import Any, Callable

import numpy as np
import pandas as pd
import pandas.core.algorithms as algos
from pandas import IntervalIndex, to_datetime, to_timedelta
from pandas._libs import Timedelta, Timestamp
from pandas._libs.lib import infer_dtype
from pandas.core.dtypes.common import (
    DT64NS_DTYPE,
    is_categorical_dtype,
    is_datetime64_dtype,
    is_datetime64tz_dtype,
    is_list_like,
    is_scalar,
    is_timedelta64_dtype,
)


def cut(
    x,
    bins,
    right: bool = True,
    labels=None,
    retbins: bool = False,
    precision: int = 3,
    include_lowest: bool = False,
    duplicates: str = "raise",
    ordered: bool = True,
):
    if x.ndim != 1:
        raise ValueError("x must be 1D")

    x, dtype = x.astype(np.int64), x.dtype

    if not np.iterable(bins):
        if is_scalar(bins) and bins < 1:
            raise ValueError("`bins` should be a positive integer.")

        try:  # for array-like
            sz = x.size
        except AttributeError:
            x = np.asarray(x)
            sz = x.size

        if sz == 0:
            raise ValueError("Cannot cut empty array")

        mn, mx = x.min(), x.max()

        if np.isinf(mn) or np.isinf(mx):
            raise ValueError(
                "cannot specify integer `bins` when input data contains infinity"
            )
        elif mn == mx:  # adjust end points before binning
            mn -= 0.001 * abs(mn) if mn != 0 else 0.001
            mx += 0.001 * abs(mx) if mx != 0 else 0.001
            bins = np.linspace(mn, mx, bins + 1, endpoint=True)
        else:  # adjust end points after binning
            bins = np.linspace(mn, mx, bins + 1, endpoint=True)
            adj = (mx - mn) * 0.001  # 0.1% of the range
            if right:
                bins[0] -= adj
            else:
                bins[-1] += adj

    elif isinstance(bins, IntervalIndex):
        if bins.is_overlapping:
            raise ValueError("Overlapping IntervalIndex is not accepted.")

    else:
        if is_datetime64tz_dtype(bins):
            bins = np.asarray(bins, dtype=DT64NS_DTYPE)
        else:
            bins = np.asarray(bins)
        bins = _convert_bin_to_numeric_type(bins, dtype)

        # GH 26045: cast to float64 to avoid an overflow
        if (np.diff(bins.astype("float64")) < 0).any():
            raise ValueError("bins must increase monotonically.")

    fac, bins = _bins_to_cuts(
        x,
        bins,
        right=right,
        labels=labels,
        precision=precision,
        include_lowest=include_lowest,
        dtype=dtype,
        duplicates=duplicates,
        ordered=ordered,
    )

    if not retbins:
        return fac

    return fac, bins


def _convert_bin_to_numeric_type(bins, dtype):
    """
    if the passed bin is of datetime/timedelta type,
    this method converts it to integer
    Parameters
    ----------
    bins : list-like of bins
    dtype : dtype of data
    Raises
    ------
    ValueError if bins are not of a compat dtype to dtype
    """
    bins_dtype = infer_dtype(bins, skipna=False)
    if is_timedelta64_dtype(dtype):
        if bins_dtype in ["timedelta", "timedelta64"]:
            bins = to_timedelta(bins).view(np.int64)
        else:
            raise ValueError("bins must be of timedelta64 dtype")
    elif is_datetime64_dtype(dtype) or is_datetime64tz_dtype(dtype):
        if bins_dtype in ["datetime", "datetime64"]:
            bins = to_datetime(bins).view(np.int64)
        else:
            raise ValueError("bins must be of datetime64 dtype")

    return bins


def _format_labels(
    bins, precision: int, right: bool = True, include_lowest: bool = False, dtype=None
):
    """based on the dtype, return our labels"""
    closed = "right" if right else "left"

    formatter: Callable[[Any], Timestamp] | Callable[[Any], Timedelta]

    if is_datetime64tz_dtype(dtype):
        formatter = lambda x: Timestamp(x, tz=dtype.tz)
        adjust = lambda x: x - Timedelta("1ns")
    elif is_datetime64_dtype(dtype):
        formatter = Timestamp
        adjust = lambda x: x - Timedelta("1ns")
    elif is_timedelta64_dtype(dtype):
        formatter = Timedelta
        adjust = lambda x: x - Timedelta("1ns")
    else:
        precision = _infer_precision(precision, bins)
        formatter = lambda x: _round_frac(x, precision)
        adjust = lambda x: x - 10 ** (-precision)

    breaks = [formatter(b) for b in bins]
    if right and include_lowest:
        # adjust lhs of first interval by precision to account for being right closed
        breaks[0] = adjust(breaks[0])

    return IntervalIndex.from_breaks(breaks, closed=closed)


def _searchsorted(x, bins, right):
    """
    koalas version of np.searchsorted
    """
    bins = sorted(bins)
    d = dict(zip(bins, range(len(bins))))

    x = x.to_frame()
    col = x.columns[0]
    x["idx_bins"] = len(bins)

    for _bin in bins[::-1]:
        mask = x[col] <= _bin.item() if right else x[col] < _bin.item()
        x.loc[mask, "idx_bins"] = d[_bin]

    ids = x.pop("idx_bins")
    x = x[col]

    return ids


def _bins_to_cuts(
    x,
    bins: np.ndarray,
    right: bool = True,
    labels=None,
    precision: int = 3,
    include_lowest: bool = False,
    dtype=None,
    duplicates: str = "raise",
    ordered: bool = True,
):
    """
    koalas version of pandas.core.reshape.tile._bins_to_cuts
    """
    bins = np.unique(bins)
    ids = _searchsorted(x, bins, right)
    na_mask = x.isna() | (ids == len(bins)) | (ids == 0)

    # hack to bypass "TypeError: 'Series' object does not support item assignment"
    ids = ids.to_frame()
    ids.loc[na_mask] = 0
    ids = ids[ids.columns[0]]

    if labels:
        if not (labels is None or is_list_like(labels)):
            raise ValueError(
                "Bin labels must either be False, None or passed in as a "
                "list-like argument"
            )
        elif labels is None:
            labels = _format_labels(
                bins, precision, right=right, include_lowest=include_lowest, dtype=dtype
            )
        elif ordered and len(set(labels)) != len(labels):
            raise ValueError(
                "labels must be unique if ordered=True; pass ordered=False "
                "for duplicate labels"
            )
        else:
            if len(labels) != len(bins) - 1:
                raise ValueError(
                    "Bin labels must be one fewer than the number of bin edges"
                )
        if not is_categorical_dtype(labels):
            labels = pd.Categorical(
                labels,
                categories=labels if len(set(labels)) == len(labels) else None,
                ordered=ordered,
            )

        label_mapping = dict(zip(range(len(labels)), labels))
        # x values outside of bins edges (i.e. when ids = 0) are mapped to NaN
        result = (ids - 1).map(label_mapping)
        result.fillna(np.nan, inplace=True)

    else:
        result = ids - 1
        # hack to bypass "TypeError: 'Series' object does not support item assignment"
        result = result.to_frame()
        result.loc[na_mask] = np.nan
        result = result[result.columns[0]]

    return result, bins


def _infer_precision(base_precision: int, bins) -> int:
    """
    Infer an appropriate precision for _round_frac
    """
    for precision in range(base_precision, 20):
        levels = [_round_frac(b, precision) for b in bins]
        if algos.unique(levels).size == bins.size:
            return precision
    return base_precision  # default


def _round_frac(x, precision: int):
    """
    Round the fractional part of the given number
    """
    if not np.isfinite(x) or x == 0:
        return x
    else:
        frac, whole = np.modf(x)
        if whole == 0:
            digits = -int(np.floor(np.log10(abs(frac)))) - 1 + precision
        else:
            digits = precision
        return np.around(x, digits)
