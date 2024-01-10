import databricks.koalas as ks
import re
from eds_scikit.io import settings
from eds_scikit.biology.utils.check_data import check_data_and_select_columns_relationship
from eds_scikit.utils.framework import get_framework, to
import pandas as pd

def select_mapping(
    mapping,
    sources=None,
    terminologies=None,
):
    #if some terminologies not in mapping : fail
    mapping_filtered = []
    
    for m in mapping:
        keep_m = True
        if sources:
            keep_m = any([source in m for source in sources]) and keep_m
        if terminologies:
            keep_m = any([(terminology in m[0]) or (terminology in m[1]) for terminology in terminologies]) and keep_m
        if keep_m:
            mapping_filtered.append(m)
    
    return mapping_filtered

def prepare_relationship_table(
    data,
    source_terminologies,
    mapping,
) -> ks.DataFrame: #ks or pandas
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
    
    framework = get_framework(relationship_table)
    
    concept_sets_tables = pd.DataFrame({})
    for concept_set in concept_sets:
        concept_set_table = concept_set.get_concept_codes_table()
        concept_sets_tables = pd.concat((concept_set_table, concept_sets_tables), axis=0)
    terminologies = concept_sets_tables.terminology.unique()
    concept_sets_tables = to(framework, concept_sets_tables)
    filtered_terminology_table = framework.DataFrame({})
    for terminology in terminologies:
        filtered_terminology_table = concept_sets_tables[concept_sets_tables.terminology == terminology].merge(relationship_table, on=f"{terminology}_concept_code", how="left", suffixes=("_x", ""))
        filtered_terminology_table = filtered_terminology_table[[column for column in filtered_terminology_table.columns if not("_x" in column)]]
        
    return filtered_terminology_table

def prepare_biology_relationship_table(data, concept_sets):
        
    biology_relationship_table = prepare_relationship_table(data, settings.source_terminologies, settings.mapping)
    biology_relationship_table = filter_concept_sets_relationship_table(biology_relationship_table, concept_sets)
    
    return biology_relationship_table