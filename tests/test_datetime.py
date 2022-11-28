from datetime import datetime

import pandas as pd
import pytest

from eds_scikit.utils import framework
from eds_scikit.utils.datetime_helpers import add_timedelta, substract_datetime
from eds_scikit.utils.test_utils import assert_equal_no_index

df = pd.DataFrame(
    data=dict(
        start=[datetime(2020, 1, 1), datetime(2020, 1, 10)],
        end=[datetime(2020, 1, 3), datetime(2020, 1, 15)],
    )
)

expected_results = dict(
    added=pd.Series([datetime(2020, 1, 2), datetime(2020, 1, 11)], name="added"),
    sub_hours=pd.Series([48.0, 120.0], name="sub_hours"),
    sub_seconds=pd.Series([3600 * 48.0, 3600 * 120.0], name="sub_seconds"),
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_datetime_helpers(module):

    converted_df = framework.to(module, df)

    results = dict()

    results["added"] = add_timedelta(converted_df["start"], days=1)
    results["sub_hours"] = substract_datetime(
        converted_df["end"], converted_df["start"], out="hours"
    )
    results["sub_seconds"] = substract_datetime(
        converted_df["end"], converted_df["start"], out="seconds"
    )

    for k, res in results.items():
        res.name = k
        assert_equal_no_index(
            expected_results[k].to_frame(),
            framework.to(module, res).to_frame(),
            check_like=True,
            check_dtype=False,
        )
