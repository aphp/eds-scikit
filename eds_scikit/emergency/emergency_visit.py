# -*- coding: utf-8 -*-
from typing import Optional

from eds_scikit.emergency import tag_emergency_care_site
from eds_scikit.utils.checks import algo_checker, concept_checker
from eds_scikit.utils.typing import DataFrame

ALGOS = [
    "from_regex_on_parent_UF",
    "from_regex_on_care_site_description",
    "from_mapping",
    "from_vo_visit_source_value",
]


@algo_checker(algos=ALGOS)
def tag_emergency_visit(
    visit_detail: DataFrame,
    care_site: Optional[DataFrame] = None,
    visit_occurrence: Optional[DataFrame] = None,
    algo: str = "from_mapping",
) -> DataFrame:
    """Tag visits that correspond to **medical emergency units**.

    The tagging is done by adding a `"IS_EMERGENCY"` column to the provided DataFrame.

    Some algos can add an additional `"EMERGENCY_TYPE"` column to the provided DataFrame,
    providing a more detailled classification.

    It works by either [tagging each visit detail's care site][eds_scikit.emergency.emergency_care_site.tag_emergency_care_site],
    or by using the *visit_occurrence*'s `"visit_source_value"`.

    Parameters
    ----------
    visit_detail: DataFrame
    care_site: DataFrame
        Isn't necessary if the algo `"from_vo_visit_source_value"` is used
    visit_occurrence: DataFrame, optional.
        Is mandatory if the algo `"from_vo_visit_source_value"` is used
    algo: str
        Possible values are:

        - [`"from_mapping"`][eds_scikit.emergency.emergency_care_site.from_mapping] relies on a list of `care_site_source_value` extracted
          by Judith LEBLANC, Ariel COHEN and validated by an ER doctor. The emergency care sites
          are here further labelled to distinguish the different types of emergency
        - [`"from_regex_on_care_site_description"`][eds_scikit.emergency.emergency_care_site.from_regex_on_care_site_description]: relies on a specific list of RegEx
          applied on the description (= simplified care site name) of each care site.
        - [`"from_regex_on_parent_UF"`][eds_scikit.emergency.emergency_care_site.from_regex_on_parent_UF]: relies on a specific list of regular expressions
          applied on the description (= simplified care site name) of each UF (Unité Fonctionnelle).
          The obtained tag is then propagated to every UF's children.
        - [`"from_vo_visit_source_value"`][eds_scikit.emergency.emergency_visit.from_vo_visit_source_value]:
        relies on the parent visit occurrence of each visit detail:
          A visit detail will be tagged as emergency if it belongs to a visit occurrence where
          `visit_occurrence.visit_source_value=='urgence'`.


    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 to 2 added columns corresponding to the following concepts:

        - `"IS_EMERGENCY"`
        - `"EMERGENCY_TYPE"` (if using algo `"from_mapping"`)
    """

    if algo == "from_vo_visit_source_value":
        return from_vo_visit_source_value(visit_detail, visit_occurrence)

    else:
        initial_care_site_columns = set(care_site.columns)
        tagged_care_site = tag_emergency_care_site(care_site, algo=algo)
        to_add_columns = list(
            set(tagged_care_site) - initial_care_site_columns | set(["care_site_id"])
        )

        return visit_detail.merge(
            tagged_care_site[to_add_columns], on="care_site_id", how="left"
        )


@concept_checker(concepts=["IS_EMERGENCY"])
def from_vo_visit_source_value(
    visit_detail: DataFrame,
    visit_occurrence: DataFrame,
) -> DataFrame:
    """
    This algo uses the *"Type de dossier"* of each visit detail's parent visit occurrence.
    Thus, a visit_detail will be tagged with `IS_EMERGENCY=True` iff the visit occurrence it belongs to
    is an emergency-type visit (meaning that `visit_occurrence.visit_source_value=='urgence'`)

    !!! aphp "Admission through ICU"
         At AP-HP, when a patient is hospitalized after coming to the ICU, its `visit_source_value`
         is set from `"urgence"` to `"hospitalisation complète"`. So you should keep in mind
         that this method doesn't tag those visits as ICU.

    Parameters
    ----------
    visit_detail: DataFrame
    visit_occurrence: DataFrame

    Returns
    -------
    visit_detail: DataFrame
        Dataframe with added columns corresponding to the following conceps:

        - `"IS_EMERGENCY"`
    """
    vo_emergency = visit_occurrence[["visit_occurrence_id", "visit_source_value"]]
    vo_emergency["IS_EMERGENCY"] = visit_occurrence.visit_source_value == "urgence"

    return visit_detail.merge(
        vo_emergency[["visit_occurrence_id", "IS_EMERGENCY"]],
        on="visit_occurrence_id",
        how="left",
    )
