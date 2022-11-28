from datetime import datetime as dt

import pandas as pd
import pytest
from numpy import nan as NaN

from eds_scikit.datasets import load_stay_duration
from eds_scikit.period.stays import get_stays_duration
from eds_scikit.utils import framework
from eds_scikit.utils.checks import MissingConceptError
from eds_scikit.utils.test_utils import assert_equal_no_order

ds = load_stay_duration()

all_params = dict(
    algo=["sum_of_visits_duration", "visits_date_difference"],
    missing_end_date_handling=["fill", "coerce"],
    open_stay_end_datetime=[dt(2022, 1, 1), None],
)
all_params = pd.DataFrame(all_params).to_dict("records")


all_expected_results = [
    pd.DataFrame(
        {
            "STAY_ID": ["A", "C", "D", "F"],
            "STAY_DURATION": [
                168.0,
                24.0,
                168.0,
                (dt(2022, 1, 1) - dt(2017, 1, 1)).total_seconds() / 3600,
            ],
        }
    ),
    pd.DataFrame(
        {
            "STAY_ID": ["A", "C", "D", "F"],
            "STAY_DURATION": [168.0, 24.0, 192.0, NaN],
        }
    ),
]


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize(
    "params, expected_results",
    [
        (params, expected_results)
        for params, expected_results in zip(all_params, all_expected_results)
    ],
)
def test_stay_duration(module, params, expected_results):

    stays = framework.to(module, ds.stays)

    results = get_stays_duration(stays, **params)
    results = framework.pandas(results)

    # Handling rounding error + dt.now() approximation
    results["STAY_DURATION"] = results["STAY_DURATION"].round(0)
    expected_results["STAY_DURATION"] = expected_results["STAY_DURATION"].round(0)
    results = results[["STAY_DURATION"]].reset_index()

    assert_equal_no_order(results, expected_results)


def test_stay_duration_missing_concept():
    with pytest.raises(MissingConceptError):
        _ = get_stays_duration(ds.stays.drop(columns=["STAY_ID"]))
