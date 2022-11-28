from dataclasses import asdict
from datetime import datetime as dt

import pytest

from eds_scikit.datasets import load_ccam
from eds_scikit.event import procedures_from_ccam
from eds_scikit.utils.test_utils import assert_equal, make_df

inputs = asdict(load_ccam())
expected_output = make_df(
    """
    person_id, t_start, t_end, concept, value, visit_occurrence_id
    1, 2010-01-01 00:00:00,2010-01-01, CARDIO_CCAM, DZEA001, 11
    1, 2010-01-01 00:00:00,2010-01-01, CARDIO_CCAM, DZEA003, 12
    2, 2012-01-01 00:00:00,2012-01-01, PULMO_CCAM, GFEA004, 13
    """
)

codes = dict(
    CARDIO_CCAM=dict(regex=r"DZEA00[0-4]"),
    PULMO_CCAM=dict(regex=r"GFEA00[0-7]"),
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@assert_equal
def test_tagging_from_ccam(
    module,
    inputs=inputs,
    expected_output=expected_output,
):

    output = procedures_from_ccam(
        visit_occurrence=inputs["visit_occurrence"],
        procedure_occurrence=inputs["procedure_occurrence"],
        codes=codes,
        date_min=dt(2010, 1, 1),
        date_max=dt(2030, 1, 1),
    )

    return output
