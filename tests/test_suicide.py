from dataclasses import asdict

import pytest

from eds_scikit.datasets import load_suicide_attempt
from eds_scikit.event import tag_suicide_attempt
from eds_scikit.utils.test_utils import assert_equal, make_df

inputs = asdict(load_suicide_attempt())
expected_output = make_df(
    """
    person_id, visit_occurrence_id, SUICIDE_ATTEMPT_Haguenoer2008, SUICIDE_ATTEMPT_X60-X84, visit_start_datetime, visit_end_datetime
    1, 11, True, True, 2010-01-01 00:00:00, 2010-01-01 00:00:00
    1, 12, False, False, 2010-01-01 00:00:00, 2010-01-01 00:00:00
    2, 13, False, False, 2010-01-01 00:00:00, 2010-01-01 00:00:00
    3, 14, False, False, 2010-01-01 00:00:00, 2010-01-01 00:00:00
    4, 16, False, True, 2010-01-01 00:00:00, 2010-01-01 00:00:00
    """
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@assert_equal
def test_suicide_tagging_from_icd10(
    module, inputs=inputs, expected_output=expected_output
):

    vo = tag_suicide_attempt(
        visit_occurrence=inputs["visit_occurrence"],
        condition_occurrence=inputs["condition_occurrence"],
        date_min=None,
        date_max=None,
        algo="X60-X84",
    )
    vo.rename(columns={"SUICIDE_ATTEMPT": "SUICIDE_ATTEMPT_X60-X84"}, inplace=True)

    vo = tag_suicide_attempt(
        visit_occurrence=vo,
        condition_occurrence=inputs["condition_occurrence"],
        date_min=None,
        date_max=None,
        algo="Haguenoer2008",
    )
    vo.rename(
        columns={"SUICIDE_ATTEMPT": "SUICIDE_ATTEMPT_Haguenoer2008"}, inplace=True
    )

    return vo
