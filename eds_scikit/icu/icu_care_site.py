# -*- coding: utf-8 -*-
from typing import Union

from eds_scikit.structures import attributes
from eds_scikit.utils.checks import algo_checker, concept_checker
from eds_scikit.utils.typing import DataFrame

ALGOS = [
    "from_authorisation_type",
    "from_regex_on_care_site_description",
]


@algo_checker(algos=ALGOS)
def tag_icu_care_site(
    care_site: DataFrame,
    algo: str = "from_mapping",
) -> DataFrame:
    """Tag care sites that correspond to **ICU units**.

    The tagging is done by adding a `"IS_ICU"` column to the provided DataFrame.

    Parameters
    ----------
    care_site: DataFrame
    algo: str
        Possible values are:

        - [`"from_authorisation_type"`][eds_scikit.icu.icu_care_site.from_authorisation_type]
        - [`"from_regex_on_care_site_description"`][eds_scikit.icu.icu_care_site.from_regex_on_care_site_description]

    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 added column corresponding to the following concept:

        - `"IS_ICU"`
    """
    if algo == "from_authorisation_type":
        return from_authorisation_type(care_site)
    elif algo == "from_regex_on_care_site_description":
        return from_regex_on_care_site_description(care_site)


@concept_checker(concepts=["IS_ICU"])
def from_authorisation_type(care_site: DataFrame) -> DataFrame:
    """This algo uses the `care_site.place_of_service_source_value` columns
    to retrieve Intensive Care Units.

    The following values are used to tag a care site as ICU:

    - `"REA PED"`
    - `"REA"`
    - `"REA ADULTE"`
    - `"REA NEONAT"`
    - `"USI"`
    - `"USI ADULTE"`
    - `"USI NEONAT"`
    - `"SC PED"`
    - `"SC"`
    - `"SC ADULTE"`

    Parameters
    ----------
    care_site: DataFrame
        Should at least contains the `place_of_service_source_value` column

    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 added column corresponding to the following concepts:

        - `"IS_ICU"`

    """

    icu_units = set(
        [
            "REA PED",
            "USI",
            "SC PED",
            "SC",
            "REA",
            "SC ADULTE",
            "USI ADULTE",
            "REA ADULTE",
            "USI NEONAT",
            "REA NEONAT",
        ]
    )

    care_site["IS_ICU"] = care_site["place_of_service_source_value"].isin(icu_units)

    return care_site


# @concept_checker(concepts=["IS_ICU"])
def from_regex_on_care_site_description(
    care_site: DataFrame, subset_care_site_type_source_value: Union[list, set] = {"UDS"}
) -> DataFrame:
    """Use regular expressions on `care_site_name` to decide if it an ICU care site.

    This relies on [this function][eds_scikit.structures.attributes.add_care_site_attributes].
    The regular expression used to detect ICU is
    `r"\bUSI|\bREA[N\s]|\bREA\b|\bUSC\b|SOINS.*INTENSIF|SURV.{0,15}CONT|\bSI\b|\bSC\b"`.

    !!! aphp "Keeping only 'UDS'"
         At AP-HP, all ICU are **UDS** (*Unité De Soins*).
         Therefore, this function filters care sites by default to only keep UDS.

    Parameters
    ----------
    care_site: DataFrame
        Should at least contains the `care_site_name` and `care_site_type_source_value` columns
    subset_care_site_type_source_value: Union[list, set]
        Acceptable values for `care_site_type_source_value`

    Returns
    -------
    care_site: DataFrame
        Dataframe with 1 added column corresponding to the following concept:

        - `"IS_ICU"`

    """  # noqa

    care_site = attributes.add_care_site_attributes(
        care_site, only_attributes=["IS_ICU"]
    )

    # Filtering matches

    if subset_care_site_type_source_value:
        care_site["IS_ICU"] = care_site["IS_ICU"] & (
            care_site.care_site_type_source_value.isin(
                subset_care_site_type_source_value
            )
        )

    return care_site
