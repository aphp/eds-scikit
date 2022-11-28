from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.typing import DataFrame


def event_from_code(
    df: DataFrame,
    columns: Dict[str, str],
    visit_occurrence: Optional[DataFrame] = None,
    concept: str = "ICD10",
    codes: Optional[Dict[str, Union[str, List[str]]]] = None,
    date_from_visit: bool = True,
    additional_filtering: Dict[str, Any] = dict(),
    date_min: Optional[datetime] = None,
    date_max: Optional[datetime] = None,
) -> DataFrame:
    """
    Generic function to filter a DataFrame based on one of its column and an ensemble of codes to select from.

    For instance, this function is called when phenotyping via ICD-10 or CCAM.

    Parameters
    ----------
    df : DataFrame
        The DataFrame to filter.
    columns : Dict[str, str]
        Dictionary with the following keys:

        - `code_source_value` : The column name containing the code to filter
        - `code_start_datetime` : The column name containing the starting date
        - `code_end_datetime` : The column name containing the ending date
    visit_occurrence : Optional[DataFrame]
        The `visit_occurrence` DataFrame, only necessary if `date_from_visit` is set to `True`.
    concept : str
        The name of the extracted concept
    codes : Dict[str, Union[str, List[str]]]
        Dictionary which values are codes (as a unique string or as a list) and which keys are
        at least one of the following:

        - `exact`: To match the codes in `codes["exact"]` **exactly**
        - `prefix`: To match the codes in `codes["prefix"]` **as prefixes**
        - `regex`: To match the codes in `codes["regex"]` **as regexes**
        You can combine any of those keys.
    date_from_visit : bool
        If set to `True`, uses `visit_start_datetime` as the code datetime
    additional_filtering : Dict[str, Any]
        An optional dictionary to filter the resulting DataFrame.
        Keys should be column names on which too filter, and values should be either

        - A single value
        - A list or set of values.
    date_min : Optional[datetime]
        The minimum code datetime to keep. **Depends on the `date_from_visit` flag**
    date_max : Optional[datetime]
        The minimum code datetime to keep. **Depends on the `date_from_visit` flag**

    Returns
    -------
    DataFrame
        A DataFrame containing especially the following columns:

        - `t_start`
        - `t_end`
        - `concept` : The provided `concept` string
        - `value` : The matched code

    """

    required_columns = list(columns.values()) + ["visit_occurrence_id", "person_id"]
    check_columns(df, required_columns=required_columns)

    d_format = {"exact": r"{code}\b", "regex": r"{code}", "prefix": r"\b{code}"}
    regexes = []

    for code_type, code_list in codes.items():

        if type(code_list) == str:
            code_list = [code_list]
        codes_formated = [d_format[code_type].format(code=code) for code in code_list]
        regexes.append(r"(?:" + "|".join(codes_formated) + ")")

    final_regex = "|".join(regexes)

    mask = df[columns["code_source_value"]].str.contains(final_regex).fillna(False)

    event = df[mask]

    if date_from_visit:
        if visit_occurrence is None:
            raise ValueError(
                "With 'date_from_visit=True', you should provide a 'visit_occurrence' DataFrame."
            )
        event = event.merge(
            visit_occurrence[
                ["visit_occurrence_id", "visit_start_datetime", "visit_end_datetime"]
            ],
            on="visit_occurrence_id",
            how="inner",
        ).rename(
            columns={
                "visit_start_datetime": "t_start",
                "visit_end_datetime": "t_end",
            }
        )

    else:
        event.loc[:, "t_start"] = event.loc[:, columns["code_start_datetime"]]
        event.loc[:, "t_end"] = event.loc[:, columns["code_end_datetime"]]
        event = event.drop(
            columns=[columns["code_start_datetime"], columns["code_end_datetime"]]
        )

    event = _column_filtering(event, filtering_dict=additional_filtering)

    mask = True  # Resetting the mask

    if date_min is not None:
        mask = mask & (event.t_start >= date_min)

    if date_max is not None:
        mask = mask & (event.t_start <= date_max)

    if type(mask) != bool:  # We have a Series mask
        event = event[mask]

    event.loc[:, "concept"] = concept
    return event.rename(columns={columns["code_source_value"]: "value"})[
        [
            "person_id",
            "t_start",
            "t_end",
            "concept",
            "value",
            "visit_occurrence_id",
        ]
        + list(additional_filtering.keys())
    ].reset_index(drop=True)


def _column_filtering(df: DataFrame, filtering_dict: Dict[str, Any]):

    for col_name, col_value in filtering_dict.items():
        if col_value is None:
            df = df
        elif type(col_value) in {set, list}:
            col_value = set(col_value)
            df = df[df[col_name].isin(col_value)]
        else:
            df = df[df[col_name] == col_value]

    return df
