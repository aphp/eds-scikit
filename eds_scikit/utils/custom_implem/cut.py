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
):  # pragma: no cover
    """
    Bin values into discrete intervals.

    Use `cut` when you need to segment and sort data values into bins. This
    function is also useful for going from a continuous variable to a
    categorical variable. For example, `cut` could convert ages to groups of
    age ranges. Supports binning into an equal number of bins, or a
    pre-specified array of bins.

    See original function at: https://github.com/pandas-dev/pandas/blob/v1.5.2/pandas/core/reshape/tile.py#L50-L305 # noqa

    Parameters
    ----------
    x : koalas Series.
        The input array to be binned. Must be 1-dimensional.
    bins : int, sequence of scalars, or IntervalIndex
        The criteria to bin by.
        * int : Defines the number of equal-width bins in the range of `x`. The
          range of `x` is extended by .1% on each side to include the minimum
          and maximum values of `x`.
        * sequence of scalars : Defines the bin edges allowing for non-uniform
          width. No extension of the range of `x` is done.
        * IntervalIndex : Defines the exact bins to be used. Note that
          IntervalIndex for `bins` must be non-overlapping.
    right : bool, default True
        Indicates whether `bins` includes the rightmost edge or not. If
        ``right == True`` (the default), then the `bins` ``[1, 2, 3, 4]``
        indicate (1,2], (2,3], (3,4]. This argument is ignored when
        `bins` is an IntervalIndex.
    labels : array or False, default None
        Specifies the labels for the returned bins. Must be the same length as
        the resulting bins. If False, returns only integer indicators of the
        bins. This affects the type of the output container (see below).
        This argument is ignored when `bins` is an IntervalIndex. If True,
        raises an error. When `ordered=False`, labels must be provided.
    retbins : bool, default False
        Whether to return the bins or not. Useful when bins is provided
        as a scalar.
    precision : int, default 3
        The precision at which to store and display the bins labels.
    include_lowest : bool, default False
        Whether the first interval should be left-inclusive or not.
    duplicates : {default 'raise', 'drop'}, optional
        If bin edges are not unique, raise ValueError or drop non-uniques.
    ordered : bool, default True
        Whether the labels are ordered or not. Applies to returned types
        Categorical and Series (with Categorical dtype). If True,
        the resulting categorical will be ordered. If False, the resulting
        categorical will be unordered (labels must be provided).
        .. versionadded:: 1.1.0
    Returns
    -------
    out : Categorical, Series, or ndarray
        An array-like object representing the respective bin for each value
        of `x`. The type depends on the value of `labels`.
        * None (default) : returns a Series for Series `x` or a
          Categorical for all other inputs. The values stored within
          are Interval dtype.
        * sequence of scalars : returns a Series for Series `x` or a
          Categorical for all other inputs. The values stored within
          are whatever the type in the sequence is.
        * False : returns an ndarray of integers.
    bins : numpy.ndarray or IntervalIndex.
        The computed or specified bins. Only returned when `retbins=True`.
        For scalar or sequence `bins`, this is an ndarray with the computed
        bins. If set `duplicates=drop`, `bins` will drop non-unique bin. For
        an IntervalIndex `bins`, this is equal to `bins`.

    See Also
    --------
    qcut : Discretize variable into equal-sized buckets based on rank
        or based on sample quantiles.
    Categorical : Array type for storing data that come from a
        fixed set of values.
    Series : One-dimensional array with axis labels (including time series).
    IntervalIndex : Immutable Index implementing an ordered, sliceable set.

    Notes
    -----
    Any NA values will be NA in the result. Out of bounds values will be NA in
    the resulting Series or Categorical object.
    Reference :ref:`the user guide <reshaping.tile.cut>` for more examples.

    Examples
    --------
    Discretize into three equal-sized bins.

    >>> from eds_scikit.utils.framework import bd
    >>> bd.cut(ks.Series(np.array([1, 7, 5, 4, 6, 3])), 3)
    ... # doctest: +ELLIPSIS
    [(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
    Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...

    >>> bd.cut(ks.Series(np.array([1, 7, 5, 4, 6, 3])), 3, retbins=True)
    ... # doctest: +ELLIPSIS
    ([(0.994, 3.0], (5.0, 7.0], (3.0, 5.0], (3.0, 5.0], (5.0, 7.0], ...
    Categories (3, interval[float64, right]): [(0.994, 3.0] < (3.0, 5.0] ...
    array([0.994, 3.   , 5.   , 7.   ]))

    Discovers the same bins, but assign them specific labels. Notice that
    the returned Categorical's categories are `labels` and is ordered.

    >>> bd.cut(ks.Series(np.array([1, 7, 5, 4, 6, 3])),
    ...        3, labels=["bad", "medium", "good"])
    ['bad', 'good', 'medium', 'medium', 'good', 'bad']
    Categories (3, object): ['bad' < 'medium' < 'good']

    ``ordered=False`` will result in unordered categories when labels are passed.
    This parameter can be used to allow non-unique labels:

    >>> bd.cut(ks.Series(np.array([1, 7, 5, 4, 6, 3])), 3,
    ...        labels=["B", "A", "B"], ordered=False)
    ['B', 'B', 'A', 'A', 'B', 'B']
    Categories (2, object): ['A', 'B']

    ``labels=False`` implies you just want the bins back.

    >>> bd.cut(ks.Series([0, 1, 1, 2]), bins=4, labels=False)
    array([0, 1, 1, 3])

    Passing a Series as an input returns a Series with categorical dtype:

    >>> s = ks.Series(np.array([2, 4, 6, 8, 10]),
    ...               index=['a', 'b', 'c', 'd', 'e'])

    >>> bd.cut(s, 3)
    ... # doctest: +ELLIPSIS
    a    (1.992, 4.667]
    b    (1.992, 4.667]
    c    (4.667, 7.333]
    d     (7.333, 10.0]
    e     (7.333, 10.0]
    dtype: category
    Categories (3, interval[float64, right]): [(1.992, 4.667] < (4.667, ...

    Passing a Series as an input returns a Series with mapping value.
    It is used to map numerically to intervals based on bins.

    >>> s = ks.Series(np.array([2, 4, 6, 8, 10]),
    ...               index=['a', 'b', 'c', 'd', 'e'])

    >>> bd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False)
    ... # doctest: +ELLIPSIS
    (a    1.0
     b    2.0
     c    3.0
     d    4.0
     e    NaN
     dtype: float64,
     array([ 0,  2,  4,  6,  8, 10]))

    Use `drop` optional when bins is not unique

    >>> bd.cut(s, [0, 2, 4, 6, 10, 10], labels=False, retbins=True,
    ...        right=False, duplicates='drop')
    ... # doctest: +ELLIPSIS
    (a    1.0
     b    2.0
     c    3.0
     d    3.0
     e    NaN
     dtype: float64,
     array([ 0,  2,  4,  6, 10]))

    Passing an IntervalIndex for `bins` results in those categories exactly.
    Notice that values not covered by the IntervalIndex are set to NaN. 0
    is to the left of the first bin (which is closed on the right), and 1.5
    falls between two bins.

    >>> bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])

    >>> bd.cut(ks.Series([0, 0.5, 1.5, 2.5, 4.5]), bins)
    [NaN, (0.0, 1.0], NaN, (2.0, 3.0], (4.0, 5.0]]
    Categories (3, interval[int64, right]): [(0, 1] < (2, 3] < (4, 5]]
    """
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


def _convert_bin_to_numeric_type(bins, dtype):  # pragma: no cover
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
):  # pragma: no cover
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


def _searchsorted(x, bins, right):  # pragma: no cover
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
):  # pragma: no cover
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


def _infer_precision(base_precision: int, bins) -> int:  # pragma: no cover
    """
    Infer an appropriate precision for _round_frac
    """
    for precision in range(base_precision, 20):
        levels = [_round_frac(b, precision) for b in bins]
        if algos.unique(levels).size == bins.size:
            return precision
    return base_precision  # default


def _round_frac(x, precision: int):  # pragma: no cover
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
