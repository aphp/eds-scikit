from typing import Iterable, List, Optional

import pandas as pd

from eds_scikit.resources import registry
from eds_scikit.utils import framework
from eds_scikit.utils.typing import DataFrame

from . import description

ATTRIBUTE_REGEX_PATTERNS = [
    {
        "attribute": "IS_EMERGENCY",
        "pattern": r"\bURG|\bSAU\b|\bUHCD\b|\bZHTCD\b",
        "true_examples": ["URG", "URGENCES", "SAU"],
        "false_examples": ["CHIRURGIE"],
    },
    {
        "attribute": "IS_ICU",
        "pattern": r"\bUSI|\bREA[N\s]|\bREA\b|\bUSC\b|SOINS.*INTENSIF|SURV.{0,15}CONT|\bSI\b|\bSC\b",
        "true_examples": ["REA", "REA NEURO", "REANIMATION"],
        "false_examples": ["CARREAU"],
    },
]
"""Default argument of :py:func:`~eds_scikit.structures.attributes.add_care_site_attributes`.

:meta private:

Examples
--------
::

    ATTRIBUTE_REGEX_PATTERNS = [
        {
            # required elements: name of attribute and pattern of regular expression
            "attribute": "IS_EMERGENCY",
            "pattern": r"\bURG|\bSAU\b|\bUHCD\b|\bZHTCD\b",

            # optional elements: list of test strings to validate the regular expression
            "true_examples": ["URG", "URGENCES", "SAU"],
            "false_examples": ["CHIRURGIE"],
        },
        ...
    ]

"""

possible_concepts = [item["attribute"] for item in ATTRIBUTE_REGEX_PATTERNS]


def add_care_site_attributes(
    care_site: DataFrame,
    only_attributes: Optional[List[str]] = None,
    attribute_regex_patterns: Optional[List[str]] = None,
) -> DataFrame:
    """Add boolean attributes as columns to care_site dataframe.

    This algo applies simple regular expressions to the ``care_site_name``
    in order to compute boolean attributes of the care site.
    Implemented attributes are:

    - ``IS_EMERGENCY``
    - ``IS_ICU``

    In order to make the detection of attributes more robust, the
    column ``care_site_name`` is first transformed to a ``DESCRIPTION``.
    This is done by :py:func:`~eds_scikit.structures.description.add_care_site_description`.

    Parameters
    ----------
    care_site : DataFrame
    only_attributes : list of str
        if only a subset of all possible attributes should be computed
    attribute_regex_patterns : list (None)
        If ``None``, the default value is :py:data:`~eds_scikit.structures.attributes.ATTRIBUTE_REGEX_PATTERNS`

    Returns
    -------
    care_site: DataFrame
        same as input with additional columns corresponding to boolean attributes.
        the column ``DESCRIPTION`` is also added : it contains of cleaner version of ``care_site_name``.


    Examples
    --------
    >>> care_site.head(2)
    care_site_id, care_site_name
    21, HOSP ACCUEIL URG PED (UF)
    22, HOSP CHIRURGIE DIGESTIVE
    23, HOSP PEDIATRIE GEN ET SAU
    >>> care_site = add_care_site_attributes(care_site, only_attributes=["IS_EMERGENCY"])
    >>> care_site.head(2)
    care_site_id, care_site_name, DESCRIPTION, IS_EMERGENCY
    21, HOSP ACCUEIL URG PED (UF),ACCUEIL URG PED,True
    22, HOSP CHIRURGIE DIGESTIVE,CHIRURGIE DIGESTIVE,False
    23, HOSP PEDIATRIE GEN ET SAU,PEDIATRIE GEN ET SAU,True

    Specifying custom regular expressions. It is a good idea to provide true and false examples for
    each attribute. These examples will be tested against the provided regular expressions.

    >>> my_attributes = [
        {
            "attribute": "IS_EMERGENCY",
            "pattern": r"\bURG|\bSAU\b|\bUHCD\b|\bZHTCD\b",
            "true_examples": ["URG", "URGENCES", "SAU"],
            "false_examples": ["CHIRURGIE"],
        },
        {
            "attribute": "IS_ICU",
            "pattern": r"\bREA\b|\bREANI",
            "true_examples": ["REA", "REA NEURO", "REANIMATION"],
            "false_examples": ["CARREAU"],
        },
    ]
    >>> care_site = add_care_site_attributes(care_site, attribute_regex_patterns=my_attributes)

    """
    # validate arguments
    if attribute_regex_patterns is None:
        attribute_regex_patterns = ATTRIBUTE_REGEX_PATTERNS

    if only_attributes:
        impossible = set(only_attributes) - set(possible_concepts)
        if impossible:
            raise ValueError(f"Unknown concepts: {impossible}")
        attribute_regex_patterns = [
            item
            for item in attribute_regex_patterns
            if item["attribute"] in only_attributes
        ]

    validate_attribute_regex_patterns(attribute_regex_patterns)

    if "DESCRIPTION" not in care_site.columns:
        care_site = description.add_care_site_description(care_site)

    # apply algo
    for item in attribute_regex_patterns:
        new_column = {
            item["attribute"]: care_site["DESCRIPTION"].str.contains(
                item["pattern"], regex=True
            )
        }
        care_site = care_site.assign(**new_column)

    if only_attributes:
        care_site = care_site.drop(["DESCRIPTION"], axis="columns")

    return care_site


def validate_attribute_regex_patterns(patterns: Iterable[str]) -> None:
    for item in patterns:
        true_examples = item.get("true_examples", [])
        false_examples = item.get("false_examples", [])
        if true_examples:
            result = pd.Series(true_examples).str.contains(item["pattern"], regex=True)
            assert (
                result.all()
            ), f"Found examples that should be True but aren't: {item['attribute']}"
        if false_examples:
            # notice the ~ NOT
            result = ~pd.Series(false_examples).str.contains(
                item["pattern"], regex=True
            )
            assert (
                result.all()
            ), f"Found examples that should be True but aren't: {item['attribute']}"


def get_parent_attributes(
    care_site: DataFrame,
    only_attributes: Optional[List[str]] = None,
    version: Optional[str] = None,
    parent_type: str = "Unité Fonctionnelle (UF)",
) -> DataFrame:
    """Get all known attributes from parent care sites and propagates them to each child care site

    Parameters
    ----------
    care_site: DataFrame
        required columns: ``["care_site_id", "care_site_type_source_value", "care_site_name"]``
    only_attributes : list of str
        same as :py:func:`~eds_scikit.structures.attributes.add_care_site_attributes`
    version: Optional[str]
        Optional version string for the care site hierarchy
    parent_type: str
        Type of care site to consider as parent, by default "Unité Fonctionnelle (UF)".
        Corresponds to the `"care_site_type_source_value"` column

    Returns
    --------
    care_site_attributes: DataFrame
        same index as input care_site. columns: care_site, is_emergency


    Warnings
    --------
    This algo requires that the `care_site` dataframe contains
    the parent care sites as well as the care sites
    that you want to tag.

    Examples
    --------
    >>> attributes = get_parent_attributes(care_site,
                                           only_attributes=["IS_EMERGENCY"],
                                           parent_type="Unité Fonctionnelle (UF)")
    >>> attributes.head()
        care_site_id, care_site_name, care_site_type_source_value, IS_EMERGENCY
        92829  , ... ,     False
        29820  , ... ,     True

    """

    function_name = "get_care_site_hierarchy"
    if version is not None:
        function_name += f".{version}"
    hierarchy = registry.get("data", function_name=function_name)()

    fw = framework.get_framework(care_site)
    hierarchy = framework.to(fw, hierarchy)

    # STEP 1: get attributes of parent
    parent_attributes = care_site.loc[
        care_site["care_site_type_source_value"] == parent_type,
        ["care_site_id", "care_site_name"],
    ]
    parent_attributes = add_care_site_attributes(
        parent_attributes, only_attributes=only_attributes
    )
    boolean_columns = [
        col for (col, dtype) in parent_attributes.dtypes.iteritems() if dtype == "bool"
    ]

    parent_attributes = parent_attributes.drop(
        ["care_site_name"], axis="columns"
    ).rename(columns={"care_site_id": "parent_id"})

    # STEP 2: propagate attributes from parent to all children
    hierarchy = hierarchy.loc[:, ["care_site_id", parent_type]].rename(
        columns={parent_type: "parent_id"}
    )
    children_attributes = hierarchy.merge(
        parent_attributes, how="left", on="parent_id"
    ).drop(["parent_id"], axis="columns")

    # STEP 3 : merge to input dataframe
    old_columns = care_site.columns
    care_site = care_site.merge(children_attributes, how="left", on="care_site_id")
    for col in care_site.columns:
        if col in boolean_columns and col not in old_columns:
            care_site[col] = care_site[col].fillna(value=False)

    return care_site

    # NOTE: this is how to return a single column that contains
    # EXACTLY the same index as the input dataframe.
    # For instance koalas requires the index name to be the same
    # for this operation to be valid:
    # >>> df["new_column"] = compute_column(df)

    # attributes = (
    #     care_site.loc[:, ["care_site_id"]]
    #     .reset_index()
    #     .merge(
    #         # drop_duplicates to ensure we keep same size as input
    #         children_attributes.drop_duplicates(subset=["care_site_id"]),
    #         how="left",
    #         on="care_site_id",
    #     )
    #     .fillna(value=False)
    #     # a merge "forgets" the index, we want to output the same as input
    #     .set_index("index")
    # )
    # attributes.index.name = care_site.index.name
