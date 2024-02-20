import os
from shutil import rmtree
from typing import List, Union

import altair as alt
import pandas as pd
from loguru import logger

from eds_scikit.biology.viz.aggregate import aggregate_measurement
from eds_scikit.biology.viz.plot import plot_concepts_set
from eds_scikit.io import settings
from eds_scikit.utils.typing import DataFrame

default_standard_terminologies = settings.measurement_config["standard_terminologies"]
default_standard_concept_regex = settings.measurement_config["standard_concept_regex"]


def plot_biology_summary(
    measurement: DataFrame,
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
    save_folder_path: str = "Biology_summary",
    stats_only: bool = False,
    terminologies: List[str] = None,
    debug: bool = False,
) -> Union[alt.ConcatChart, pd.DataFrame]:
    """
    Aggregate measurements, create plots and saves all the concepts-sets in folder.


    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    save_folder_path : str, optional
        Name of the folder where the plots will be saved
    stats_only : bool, optional
        If ``True``, it will only aggregate the data for the [summary table][summary-table].
    terminologies : List[str], optional
        biology summary only on terminologies codes columns
    value_column : str, optional
        value column for distribution summary plot
    debug : bool, optional
        If ``True``, info log will de displayed to follow aggregation steps

    Returns
    -------
    List[alt.ConcatChart, pd.DataFrame]
        Altair plots describing the volumetric and the distribution properties of your biological data along with a pandas DataFrame with a statistical summary
    """

    if not value_column:
        raise ValueError(
            "Must give a 'value_column' parameter. By default, use value_as_number. Or value_as_number_normalized if exists."
        )
    if not unit_column:
        raise ValueError(
            "Must give a 'unit_column' parameter. By default, use unit_source_value. Or unit_source_value_normalized if exists."
        )

    if not os.path.isdir(save_folder_path):
        os.mkdir(save_folder_path)
        logger.info("{} folder has been created.", save_folder_path)

    if terminologies:
        measurement = measurement.drop(
            columns=[f"{col}_concept_code" for col in terminologies]
        )

    tables_agg = aggregate_measurement(
        measurement=measurement,
        value_column=value_column,
        unit_column=unit_column,
        stats_only=stats_only,
        overall_only=stats_only,
        category_columns=["concept_set", "care_site_short_name"],
        debug=debug,
    )

    table_names = list(tables_agg.keys())
    concept_sets_names = tables_agg[table_names[0]].concept_set.unique()

    for concept_set_name in concept_sets_names:

        concepts_set_path = "{}/{}".format(save_folder_path, concept_set_name)
        rmtree(concepts_set_path, ignore_errors=True)
        os.mkdir(concepts_set_path)
        logger.info(
            "{}/{} folder has been created.",
            save_folder_path,
            concept_set_name,
        )

        for table_name in table_names:
            table = tables_agg[table_name].query("concept_set == @concept_set_name")
            table.to_pickle(
                "{}/{}/{}.pkl".format(save_folder_path, concept_set_name, table_name)
            )

        logger.info(
            "{} has been processed and saved in {}/{} folder.",
            concept_set_name,
            save_folder_path,
            concept_set_name,
        )

        plot_concepts_set(
            concepts_set_name=concept_set_name, source_path=save_folder_path
        )
