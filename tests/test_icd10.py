from dataclasses import asdict
from datetime import datetime as dt

import pytest

from eds_scikit.datasets import load_icd10
from eds_scikit.event import conditions_from_icd10
from eds_scikit.utils.test_utils import assert_equal, make_df

inputs = asdict(load_icd10())
expected_output = make_df(
    """
    person_id, t_start, t_end, concept, value, condition_status_source_value, visit_occurrence_id
    1, 2010-01-01 00:00:00,2010-01-01 00:00:00, C, C10, DP, 11
    1, 2010-01-01 00:00:00,2010-01-01 00:00:00, E, E112, DAS, 12
    1, 2012-01-01 00:00:00,2012-01-01 00:00:00, D, D20, DAS, 13
    1, 2020-01-01 00:00:00,2020-01-01 00:00:00, A, A20, DP, 14
    1, 2020-01-01 00:00:00,2020-01-01 00:00:00, A, A21, DP, 15
    """
)

codes = dict(
    E=dict(prefix="E11"),
    C=dict(exact="C10"),
    D=dict(prefix=["D2"]),
    A=dict(regex=r"A2[01]"),
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@assert_equal
def test_tagging_from_icd10(
    module,
    inputs=inputs,
    expected_output=expected_output,
):

    output = conditions_from_icd10(
        visit_occurrence=inputs["visit_occurrence"],
        condition_occurrence=inputs["condition_occurrence"],
        codes=codes,
        date_min=dt(2000, 1, 1),
        date_max=dt(2030, 1, 1),
    )

    return output
