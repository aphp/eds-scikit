from datetime import datetime
from typing import Dict, List, Optional, Union

from eds_scikit.event import event_from_code
from eds_scikit.utils.framework import get_framework
from eds_scikit.utils.typing import DataFrame


def procedures_from_ccam(
    procedure_occurrence: DataFrame,
    visit_occurrence: Optional[DataFrame] = None,
    codes: Optional[Dict[str, Union[str, List[str]]]] = None,
    date_from_visit: bool = True,
    additional_filtering=dict(),
    date_min: Optional[datetime] = None,
    date_max: Optional[datetime] = None,
) -> DataFrame:
    """

    Phenotyping based on CCAM codes.

    Parameters
    ----------
    procedure_occurrence : DataFrame
        `procedure_occurrence` OMOP DataFrame.
    visit_occurrence : Optional[DataFrame]
        `visit_occurrence` OMOP DataFrame, only necessary if `date_from_visit` is set to `True`.
    codes : Dict[str, Union[str, List[str]]]
        Dictionary which values are CCAM codes (as a unique string or as a list) and which keys are
        at least one of the following:

        - `exact`: To match the codes in `codes["exact"]` **exactly**
        - `prefix`: To match the codes in `codes["prefix"]` **as prefixes**
        - `regex`: To match the codes in `codes["regex"]` **as regexes**
        You can combine any of those keys.
    date_from_visit : bool
        If set to `True`, uses `visit_start_datetime` as the code datetime
    additional_filtering : Dict[str, Any]
        An optional dictionary to filter the resulting DataFrame.

        Keys should be column names on which to filter, and values should be either

        - A single value
        - A list or set of values.
    date_min : Optional[datetime]
        The minimum code datetime to keep. **Depends on the `date_from_visit` flag**
    date_max : Optional[datetime]
        The minimum code datetime to keep. **Depends on the `date_from_visit` flag**

    Returns
    -------
    DataFrame
        "event" DataFrame including the following columns:

        - `t_start`: If `date_from_visit` is set to `False`, contains `procedure_datetime`,
        else contains `visit_start_datetime`
        - `t_end`: If `date_from_visit` is set to `False`, contains `procedure_datetime`,
        else contains `visit_end_datetime`
        - `concept` : contaning values from `codes.keys()`
        - `value` : The extracted CCAM code.
        - `visit_occurrence_id` : the `visit_occurrence_id` from the visit which contains the CCAM code.
    """  # noqa: E501

    procedure_columns = dict(
        code_source_value="procedure_source_value",
        code_start_datetime="procedure_datetime",
        code_end_datetime="procedure_datetime",
    )
    events = []

    for concept, code_dict in codes.items():
        tmp_df = event_from_code(
            df=procedure_occurrence,
            columns=procedure_columns,
            visit_occurrence=visit_occurrence,
            concept=concept,
            codes=code_dict,
            date_from_visit=date_from_visit,
            additional_filtering=additional_filtering,
            date_min=date_min,
            date_max=date_max,
        )

        events.append(tmp_df)

    framework = get_framework(procedure_occurrence)
    return framework.concat(events)
