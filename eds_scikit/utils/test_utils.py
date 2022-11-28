import io
from datetime import datetime as dt

import numpy as np
import pandas as pd
from decorator import decorator
from PIL import Image

from eds_scikit.utils.checks import _get_arg_value
from eds_scikit.utils.typing import DataObject

from . import framework


def make_df(
    string: str,
    autoconvert_datetimes: bool = True,
    **kwargs,
):
    buffer = io.StringIO(string)
    df = pd.read_csv(buffer, skipinitialspace=True, **kwargs)
    if autoconvert_datetimes:
        for (col, dtype) in df.dtypes.iteritems():
            if dtype == "object":
                if df[col].str.match(r"\d{4}-\d{2}-\d{2}.*").any():
                    df[col] = pd.to_datetime(df[col])
    return df


def assert_equal_no_index(left: DataObject, right: DataObject, **kwargs):
    return pd.testing.assert_frame_equal(
        framework.pandas(left).reset_index(drop=True),
        framework.pandas(right).reset_index(drop=True),
        **kwargs,
    )


def assert_equal_no_order(left: DataObject, right: DataObject, **kwargs):
    def sorted_df(df):
        cols = sorted(df.columns)
        return df.loc[:, cols].sort_values(by=cols)

    return assert_equal_no_index(sorted_df(left), sorted_df(right), **kwargs)


def day(i):
    return dt(2020, 1, i)


def date(s):
    return dt.strptime(s, "%Y-%m-%d")


@decorator
def assert_equal(
    test_function,
    *args,
    **kwargs,
):

    inputs, index_or_key = _get_arg_value(
        test_function,
        argname="inputs",
        args=args,
        kwargs=kwargs,
        return_index_or_key=True,
    )
    expected_output = _get_arg_value(
        test_function,
        argname="expected_output",
        args=args,
        kwargs=kwargs,
    )

    module = _get_arg_value(
        test_function,
        argname="module",
        args=args,
        kwargs=kwargs,
    )

    for input_name, input_df in inputs.items():
        inputs[input_name] = framework.to(module, input_df)

    if type(index_or_key) == int:
        args = list(args)
        args[index_or_key] = inputs
        args = tuple(args)
    elif type(index_or_key) == str:
        kwargs[index_or_key] = inputs

    output = test_function(*args, **kwargs)

    assert_equal_no_order(output, expected_output)

    return output


def assert_images_equal(image_1: str, image_2: str):
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    sum_sq_diff = np.sum(
        (np.asarray(img1).astype("float") - np.asarray(img2).astype("float")) ** 2
    )

    if sum_sq_diff == 0:
        # Images are exactly the same
        pass
    else:
        normalized_sum_sq_diff = sum_sq_diff / np.sqrt(sum_sq_diff)
        assert normalized_sum_sq_diff < 0.001
