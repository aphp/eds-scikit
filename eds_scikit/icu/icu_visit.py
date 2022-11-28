# -*- coding: utf-8 -*-
from eds_scikit.icu import tag_icu_care_site
from eds_scikit.utils.checks import algo_checker
from eds_scikit.utils.typing import DataFrame

ALGOS = [
    "from_authorisation_type",
    "from_regex_on_care_site_description",
]


@algo_checker(algos=ALGOS)
def tag_icu_visit(
    visit_detail: DataFrame,
    care_site: DataFrame,
    algo: str = "from_authorisation_type",
) -> DataFrame:
    """Tag care_sites that correspond to **ICU units**.

    The tagging is done by adding a `"IS_ICU"` column to the provided DataFrame.

    It works by [tagging each visit detail's care site][eds_scikit.icu.icu_care_site.tag_icu_care_site].

    Parameters
    ----------
    visit_detail: DataFrame
    care_site: DataFrame
    algo: str
        Possible values are:

        - [`"from_authorisation_type"`][eds_scikit.icu.icu_care_site.from_authorisation_type]
        - [`"from_regex_on_care_site_description"`][eds_scikit.icu.icu_care_site.from_regex_on_care_site_description]

    Returns
    -------
    visit_detail: DataFrame
        Dataframe with 1 added column corresponding to the following concept:

        - `"IS_ICU"`

    """
    tagged_care_site = tag_icu_care_site(care_site, algo=algo)

    return visit_detail.merge(
        tagged_care_site[["care_site_id", "IS_ICU"]], on="care_site_id", how="left"
    )
