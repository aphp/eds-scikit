import pandas as pd
from eds_scikit.utils.checks import check_columns, check_tables
from eds_scikit.utils.framework import get_framework, to

def prepare_biology_relationship(
    data,
    source_terminologies,
    mapping
) -> pd.DataFrame:
    """Computes biology relationship table

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

    check_tables(data=data, required_tables=["concept", "concept_relationship"])
    concept_columns = [
        "concept_id",
        "concept_name",
        "concept_code",
        "vocabulary_id",
    ]

    concept_relationship_columns = [
        "concept_id_1",
        "concept_id_2",
        "relationship_id",
    ]
    check_columns(
        data.concept,
        required_columns=concept_columns,
        df_name="concept",
    )

    check_columns(
        data.concept_relationship,
        required_columns=concept_relationship_columns,
        df_name="concept_relationship",
    )
    
    concept = data.concept[concept_columns]
    concept_relationship = data.concept_relationship[concept_relationship_columns]
    
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
    biology_relationship = concept_by_terminology[root_terminology]
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
        biology_relationship = biology_relationship.merge(
            relationship, on="{}_concept_id".format(source), how="left"
        )
        
    biology_relationship = biology_relationship.fillna("Unknown")
                
    return biology_relationship
