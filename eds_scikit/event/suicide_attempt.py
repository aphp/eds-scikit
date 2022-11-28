from datetime import datetime
from typing import Optional

from eds_scikit.utils.checks import algo_checker, concept_checker
from eds_scikit.utils.typing import DataFrame

from . import conditions_from_icd10

ALGOS = ["X60-X84", "Haguenoer2008"]

CONCEPT = "SUICIDE_ATTEMPT"

DEFAULT_CONFIG = {
    "X60-X84": dict(
        codes={
            CONCEPT: dict(
                regex=["X[67]", "X8[0-4]"],
            ),
        },
        date_from_visit=True,
        additional_filtering=dict(condition_status_source_value=None),
    ),
    "Haguenoer2008": dict(
        codes={
            f"{CONCEPT}_BIS": dict(
                regex=["S", "T[0-9]"],
            ),
        },
        date_from_visit=True,
        additional_filtering=dict(condition_status_source_value="DP"),
    ),
}


@concept_checker(concepts=["SUICIDE_ATTEMPT"])
@algo_checker(algos=ALGOS)
def tag_suicide_attempt(
    visit_occurrence: DataFrame,
    condition_occurrence: DataFrame,
    date_min: Optional[datetime] = None,
    date_max: Optional[datetime] = None,
    algo: str = "X60-X84",
) -> DataFrame:
    """
    Function to return visits that fulfill different definitions of suicide attempt by ICD10.

    Parameters
    ----------
    visit_occurrence: DataFrame
    condition_occurrence: DataFrame
    date_min: datetime
        Minimal starting date (on `visit_start_datetime`)
    date_max: datetime
        Maximal starting date (on `visit_start_datetime`)
    algo: str
        Method to use. Available values are:

        - `"X60-X84"`: Will return a the visits that have at least one ICD code that belongs to the range X60 to X84.
        - `"Haguenoer2008"`: Will return a the visits that follow the definiton of "*Haguenoer, Ken, Agnès Caille, Marc Fillatre, Anne Isabelle Lecuyer, et Emmanuel Rusch. « Tentatives de Suicide », 2008, 4.*". This rule requires at least one Main Diagnostic (DP) belonging to S00 to T98, and at least one Associated Diagnostic (DAS) that belongs to the range X60 to X84.

    Returns
    -------
    visit_occurrence: DataFrame
        Tagged with an additional column `SUICIDE_ATTEMPT`

    !!! tip
         These rules were implemented in the CSE project n°210013

    """

    events_1 = conditions_from_icd10(
        condition_occurrence,
        visit_occurrence=visit_occurrence,
        date_min=date_min,
        date_max=date_max,
        **DEFAULT_CONFIG["X60-X84"],
    )

    events_1 = events_1[
        ["visit_occurrence_id", "condition_status_source_value"]
    ].drop_duplicates(subset="visit_occurrence_id")
    events_1[CONCEPT] = True

    if algo == "X60-X84":

        visit_occurrence_tagged = visit_occurrence.merge(
            events_1[["visit_occurrence_id", CONCEPT]],
            on="visit_occurrence_id",
            how="left",
        )

        visit_occurrence_tagged[CONCEPT].fillna(False, inplace=True)

        return visit_occurrence_tagged

    if algo == "Haguenoer2008":

        events_1 = events_1[events_1.condition_status_source_value == "DAS"]

        events_2 = conditions_from_icd10(
            condition_occurrence,
            visit_occurrence=visit_occurrence,
            date_min=date_min,
            date_max=date_max,
            **DEFAULT_CONFIG[algo],
        )

        events_2 = events_2[["visit_occurrence_id"]].drop_duplicates()
        events_2[f"{CONCEPT}_BIS"] = True

        visit_occurrence_tagged = visit_occurrence.merge(
            events_1[["visit_occurrence_id", CONCEPT]],
            on="visit_occurrence_id",
            how="left",
        ).merge(
            events_2[["visit_occurrence_id", f"{CONCEPT}_BIS"]],
            on="visit_occurrence_id",
            how="left",
        )

        visit_occurrence_tagged[CONCEPT] = (
            visit_occurrence_tagged[CONCEPT] & visit_occurrence_tagged[f"{CONCEPT}_BIS"]
        )

        visit_occurrence_tagged = visit_occurrence_tagged.drop(
            columns=[f"{CONCEPT}_BIS"]
        )

        return visit_occurrence_tagged
