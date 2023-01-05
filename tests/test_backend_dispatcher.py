import logging
from datetime import datetime

import numpy as np
import pandas as pd
import pyspark
import pytest
from databricks import koalas as ks
from numpy.testing import assert_array_equal
from pandas.testing import assert_frame_equal

import eds_scikit
from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.utils.framework import bd

spark, sc, sql = eds_scikit.improve_performances()

data = load_person()
df = data.person


def assert_df_is_pandas(df):
    assert df.__class__.__module__.startswith(pd.__name__)


def assert_df_is_koalas(df):
    assert df.__class__.__module__.startswith(ks.__name__)


def test_get_backend():
    assert bd.get_backend(pd) is pd
    assert bd.get_backend(ks) is ks

    assert bd.get_backend(pd.DataFrame()) is pd
    assert bd.get_backend(ks.DataFrame()) is ks

    assert bd.get_backend(pyspark) is None
    assert bd.get_backend(np.array([])) is None
    assert bd.get_backend([pd.DataFrame()]) is None
    assert bd.get_backend([ks.DataFrame()]) is None


def test_is_pandas_is_koalas():
    assert bd.is_pandas(pd)
    assert not bd.is_pandas(ks)

    assert bd.is_koalas(ks)
    assert not bd.is_koalas(pd)


def test_to():
    kdf = ks.from_pandas(df)

    assert_df_is_pandas(bd.to(df, backend=pd))
    assert_df_is_koalas(bd.to(df, backend=ks))

    assert_df_is_pandas(bd.to(kdf, backend="pandas"))
    assert_df_is_koalas(bd.to(kdf, backend="koalas"))

    kdf_list = bd.to([df, df, df], backend="koalas")
    assert all([bd.is_koalas(_kdf) for _kdf in kdf_list])

    df_tuple = bd.to((kdf, kdf, kdf), backend="pandas")
    assert all([bd.is_pandas(_df) for _df in df_tuple])

    df_dict = bd.to({"df_1": kdf, "df_2": kdf}, backend="pandas")
    assert df_dict.keys() == {"df_1", "df_2"}
    assert all([bd.is_pandas(el) for el in df_dict.values()])

    with pytest.raises(ValueError, match="Unknown backend"):
        bd.to(df, backend="spark")


@pytest.mark.parametrize("backend", ["pd", pd, df])
def test_get_params_pd_backend(backend):

    today = datetime.today()
    deltas = today - df["birth_datetime"]
    deltas = deltas.dt.total_seconds()
    df["age"] = deltas / (365 * 24 * 3600)

    bins = np.arange(0, 100, 10)
    labels = [f"{left}-{right}" for left, right in zip(bins[:-1], bins[1:])]
    age_bins_ref = pd.cut(df["age"], bins=bins, labels=labels)

    age_bins = bd.cut(df["age"], bins=bins, labels=labels, backend=backend)
    assert_array_equal(age_bins_ref.astype(str), age_bins.astype(str))


@pytest.mark.parametrize("backend", ["ks", ks])
def test_get_params_ks_backend(backend):

    df = load_person().person

    kdf = ks.from_pandas(df)
    kdf = bd.add_unique_id(kdf, backend=backend)

    df = bd.add_unique_id(df, backend=pd)
    assert_array_equal(kdf["id"].to_pandas(), df["id"])

    with pytest.raises(ValueError, match="Unknown backend"):
        bd.add_unique_id(kdf, backend="spark")


def test_get_params_from_params():
    expected_result = pd.concat([df, df], axis=0)
    result = bd.concat([df, df], axis=0)
    assert_frame_equal(expected_result, result)

    kdf = ks.from_pandas(df)
    expected_result = ks.concat([kdf, kdf], axis=0).to_pandas()
    result = bd.concat([kdf, kdf], axis=0).to_pandas()
    assert_frame_equal(expected_result, result)

    with pytest.raises(ValueError):
        # mixing backend is not supported
        bd.concat([df, kdf], axis=0)


def test_get_params_from_method(caplog):

    with caplog.at_level(logging.WARNING):
        # Both pd.isna and ks.isna exist,
        # so not providing a "backend" argument will
        # raise a warning.
        bd.isna(1)

    assert bd.isna(1, backend="pandas") == bd.isna(1, backend="koalas")

    msg = (
        "Method 'optimize' doesn't belong to pandas or koalas "
        "and is not implemented in eds_scikit yet."
    )
    with pytest.raises(NotImplementedError, match=msg):
        bd.optimize()

    bd.value_counts(list("scikit"))
