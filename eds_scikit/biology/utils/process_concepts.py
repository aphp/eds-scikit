import ast
import re
from functools import reduce
from typing import List, Union

import pandas as pd
from loguru import logger

from eds_scikit import datasets
from eds_scikit.io import settings
from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.framework import get_framework, to
from eds_scikit.utils.typing import DataFrame

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


class ConceptsSet:
    """Class defining the concepts-sets with 2 attributes:

    - ``name``: the name of the concepts-set
    - ``concept_codes`` : the list of concepts codes included in the concepts-set
    """

    def __init__(self, name: str, concept_codes: List[str] = None):
        self.name = name
        if concept_codes is None:
            self.concept_codes = fetch_concept_codes_from_name(name)
        else:
            self.concept_codes = concept_codes

    def add_concept_codes(self, concept_codes: Union[str, List[str]]):
        if isinstance(concept_codes, str):
            if concept_codes not in self.concept_codes:
                self.concept_codes.append(concept_codes)
        elif isinstance(concept_codes, list):
            for concept_code in concept_codes:
                if concept_code not in self.concept_codes:
                    self.concept_codes.append(concept_code)
        else:
            logger.error("concept_codes must be string or list")
            raise TypeError

    def remove_concept_codes(self, concept_codes: Union[str, List[str]]):
        if isinstance(concept_codes, str):
            if concept_codes in self.concept_codes:
                self.concept_codes.remove(concept_codes)
                logger.info("concept_code {} has been deleted", concept_codes)
        elif isinstance(concept_codes, list):
            for concept_code in concept_codes:
                if concept_code in self.concept_codes:
                    self.concept_codes.remove(concept_code)
                    logger.info("concept_code {} has been deleted", concept_code)
        else:
            logger.error("concept_codes must be string or list")
            raise TypeError


def fetch_concept_codes_from_name(
    concepts_set_name: str, concepts_sets_table_name: str = "default_concepts_sets"
):
    default_concepts_sets = getattr(datasets, concepts_sets_table_name).set_index(
        "concepts_set_name"
    )
    if concepts_set_name in default_concepts_sets.index:
        standard_concepts = []
        for column in default_concepts_sets.columns:
            terminology_standard_concepts = ast.literal_eval(
                default_concepts_sets.loc[concepts_set_name][column]
            )
            standard_concepts.extend(terminology_standard_concepts)
        return standard_concepts
    else:
        logger.warning(
            "The concepts-set {} has not been found in the default concepts-set table.",
            concepts_set_name,
        )
        return None


def fetch_all_concepts_set(
    concepts_sets_table_name: str = "default_concepts_sets",
) -> List[ConceptsSet]:
    """Returns a list of all the concepts-sets of the chosen tables. By default, the table is [here][concepts-sets].

    Parameters
    ----------
    concepts_sets_table_name : str, optional
        Name of the table to extract concepts-sets from

    Returns
    -------
    List[ConceptsSet]
        The list of all concepts-sets in the selected table
    """
    concepts_sets = []
    default_concepts_sets = getattr(datasets, concepts_sets_table_name)
    for concepts_set_name in default_concepts_sets.concepts_set_name:
        concepts_sets.append(ConceptsSet(concepts_set_name))
    logger.info("Fetch all concepts-sets from table {}", concepts_sets_table_name)
    return concepts_sets


def get_concept_src_to_std(
    concept: DataFrame,
    concept_relationship: DataFrame,
    concepts_sets: List[ConceptsSet],
    standard_concept_regex: dict = default_standard_concept_regex,
    standard_terminologies: List[str] = default_standard_terminologies,
) -> pd.DataFrame:
    """Process ``Concept`` and ``Concept Relationship`` tables to obtain a wide DataFrame that gives for all concepts-sets the source code along with the standard concepts codes.

    Parameters
    ----------
    concept : DataFrame
        [Concept](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept) OMOP table
    concept_relationship : DataFrame
        [Concept Relationship](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept_relationship) OMOP table
    concepts_sets : List[ConceptsSet]
        List of concepts-sets to select
    standard_concept_regex : dict, optional
        **EXAMPLE**: `{"LOINC": "[0-9]{2,5}[-][0-9]","AnaBio": "[A-Z][0-9]{4}"}`
    standard_terminologies : List[str], optional
        **EXAMPLE**: `["LOINC", "AnaBio"]`


    Returns
    -------
    pd.DataFrame
        DataFrame with a column for the source concepts codes and columns for the selected standard concepts codes"""
    check_columns(
        concept,
        required_columns=[
            "concept_id",
            "concept_code",
            "concept_name",
            "vocabulary_id",
        ],
        df_name="concept",
    )
    check_columns(
        concept_relationship,
        required_columns=[
            "concept_id_1",
            "concept_id_2",
            "relationship_id",
        ],
        df_name="concept_relationship",
    )

    # Get desired concepts
    filtered_concepts = _filter_concepts(concept, concepts_sets, standard_concept_regex)

    # Get only parent concepts
    concept_relationship = concept_relationship[
        concept_relationship.relationship_id.isin(["Maps to", "Mapped from"])
    ]
    concept_relationship = concept_relationship.drop(columns="relationship_id")

    # Get the complete standard concept id list
    original_concpet_id = filtered_concepts.merge(
        concept_relationship, left_on="concept_id", right_on="concept_id_2", how="inner"
    )[["concept_id_1", "concepts_set"]]
    original_concpet_id.drop_duplicates("concept_id_1", inplace=True)
    related_concept_id = concept_relationship.merge(
        original_concpet_id, on="concept_id_1", how="inner"
    )
    long_src_to_std = concept.merge(
        related_concept_id, left_on="concept_id", right_on="concept_id_2", how="inner"
    )
    long_src_to_std = long_src_to_std.drop(columns=["concept_id", "concept_id_2"])
    long_src_to_std.rename(
        columns={
            "concept_id_1": "source_concept_id",
        },
        inplace=True,
    )
    long_src_to_std = to("pandas", long_src_to_std)

    # Convert long src_std to a wide src_std
    related_terminologies_concept_id = []
    for terminology in standard_terminologies:
        # Filter each terminology concept id
        terminology_filter = long_src_to_std.vocabulary_id.str.contains(
            terminology, case=False, regex=False
        )
        related_terminology_concept_id = long_src_to_std[terminology_filter].copy()
        related_terminology_concept_id.rename(
            columns={
                "concept_code": "{}_concept_code".format(terminology),
                "concept_name": "{}_concept_name".format(terminology),
                "vocabulary_id": "{}_vocabulary_id".format(terminology),
            },
            inplace=True,
        )
        related_terminology_concept_id.drop_duplicates(
            ["source_concept_id", "{}_concept_code".format(terminology)], inplace=True
        )
        related_terminologies_concept_id.append(related_terminology_concept_id)

    # Merge all terminologies
    if len(related_terminologies_concept_id) >= 2:
        wide_src_to_std = reduce(
            lambda left, right: left.merge(
                right, on=["source_concept_id", "concepts_set"], how="outer"
            ),
            related_terminologies_concept_id,
        )
    elif len(related_terminologies_concept_id) == 1:
        wide_src_to_std = related_terminologies_concept_id[0]

    else:
        return long_src_to_std[["source_concept_id"]]

    if all(
        terminology in standard_terminologies
        for terminology in default_standard_concept_regex
    ):
        # Get LOINC NAME and code from ITM
        wide_src_to_std = _override_name_code_with_itm(wide_src_to_std)

    wide_src_to_std = _rename_duplicate_code_with_different_names(wide_src_to_std)
    wide_src_to_std.fillna("Non renseigné", inplace=True)

    return wide_src_to_std


def _filter_concepts(
    concept: DataFrame,
    concepts_sets: List[ConceptsSet],
    standard_concept_regex: dict = default_standard_concept_regex,
):
    check_columns(
        df=concept, required_columns=["concept_code", "concept_name"], df_name="concept"
    )

    if isinstance(concepts_sets, ConceptsSet):
        concepts_sets = [concepts_sets]

    filtered_concepts_tables = []
    for concepts_set in concepts_sets:

        concepts_set_name = concepts_set.name
        concepts_codes = concepts_set.concept_codes

        match, unmatched_concepts = _check_regex(concepts_codes, standard_concept_regex)

        if match:
            filtered_concepts_table = concept[
                concept.concept_code.isin(concepts_codes)
            ].copy()
            filtered_concepts_table["concepts_set"] = concepts_set_name
            if filtered_concepts_table.empty:
                logger.error(
                    "None of the code from {} has been found in the Concept table.",
                    concepts_set_name,
                )
            filtered_concepts_tables.append(filtered_concepts_table)

        else:
            logger.warning(
                "The following codes {} from the concept set {} have not matched the terminology regex {}.",
                unmatched_concepts,
                concepts_set_name,
                standard_concept_regex,
            )

            if len(unmatched_concepts) < len(concepts_codes):
                concepts_codes = [
                    concept
                    for concept in concepts_codes
                    if concept not in unmatched_concepts
                ]

                filtered_concepts_table = concept[
                    concept.concept_code.isin(concepts_codes)
                ].copy()
                filtered_concepts_table["concepts_set"] = concepts_set_name
                if filtered_concepts_table.empty:
                    logger.error(
                        "None of the code has been found in the Concept table."
                    )
                filtered_concepts_tables.append(filtered_concepts_table)

            elif all(type(item) is str for item in concepts_codes):
                logger.warning(
                    "As all the concepts have not matched the regex, it will filter directly on the string. This is not encouraged."
                )
                filtered_concepts_table = concept[
                    concept.concept_name.str.contains(
                        _regify(concepts_codes), case=False, regex=True
                    )
                ].copy()
                filtered_concepts_table["concepts_set"] = concepts_set_name
                if filtered_concepts_table.empty:
                    logger.error(
                        "None of the code has been found in the Concept table."
                    )
                filtered_concepts_tables.append(filtered_concepts_table)
            else:
                logger.error(
                    "Concepts codes must be string, concepts-set {} has not been processed",
                    concepts_set_name,
                )
    return get_framework(filtered_concepts_tables[0]).concat(filtered_concepts_tables)


def _regify(words, base=str(r"^{}"), expr=str("(?=.*{})")):
    return base.format("".join(expr.format(w) for w in words))


def _check_regex(
    concepts_codes: List[str],
    standard_concept_regex: dict = default_standard_concept_regex,
):
    unmatched_concepts = []
    for concept in concepts_codes:
        match = False
        for regex in standard_concept_regex.values():
            if bool(re.match(regex, concept)):
                match = True
        if not match:
            unmatched_concepts.append(concept)
    if unmatched_concepts:
        return (False, unmatched_concepts)
    else:
        return (True, unmatched_concepts)


def _override_name_code_with_itm(wide_src_to_std):
    logger.info(
        "ITM mapper has been identified in your data and will be prioritized for concept names."
    )
    # Get LOINC NAME and code from ITM
    # Get ITM LOINC code with names
    loinc_itm = wide_src_to_std[
        wide_src_to_std.LOINC_vocabulary_id == "APHP - ITM - LOINC"
    ][["AnaBio_concept_code", "LOINC_concept_code", "LOINC_concept_name"]].rename(
        columns={
            "LOINC_concept_code": "LOINC_ITM_conept_code",
            "LOINC_concept_name": "LOINC_ITM_conept_name",
        }
    )
    loinc_itm.drop_duplicates(["AnaBio_concept_code"], inplace=True)

    wide_src_to_std = wide_src_to_std.merge(
        loinc_itm,
        on="AnaBio_concept_code",
        how="left",
    )

    wide_src_to_std["LOINC_concept_code"] = wide_src_to_std["LOINC_concept_code"].where(
        (wide_src_to_std["LOINC_ITM_conept_code"].isna()),
        wide_src_to_std["LOINC_ITM_conept_code"],
    )

    wide_src_to_std["LOINC_vocabulary_id"] = wide_src_to_std[
        "LOINC_vocabulary_id"
    ].where((wide_src_to_std["LOINC_ITM_conept_code"].isna()), "APHP - ITM - LOINC")

    wide_src_to_std["LOINC_concept_name"] = wide_src_to_std["LOINC_concept_name"].where(
        (wide_src_to_std["LOINC_ITM_conept_name"].isna()),
        wide_src_to_std["LOINC_ITM_conept_name"],
    )

    wide_src_to_std = wide_src_to_std.drop(
        columns=["LOINC_ITM_conept_code", "LOINC_ITM_conept_name"]
    )
    return wide_src_to_std


def _rename_duplicate_code_with_different_names(wide_src_to_std):
    concept_code_cols = [
        column_name
        for column_name in wide_src_to_std.columns
        if "concept_code" in column_name
    ]
    concept_name_cols = [
        column_name
        for column_name in wide_src_to_std.columns
        if "concept_name" in column_name
    ]
    concepts_info = wide_src_to_std[concept_code_cols + concept_name_cols].copy()
    concepts_info.drop_duplicates(concept_code_cols, inplace=True)

    wide_src_to_std = wide_src_to_std.drop(columns=concept_name_cols)
    wide_src_to_std = wide_src_to_std.merge(
        concepts_info,
        on=concept_code_cols,
        how="left",
    )

    return wide_src_to_std
