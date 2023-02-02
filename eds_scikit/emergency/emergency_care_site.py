# -*- coding: utf-8 -*-
from typing import Optional

from eds_scikit.resources import registry, versionize
from eds_scikit.structures import attributes
from eds_scikit.utils import framework
from eds_scikit.utils.checks import algo_checker, concept_checker
from eds_scikit.utils.typing import DataFrame

ALGOS = [
    "from_regex_on_parent_UF",
    "from_regex_on_care_site_description",
    "from_mapping",
]


@algo_checker(algos=ALGOS)
def tag_emergency_care_site(
    care_site: DataFrame,
    algo: str = "from_mapping",
) -> DataFrame:
    """Tag care sites that correspond to **medical emergency units**.

    The tagging is done by adding a `"IS_EMERGENCY"` column to the provided DataFrame.

    Some algos can add an additional `"EMERGENCY_TYPE"` column to the provided DataFrame,
    providing a more detailled classification.

    Parameters
    ----------
    care_site: DataFrame
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


    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 to 2 added columns corresponding to the following concepts:

        - `"IS_EMERGENCY"`
        - `"EMERGENCY_TYPE"` (if using algo `"from_mapping"`)

    """
    if algo == "from_regex_on_parent_UF":
        return from_regex_on_parent_UF(care_site)
    elif algo == "from_regex_on_care_site_description":
        return from_regex_on_care_site_description(care_site)
    elif algo.startswith("from_mapping"):
        return from_mapping(care_site, version=versionize(algo))


@concept_checker(concepts=["IS_EMERGENCY", "EMERGENCY_TYPE"])
def from_mapping(
    care_site: DataFrame,
    version: Optional[str] = None,
) -> DataFrame:
    """This algo uses a labelled list of 201 emergency care sites.

    Those care sites were extracted and verified by Ariel COHEN,
    Judith LEBLANC, and an ER doctor validated them.

    Those emergency care sites are further divised into different categories,
    as defined in the concept 'EMERGENCY_TYPE'.
    The different categories are:

    - Urgences spécialisées
    - UHCD + Post-urgences
    - Urgences pédiatriques
    - Urgences générales adulte
    - Consultation urgences
    - SAMU / SMUR

    See the dataset [here](/datasets/care-site-emergency)

    Parameters
    ----------
    care_site: DataFrame
        Should at least contains the `care_site_source_value` column
    version: Optional[str]
        Optional version string for the mapping

    Returns
    -------
    care_site: DataFrame
        Dataframe with 2 added columns corresponding to the following concepts:

        - `"IS_EMERGENCY"`
        - `"EMERGENCY_TYPE"`

    """

    function_name = "get_care_site_emergency_mapping"
    if version is not None:
        function_name += f".{version}"

    mapping = registry.get("data", function_name=function_name)()

    # Getting the right framework
    fw = framework.get_framework(care_site)
    mapping = framework.to(fw, mapping)

    care_site = care_site.merge(
        mapping,
        how="left",
        on="care_site_source_value",
    )

    care_site["IS_EMERGENCY"] = care_site["EMERGENCY_TYPE"].notna()

    return care_site


# @concept_checker(concepts=["IS_EMERGENCY"])
def from_regex_on_care_site_description(care_site: DataFrame) -> DataFrame:
    """Use regular expressions on `care_site_name` to decide if it an emergency care site.

    This relies on [this function][eds_scikit.structures.attributes.add_care_site_attributes].
    The regular expression used to detect emergency status is `r"\bURG|\bSAU\b|\bUHCDb\b|\bZHTCD\b"`

    Parameters
    ----------
    care_site: DataFrame
        Should at least contains the `care_site_name` column

    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 added column corresponding to the following concept:

        - `"IS_EMERGENCY"`

    """
    return attributes.add_care_site_attributes(
        care_site, only_attributes=["IS_EMERGENCY"]
    )


@concept_checker(concepts=["IS_EMERGENCY"])
def from_regex_on_parent_UF(care_site: DataFrame) -> DataFrame:
    """Use regular expressions on parent UF (Unité Fonctionnelle) to classify emergency care site.

    This relies on [this function][eds_scikit.structures.attributes.get_parent_attributes].
    The regular expression used to detect emergency status is `r"\bURG|\bSAU\b|\bUHCD\b|\bZHTCD\b"`

    Parameters
    ----------
    care_site: DataFrame
        Should at least contains the `care_site_name` column

    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 added column corresponding to the following concept:

        - 'IS_EMERGENCY'
    """
    return attributes.get_parent_attributes(
        care_site,
        only_attributes=["IS_EMERGENCY"],
        parent_type="Unité Fonctionnelle (UF)",
    )
