from datetime import timedelta
from typing import Any, Dict, List, Optional, Union

from eds_scikit.utils.checks import concept_checker
from eds_scikit.utils.datetime_helpers import substract_datetime
from eds_scikit.utils.framework import bd, get_framework
from eds_scikit.utils.typing import DataFrame


@concept_checker(
    concepts=[
        "CONSULTATION_DATE",
        "CONSULTATION_ID",
        "CONSULTATION_DATE_EXTRACTION",
    ]
)
def get_consultation_dates(
    vo: DataFrame,
    note: DataFrame,
    note_nlp: Optional[DataFrame] = None,
    algo: Union[str, List[str]] = ["nlp"],
    max_timedelta: timedelta = timedelta(days=7),
    structured_config: Dict[str, Any] = dict(),
    nlp_config: Dict[str, Any] = dict(),
) -> DataFrame:
    """
    Extract consultation dates.
    See the implementation details of the algo(s) you want to use

    Parameters
    ----------
    vo : DataFrame
        `visit_occurrence` DataFrame
    note : DataFrame
        `note` DataFrame
    note_nlp : Optional[DataFrame]
        `note_nlp` DataFrame, used only with the `"nlp"` algo
    algo: Union[str, List[str]] = ["nlp"]
        Algorithm(s) to use to determine consultation dates.
        Multiple algorithms can be provided as a list. Accepted values are:

        - `"structured"`: See [get_consultation_dates_structured()][eds_scikit.event.consultations.get_consultation_dates_structured]
        - `"nlp"`: See [get_consultation_dates_nlp()][eds_scikit.event.consultations.get_consultation_dates_nlp]
    max_timedelta: timedelta = timedelta(days=7)
        If two extracted consultations are spaced by less than `max_timedelta`,
        we consider that they correspond to the same event and only keep the first one.
    structured_config : Dict[str, Any] = dict()
        A dictionnary of parameters when using the [`structured`][eds_scikit.event.consultations.get_consultation_dates_structured] algorithm
    nlp_config : Dict[str, Any] = dict()
        A dictionnary of parameters when using the [`nlp`][eds_scikit.event.consultations.get_consultation_dates_nlp] algorithm

    Returns
    -------
    DataFrame
        Event type DataFrame with the following columns:

        - `person_id`
        - `visit_occurrence_id`
        - `CONSULTATION_DATE`: corresponds to the `note_datetime` value of a consultation
          report coming from the considered visit.
        - `CONSULTATION_NOTE_ID`: the `note_id` of the corresponding report.
        - `CONSULTATION_DATE_EXTRACTION`: the method of extraction

    """

    fw = get_framework(vo)

    if type(algo) == str:
        algo = [algo]

    dates = []

    for a in algo:
        if a == "structured":
            dates.append(
                get_consultation_dates_structured(
                    vo=vo,
                    note=note,
                    **structured_config,
                )
            )
        if a == "nlp":
            dates.append(
                get_consultation_dates_nlp(
                    note_nlp=note_nlp,
                    **nlp_config,
                )
            )

    dates_per_note = (
        fw.concat(dates)
        .reset_index()
        .merge(note[["note_id", "visit_occurrence_id"]], on="note_id", how="inner")
    )

    # Remove timezone errors from spark
    dates_per_note["CONSULTATION_DATE"] = dates_per_note["CONSULTATION_DATE"].astype(
        str
    )

    dates_per_visit = (
        dates_per_note.groupby(["visit_occurrence_id", "CONSULTATION_DATE"])[
            "CONSULTATION_DATE_EXTRACTION"
        ]
        .unique()
        .apply(sorted)
        .str.join("+")
    )

    dates_per_visit.name = "CONSULTATION_DATE_EXTRACTION"

    dates_per_visit = bd.add_unique_id(
        dates_per_visit.reset_index(), col_name="TMP_CONSULTATION_ID"
    )

    # Convert back to datetime format
    dates_per_visit["CONSULTATION_DATE"] = bd.to_datetime(
        dates_per_visit["CONSULTATION_DATE"], errors="coerce"
    )

    dates_per_visit = clean_consultations(
        dates_per_visit,
        max_timedelta,
    )

    # Equivalent to df.spark.cache() for ks.DataFrame
    bd.cache(dates_per_visit)

    return dates_per_visit


def get_consultation_dates_structured(
    note: DataFrame,
    vo: Optional[DataFrame] = None,
    kept_note_class_source_value: Optional[Union[str, List[str]]] = "CR-CONS",
    kept_visit_source_value: Optional[Union[str, List[str]]] = "consultation externe",
) -> DataFrame:
    """
    Uses `note_datetime` value to infer *true* consultation dates

    Parameters
    ----------
    note : DataFrame
        A `note` DataFrame with at least the following columns:

        - `note_id`
        - `note_datetime`
        - `note_source_value` **if** `kept_note_class_source_value is not None`
        - `visit_occurrence_id` **if** `kept_visit_source_value is not None`
    vo : Optional[DataFrame]
        A visit_occurrence DataFrame to provide **if** `kept_visit_source_value is not None`,
        with at least the following columns:

        - `visit_occurrence_id`
        - `visit_source_value` **if** `kept_visit_source_value is not None`
    kept_note_class_source_value : Optional[Union[str, List[str]]]
        Value(s) allowed for the `note_class_source_value` column.
    kept_visit_source_value : Optional[Union[str, List[str]]], optional
        Value(s) allowed for the `visit_source_value` column.

    Returns
    -------
    Dataframe
        With 2 added columns corresponding to the following concept:

        - `CONSULTATION_DATE`, containing the date
        - `CONSULTATION_DATE_EXTRACTION`, containing `"STRUCTURED"`
    """

    kept_note = note

    if kept_note_class_source_value is not None:
        if type(kept_note_class_source_value) == str:
            kept_note_class_source_value = [kept_note_class_source_value]
        kept_note = note[
            note.note_class_source_value.isin(set(kept_note_class_source_value))
        ]

    if kept_visit_source_value is not None:
        if type(kept_visit_source_value) == str:
            kept_visit_source_value = [kept_visit_source_value]
        kept_note = kept_note.merge(
            vo[
                [
                    "visit_occurrence_id",
                    "visit_source_value",
                ]
            ][vo.visit_source_value.isin(set(kept_visit_source_value))],
            on="visit_occurrence_id",
        )

    dates_per_note = kept_note[["note_datetime", "note_id"]].rename(
        columns={
            "note_datetime": "CONSULTATION_DATE",
        }
    )

    dates_per_note["CONSULTATION_DATE_EXTRACTION"] = "STRUCTURED"

    return dates_per_note.set_index("note_id")


def get_consultation_dates_nlp(
    note_nlp: DataFrame,
    dates_to_keep: str = "min",
) -> DataFrame:
    """
    Uses consultation dates extracted *a priori* in consultation reports to infer *true* consultation dates

    Parameters
    ----------
    note_nlp : DataFrame
        A DataFrame with (at least) the following columns:

        - `note_id`
        - `consultation_date`
        - `end` **if** using `dates_to_keep=first`:
        `end` should store the character offset of the extracted date.
    dates_to_keep : str, optional
        How to handle multiple consultation dates found in the document:

        - `min`: keep the oldest one
        - `first`: keep the occurrence that appeared first in the text
        - `all`: keep all date

    Returns
    -------
    Dataframe
        With 2 added columns corresponding to the following concept:

        - `CONSULTATION_DATE`, containing the date
        - `CONSULTATION_DATE_EXTRACTION`, containing `"NLP"`
    """

    if dates_to_keep == "min":
        dates_per_note = note_nlp.groupby("note_id").agg(
            CONSULTATION_DATE=("consultation_date", "min"),
        )
    elif dates_to_keep == "first":
        dates_per_note = (
            note_nlp.sort_values(by="start")
            .groupby("note_id")
            .agg(CONSULTATION_DATE=("consultation_date", "first"))
        )
    elif dates_to_keep == "all":
        dates_per_note = note_nlp[["consultation_date", "note_id"]].set_index("note_id")
        dates_per_note = dates_per_note.rename(
            columns={"consultation_date": "CONSULTATION_DATE"}
        )
    dates_per_note["CONSULTATION_DATE_EXTRACTION"] = "NLP"

    return dates_per_note


def clean_consultations(
    dates,
    max_timedelta,
):
    # Cartesian product
    merged = dates.merge(
        dates,
        on="visit_occurrence_id",
        how="inner",
        suffixes=("_1", "_2"),
    )

    # Keeping only consultations where 1 occurs before 2
    merged = merged[merged["CONSULTATION_DATE_1"] <= merged["CONSULTATION_DATE_2"]]

    # Checking correct distance
    th = max_timedelta.total_seconds()

    merged["delta"] = substract_datetime(
        merged["CONSULTATION_DATE_2"], merged["CONSULTATION_DATE_1"]
    )
    merged["to_merge"] = (merged["delta"] <= th).astype(int)

    # If the only previous consultation to be merged with is itself, we found our first consultation!
    first_consult_mask = merged.groupby("TMP_CONSULTATION_ID_2")["to_merge"].sum() == 1
    first_consult_mask.index.name = None
    dates.index.name = None

    results = dates[first_consult_mask]

    results["CONSULTATION_ID"] = (
        results["visit_occurrence_id"].astype(str)
        + "-"
        + results["CONSULTATION_DATE"].dt.strftime("%Y%m%d")
    )
    return results.drop(columns=["TMP_CONSULTATION_ID"])
