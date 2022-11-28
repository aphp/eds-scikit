from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from eds_scikit.event import conditions_from_icd10
from eds_scikit.utils.typing import DataFrame

DEFAULT_DIABETE_FROM_ICD10_CONFIG = dict(
    codes=dict(
        DIABETES_TYPE_I=dict(
            prefix="E10",
        ),
        DIABETES_TYPE_II=dict(
            prefix="E11",
        ),
        DIABETES_MALNUTRITION=dict(
            prefix="E12",
        ),
        DIABETES_IN_PREGNANCY=dict(
            prefix="O24",
        ),
        OTHER_DIABETES_MELLITUS=dict(
            prefix=["E13", "E14"],
        ),
        DIABETES_INSIPIDUS=dict(
            exact=["E232", "N251"],
        ),
    ),
    date_from_visit=True,
    additional_filtering=dict(condition_status_source_value={"DP", "DAS"}),
)
"""
Default parameters feeded to [conditions_from_icd10()][eds_scikit.event.icd10.conditions_from_icd10]
"""


def diabetes_from_icd10(
    condition_occurrence: DataFrame,
    visit_occurrence: DataFrame,
    date_min: Optional[datetime] = None,
    date_max: Optional[datetime] = None,
    codes: Dict[str, Union[str, List[str]]] = DEFAULT_DIABETE_FROM_ICD10_CONFIG[
        "codes"
    ],
    date_from_visit: bool = DEFAULT_DIABETE_FROM_ICD10_CONFIG["date_from_visit"],
    additional_filtering: Dict[str, Any] = DEFAULT_DIABETE_FROM_ICD10_CONFIG[
        "additional_filtering"
    ],
) -> DataFrame:
    """
    Wrapper around the [conditions_from_icd10()][eds_scikit.event.icd10.conditions_from_icd10] function.
    Check the [default configuration][eds_scikit.event.diabetes.DEFAULT_DIABETE_FROM_ICD10_CONFIG] to see
    the used parameters

    Parameters
    ----------
    condition_occurrence
        OMOP-like condition occurrence DataFrame
    visit_occurrence : Optional[DataFrame]
        OMOP-like visit_occurrence DataFrame
    date_min : Optional[datetime]
        Lower temporal bound
    date_max : Optional[datetime]
        Upper temporal bound
    codes : Optional[Dict[str, Union[str, List[str]]]]
        Dictionary of ICD-10 used for phenotyping
    date_from_visit : bool, by default True
        If true, use the `visit_[start/end]_datetime` for filtering. Else, use `condition_start_datetime`
    additional_filtering : Dict[str, Any]
        A dictionary to perform additional filtering.

        - **Each key** should be a valid column name from `condition_occurrence`
        - **Each value** should be a value / set of values / list of values
        For each pair (key, value), filtering is done as `condition_occurrence[condition_occurrence[k].isin(v)]`

    Returns
    -------
    DataFrame
        Event DataFrame in **long** format (with a `concept` and a `value` column).
        The `concept` column contains one of the following:

        - DIABETES_TYPE_I
        - DIABETES_TYPE_II
        - DIABETES_MALNUTRITION
        - DIABETES_IN_PREGNANCY
        - OTHER_DIABETES_MELLITUS
        - DIABETES_INSIPIDUS
        The `value` column contains the corresponding ICD-10 code that was extracted
    """
    diabetes = conditions_from_icd10(
        condition_occurrence=condition_occurrence,
        visit_occurrence=visit_occurrence,
        date_min=date_min,
        date_max=date_max,
        codes=codes,
        date_from_visit=date_from_visit,
        additional_filtering=additional_filtering,
    )

    diabetes["value"] = diabetes["concept"]
    diabetes["concept"] = "DIABETES_FROM_ICD10"

    return diabetes
