import os
from datetime import datetime
from shutil import rmtree
from typing import List, Tuple, Union

import pandas as pd
from altair.vegalite.v4.api import VConcatChart as AltChart
from loguru import logger

from eds_scikit.biology.utils.process_concepts import (
    ConceptsSet,
    fetch_all_concepts_set,
)
from eds_scikit.biology.viz.aggregate import aggregate_concepts_set
from eds_scikit.biology.viz.plot import plot_concepts_set
from eds_scikit.io import settings
from eds_scikit.utils.typing import Data

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


def plot_biology_summary(
    data: Data,
    concepts_sets: List[ConceptsSet] = None,
    start_date: datetime = None,
    end_date: datetime = None,
    save_folder_path: str = "Biology_summary",
    number_of_concept: Tuple[str, int] = None,
    limit_count: Tuple[str, int] = None,
    standard_terminologies: List[str] = default_standard_terminologies,
    standard_concept_regex: dict = default_standard_concept_regex,
    pd_limit_size: int = 100000,
    stats_only: bool = False,
) -> Union[AltChart, pd.DataFrame]:
    """It aggregates, plots and saves all the concepts-sets in folders.


    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    concepts_sets : List[str], optional
        List of concepts-sets to select
    start_date : datetime
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2021-11-01"`
    save_folder_path : str, optional
        Name of the folder where the plots will be saved
    number_of_concept : Tuple[str, int], optional
        The maximum number of concepts for a given terminology
        **EXAMPLE**: `("LOINC", 5)`
    limit_count : Tuple[str, int], optional
        The minimum number of observations per concepts for a given terminology
        **EXAMPLE**: `("LOINC", 5)`
    standard_terminologies : List[str], optional
        **EXAMPLE**: `["LOINC", "AnaBio"]`
    standard_concept_regex : dict, optional
        **EXAMPLE**: `{"LOINC": "[0-9]{2,5}[-][0-9]","AnaBio": "[A-Z][0-9]{4}"}`
    pd_limit_size : int, optional
        The limit number of rows to convert [Koalas](https://koalas.readthedocs.io/en/latest/) DatFrame into [Pandas](https://pandas.pydata.org/) DataFrame
    stats_only : bool, optional
        If ``True``, it will only aggregate the data for the [summary table][summary-table].

    Returns
    -------
    List[AltChart, pd.DataFrame]
        Altair plots describing the volumetric and the distribution properties of your biological data along with a pandas DataFrame with a statistical summary
    """

    if concepts_sets is None:
        concepts_sets = fetch_all_concepts_set()
    elif isinstance(concepts_sets, ConceptsSet):
        concepts_sets = [concepts_sets]

    if not os.path.isdir(save_folder_path):
        os.mkdir(save_folder_path)
        logger.info("{} folder has been created.", save_folder_path)

    if isinstance(concepts_sets, list) and all(
        isinstance(concepts_set, ConceptsSet) for concepts_set in concepts_sets
    ):
        for concepts_set in concepts_sets:
            concepts_set_path = "{}/{}".format(save_folder_path, concepts_set.name)
            rmtree(concepts_set_path, ignore_errors=True)
            os.mkdir(concepts_set_path)
            logger.info(
                "{}/{} folder has been created.",
                save_folder_path,
                concepts_set.name,
            )

            tables = aggregate_concepts_set(
                data=data,
                concepts_set=concepts_set,
                start_date=start_date,
                end_date=end_date,
                number_of_concept=number_of_concept,
                limit_count=limit_count,
                standard_terminologies=standard_terminologies,
                standard_concept_regex=standard_concept_regex,
                pd_limit_size=pd_limit_size,
                stats_only=stats_only,
            )

            for table_name, table in tables.items():
                table.to_pickle(
                    "{}/{}/{}.pkl".format(
                        save_folder_path, concepts_set.name, table_name
                    )
                )

            logger.info(
                "{} has been processed and saved in {}/{} folder.",
                concepts_set.name,
                save_folder_path,
                concepts_set.name,
            )

            plot_concepts_set(
                concepts_set_name=concepts_set.name, source_path=save_folder_path
            )
    else:
        logger.error(
            "concepts_set type is {} and must be a ConceptsSet object or a list of ConceptsSet objects",
            type(concepts_sets),
        )
