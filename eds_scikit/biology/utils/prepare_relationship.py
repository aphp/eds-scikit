from typing import Dict, List, Tuple

import databricks.koalas as ks
import pandas as pd

from eds_scikit.biology.utils.check_data import (
    check_data_and_select_columns_relationship,
)
from eds_scikit.biology.utils.process_concepts import ConceptsSet
from eds_scikit.io.settings import measurement_config
from eds_scikit.utils.framework import get_framework, to
from eds_scikit.utils.typing import Data, DataFrame

mapping = measurement_config["mapping"]
source_terminologies = measurement_config["source_terminologies"]


def prepare_relationship_table(
    data: Data,
    source_terminologies: Dict[str, str],
    mapping: List[Tuple[str, str, str]],
) -> ks.DataFrame:  # ks or pandas
    """

    Create easy-to-use relationship table based on given terminologies and mapping between them.

    Parameters
    ----------
    data : Data
        Instantiated [``HiveData``][edsteva.io.hive.HiveData], [``PostgresData``][edsteva.io.postgres.PostgresData] or [``LocalData``][edsteva.io.files.LocalData]
    source_terminologies : Dict[str, str]
        Dictionary of concepts terminologies with their associated regex.
    **EXAMPLE**: `{'source_concept'  : r'src_.{0, 10}_lab', 'standard_concept' : r'std_concept'}`
    mapping : List[Tuple[str, str, str]]
        Ordered mapping of terminologies based on concept_relationship table
    **EXAMPLE**: `[("source_concept", "standard_concept", "Maps to")]`

    Output
    -------
    |   source_concept_id | source_concept_name   | source_concept_code   |   standard_concept_id     | standard_concept_name     | standard_concept_code       |
    |--------------------:|:---------------------:|:---------------------:|:-------------------------:|:-------------------------:|:---------------------------:|
    |                   3 | xxxxxxxxxxxx          | CX1                   |                         4 | xxxxxxxxxxxx              | A1                          |
    |                   9 | xxxxxxxxxxxx          | ZY2                   |                         5 | xxxxxxxxxxxx              | A2                          |
    |                   9 | xxxxxxxxxxxx          | B3F                   |                        47 | xxxxxxxxxxxx              | D3                          |
    |                   7 | xxxxxxxxxxxx          | T32                   |                         4 | xxxxxxxxxxxx              | F82                         |
    |                   5 | xxxxxxxxxxxx          | S23                   |                         1 | xxxxxxxxxxxx              | A432                        |


    """

    concept, concept_relationship = check_data_and_select_columns_relationship(data)

    concept_by_terminology = {}
    for terminology, regex in source_terminologies.items():
        concept_by_terminology[terminology] = (
            concept[concept.vocabulary_id.str.contains(regex)]
            .rename(
                columns={
                    "concept_id": "{}_concept_id".format(terminology),
                    "concept_name": "{}_concept_name".format(terminology),
                    "concept_code": "{}_concept_code".format(terminology),
                }
            )
            .drop(columns="vocabulary_id")
        )
    root_terminology = mapping[0][0]
    relationship_table = concept_by_terminology[root_terminology]
    # Look over all predefined structured mapping
    for source, target, relationship_id in mapping:
        relationship = concept_relationship.rename(
            columns={
                "concept_id_1": "{}_concept_id".format(source),
                "concept_id_2": "{}_concept_id".format(target),
            }
        )[concept_relationship.relationship_id == relationship_id].drop(
            columns="relationship_id"
        )
        relationship = relationship.merge(
            concept_by_terminology[target], on="{}_concept_id".format(target)
        )
        relationship_table = relationship_table.merge(
            relationship, on="{}_concept_id".format(source), how="left"
        )

    relationship_table = relationship_table.fillna("Unknown")

    return relationship_table


def filter_concept_sets_relationship_table(relationship_table, concept_sets):
    """Filter relationship table using concept_sets concept codes.

    Parameters
    ----------
    relationship_table : DataFrame
        Biology relationship table
    concept_sets : List[ConceptsSet]
        List of concepts-sets to select

    Returns
    -------
    DataFrame
        Filtered biology relationship table
    """

    framework = get_framework(relationship_table)

    concept_sets_tables = pd.DataFrame({})
    for concept_set in concept_sets:
        concept_set_table = concept_set.get_concept_codes_table()
        concept_sets_tables = pd.concat(
            (concept_set_table, concept_sets_tables), axis=0
        )
    terminologies = concept_sets_tables.terminology.unique()
    concept_sets_tables = to(framework, concept_sets_tables)
    filtered_terminology_table = framework.DataFrame({})
    for terminology in terminologies:
        if f"{terminology}_concept_code" in relationship_table.columns:
            filtered_terminology_table_ = concept_sets_tables[
                concept_sets_tables.terminology == terminology
            ].merge(
                relationship_table,
                on=f"{terminology}_concept_code",
                how="left",
                suffixes=("_x", ""),
            )
            filtered_terminology_table_ = filtered_terminology_table_[
                [
                    column
                    for column in filtered_terminology_table_.columns
                    if not ("_x" in column)
                ]
            ]
            filtered_terminology_table = framework.concat(
                (filtered_terminology_table_, filtered_terminology_table)
            ).drop_duplicates()

    return filtered_terminology_table


def concept_sets_columns(
    relationship_table: DataFrame,
    concept_sets: List[ConceptsSet],
    extra_terminologies: List = List[str],
) -> List[str]:
    """Filter relationship_table keeping concepts_sets terminologies columns.

    Parameters
    ----------
    relationship_table : DataFrame
    concept_sets : List[ConceptsSet]
    extra_terminologies : List, optional

    Returns
    -------
    List[str]
    """
    keep_terminologies = extra_terminologies
    for concept_set in concept_sets:
        keep_terminologies += concept_set.concept_codes.keys()

    keep_columns = []
    for col in relationship_table.columns:
        if any([terminology in col for terminology in keep_terminologies]):
            keep_columns.append(col)

    return keep_columns


def prepare_biology_relationship_table(
    data: Data,
    concept_sets: List[ConceptsSet] = None,
    get_all_terminologies: bool = True,
) -> DataFrame:
    """Prepare biology relationship table to map concept codes based on settings.source_terminologies and settings.mapping.

    Parameters
    ----------
    data : Data
        Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    concept_sets : List[ConceptsSet], optional
        List of concepts-sets to select
    get_all_terminologies : bool, optional
        If True, all terminologies from settings terminologies will be added, by default True
    Returns
    -------
    DataFrame
        biology_relationship_table to be merged with measurement
    """
    if concept_sets is None and not get_all_terminologies:
        raise Exception(
            "get_all_terminologies must be True if no concept_sets provided."
        )

    biology_relationship_table = prepare_relationship_table(
        data, source_terminologies, mapping
    )
    biology_relationship_table = (
        filter_concept_sets_relationship_table(biology_relationship_table, concept_sets)
        if concept_sets
        else biology_relationship_table
    )

    keep_columns = (
        biology_relationship_table.columns
        if get_all_terminologies
        else concept_sets_columns(
            biology_relationship_table,
            concept_sets,
            [mapping[0][0], "concept_set"],
        )
    )
    biology_relationship_table = biology_relationship_table[keep_columns]

    return biology_relationship_table
