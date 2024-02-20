import ast
from typing import List, Union

import pandas as pd
from loguru import logger

from eds_scikit import datasets
from eds_scikit.biology.utils.process_units import Units
from eds_scikit.io import settings
from eds_scikit.utils.typing import DataFrame

default_standard_terminologies = settings.measurement_config["standard_terminologies"]
default_source_terminologies = settings.measurement_config["source_terminologies"]
default_standard_concept_regex = settings.measurement_config["standard_concept_regex"]
default_concepts_sets = datasets.default_concepts_sets


class ConceptsSet:
    """Class defining the concepts-sets with 2 attributes:

    - ``name``: the name of the concepts-set
    - ``concept_codes`` : the list of concepts codes included in the concepts-set
    """

    def __init__(self, name: str):
        self.name = name
        self.units = Units()

        fetched_codes = fetch_concept_codes_from_name(name)
        if fetched_codes:
            self.concept_codes = {"GLIMS_ANABIO": fetch_concept_codes_from_name(name)}
        else:
            self.concept_codes = {}

    def add_concept_codes(
        self, concept_codes: Union[str, List[str]], terminology: str = None
    ):
        if not terminology:
            logger.error(
                "concept_codes terminology must be provided. See settings.source_terminologie."
            )
            raise TypeError
        if isinstance(concept_codes, str):
            concept_codes = [concept_codes]
        elif isinstance(concept_codes, list):
            for concept_code in concept_codes:
                if not (isinstance(concept_code, str)):
                    logger.error("concept_codes must be string or list of string")
                    raise TypeError
            if not (terminology in self.concept_codes.keys()):
                self.concept_codes[terminology] = []
            for concept_code in concept_codes:
                if concept_code not in self.concept_codes[terminology]:
                    self.concept_codes[terminology].append(concept_code)
        else:
            logger.error("concept_codes must be string or list of string")
            raise TypeError

    def remove_concept_codes(
        self, concept_codes: Union[str, List[str]], terminology: str = None
    ):
        if not (terminology and terminology in self.concept_codes.keys()):
            logger.error(
                "concept_codes terminology must be provided and must exist in concept_codes keys"
            )
            raise TypeError
        if isinstance(concept_codes, str):
            concept_codes = [concept_codes]
        if isinstance(concept_codes, list):
            for concept_code in concept_codes:
                if concept_code in self.concept_codes[terminology]:
                    self.concept_codes[terminology].remove(concept_code)
                    logger.info("concept_code {} has been deleted", concept_code)
        else:
            logger.error("concept_codes must be string or list")
            raise TypeError

    def get_concept_codes_table(
        self, terminologies: str = None, relationship_table: DataFrame = None
    ):

        if not terminologies:
            terminologies = self.concept_codes.keys()

        result_df = pd.DataFrame({})
        for terminology in terminologies:
            df = pd.DataFrame(
                {
                    "concept_set": [self.name] * len(self.concept_codes[terminology]),
                    "terminology": [terminology] * len(self.concept_codes[terminology]),
                    "concept_code": self.concept_codes[terminology],
                    f"{terminology}_concept_code": self.concept_codes[terminology],
                }
            )

            if relationship_table is not None:
                df = df.merge(
                    relationship_table,
                    on=f"{terminology}_concept_code",
                    how="left",
                    suffixes=("_x", ""),
                )
                df = df[[column for column in df.columns if not ("_x" in column)]]

            result_df = pd.concat((df, result_df), axis=0)

        return result_df

    def add_target_unit(self, target_unit):
        self.units.add_target_unit(target_unit)

    def add_conversion(self, unit_a, unit_b, conversion):
        self.units.add_conversion(unit_a, unit_b, conversion)


def fetch_concept_codes_from_name(
    concepts_set_name: str, concepts_sets_table_name: str = "default_concepts_sets"
):
    default_concepts_sets = getattr(datasets, concepts_sets_table_name).set_index(
        "concepts_set_name"
    )
    if concepts_set_name in default_concepts_sets.index:
        standard_concepts = []
        concept_code_columns = [
            col for col in default_concepts_sets.columns if "concept_code" in col
        ]
        for column in concept_code_columns:
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
