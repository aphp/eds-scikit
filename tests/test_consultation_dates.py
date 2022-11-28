from datetime import timedelta

import pandas as pd
import pytest

from eds_scikit.datasets import load_consultation_dates
from eds_scikit.event.consultations import get_consultation_dates
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order, day

ds = load_consultation_dates()

results = dict(
    min=pd.DataFrame(
        {
            "visit_occurrence_id": [0, 0, 1, 1, 1, 2, 2, 3, 3],
            "CONSULTATION_DATE": [
                day(1),
                day(5),
                day(2),
                day(6),
                day(9),
                day(1),
                day(5),
                day(2),
                day(9),
            ],
            "CONSULTATION_DATE_EXTRACTION": [
                "NLP+STRUCTURED",
                "NLP+STRUCTURED",
                "NLP",
                "STRUCTURED",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
            ],
            "CONSULTATION_ID": [
                "0-20200101",
                "0-20200105",
                "1-20200102",
                "1-20200106",
                "1-20200109",
                "2-20200101",
                "2-20200105",
                "3-20200102",
                "3-20200109",
            ],
        }
    ),
    first=pd.DataFrame(
        {
            "visit_occurrence_id": [0, 0, 0, 1, 1, 1, 2, 2, 3, 3],
            "CONSULTATION_DATE": [
                day(1),
                day(5),
                day(7),
                day(2),
                day(6),
                day(9),
                day(1),
                day(6),
                day(2),
                day(9),
            ],
            "CONSULTATION_DATE_EXTRACTION": [
                "NLP+STRUCTURED",
                "NLP+STRUCTURED",
                "NLP",
                "NLP",
                "STRUCTURED",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
            ],
            "CONSULTATION_ID": [
                "0-20200101",
                "0-20200105",
                "0-20200107",
                "1-20200102",
                "1-20200106",
                "1-20200109",
                "2-20200101",
                "2-20200106",
                "3-20200102",
                "3-20200109",
            ],
        }
    ),
    all=pd.DataFrame(
        {
            "visit_occurrence_id": [0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3],
            "CONSULTATION_DATE": [
                day(1),
                day(5),
                day(2),
                day(6),
                day(9),
                day(12),
                day(1),
                day(5),
                day(2),
                day(9),
                day(12),
            ],
            "CONSULTATION_DATE_EXTRACTION": [
                "NLP+STRUCTURED",
                "NLP+STRUCTURED",
                "NLP",
                "STRUCTURED",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
                "NLP",
            ],
            "CONSULTATION_ID": [
                "0-20200101",
                "0-20200105",
                "1-20200102",
                "1-20200106",
                "1-20200109",
                "1-20200112",
                "2-20200101",
                "2-20200105",
                "3-20200102",
                "3-20200109",
                "3-20200112",
            ],
        }
    ),
)


@pytest.mark.parametrize("dates_to_keep", ["min", "first", "all"])
@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_get_consultation_dates(dates_to_keep, module):

    vo = framework.to(module, ds.visit_occurrence)
    n = framework.to(module, ds.note)
    nnlp = framework.to(module, ds.note_nlp)

    cons = get_consultation_dates(
        vo,
        note=n,
        note_nlp=nnlp,
        algo=["structured", "nlp"],
        max_timedelta=timedelta(days=1),
        nlp_config=dict(dates_to_keep=dates_to_keep),
    )

    cons = framework.pandas(cons)

    assert_equal_no_order(cons, results[dates_to_keep])
