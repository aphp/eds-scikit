import pandas as pd
import pytest

from eds_scikit.datasets import load_visit_merging
from eds_scikit.period.stays import merge_visits
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order

ds = load_visit_merging()

all_params = dict(
    remove_deleted_visits=[False, True, True],
    long_stay_filtering=["all", "open", None],
    merge_different_hospitals=[False, True, False],
    merge_different_source_values=[True, False, ["hospitalisés", "urgence"]],
)
all_params = pd.DataFrame(all_params).to_dict("records")

visit_occurrence_ids = ds.visit_occurrence.visit_occurrence_id.values

all_results = [
    pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "STAY_ID": ["A", "A", "C", "C", "E", "F", "G"],
            "CONTIGUOUS_STAY_ID": ["A", "A", "C", "C", "E", "F", "G"],
        }
    ),
    pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "STAY_ID": ["A", "B", "C", "D", "C", "F", "G"],
            "CONTIGUOUS_STAY_ID": ["A", "B", "C", "D", "E", "F", "G"],
        }
    ),
    pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "STAY_ID": ["A", "G", "G", "G", "E", "G", "G"],
            "CONTIGUOUS_STAY_ID": ["A", "G", "G", "G", "E", "G", "G"],
        }
    ),
]


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize(
    "params, results",
    [(params, results) for params, results in zip(all_params, all_results)],
)
def test_visit_merging(module, params, results):

    results = framework.to(module, results)

    vo = framework.to(module, ds.visit_occurrence)
    merged = merge_visits(vo, **params)
    merged = framework.pandas(merged)

    assert_equal_no_order(
        merged[["visit_occurrence_id", "STAY_ID", "CONTIGUOUS_STAY_ID"]], results
    )
