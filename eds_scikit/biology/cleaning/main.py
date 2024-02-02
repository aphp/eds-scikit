from datetime import datetime
from typing import List, Union

from loguru import logger

from eds_scikit.biology.cleaning.cohort import select_cohort
from eds_scikit.biology.utils.process_concepts import ConceptsSet
from eds_scikit.biology.utils.prepare_measurement import prepare_measurement_table
from eds_scikit.biology.viz.wrapper import plot_biology_summary
from eds_scikit.io import settings
from eds_scikit.utils.typing import Data, DataFrame

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


def bioclean(
    data: Data,
    concepts_sets: List[ConceptsSet] = None,
    start_date: datetime = None,
    end_date: datetime = None,
    convert_units: bool = False,
    studied_cohort: Union[DataFrame, List[int]] = None,
) -> Data:
    """It follows the pipeline explained [here][cleaning]:

    Parameters
    ----------
    data : Data
        Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    concepts_sets : List[ConceptsSet], optional
        List of concepts-sets to select
    config_name : str, optional
        Name of the dataset used to [transform][eds_scikit.biology.cleaning.transform.transform_measurement] the data.
    start_date : datetime, optional
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2022-05-01"`
    studied_cohort : Union[DataFrame, np.iterable, set], optional
        List of patient_ids to select
    clip : bool, optional
        If `True` extreme values are set equal to the thresholds
    standard_terminologies : List[str], optional
        **EXAMPLE**: `["LOINC", "AnaBio"]`
    standard_concept_regex : dict, optional
        **EXAMPLE**: `{"LOINC": "[0-9]{2,5}[-][0-9]","AnaBio": "[A-Z][0-9]{4}"}`

    Returns
    -------
    Data
        Same as the input with the transformed `bioclean` table
    """
    
    if concepts_sets is None:
        logger.info("No concepts sets provided. Loading default concepts sets.")
        concepts_sets = fetch_all_concepts_set()
    
    measurements = prepare_measurement_table(data, start_date, end_date, concepts_sets, convert_units)
    
    # Filter Measurement.
    if studied_cohort:
        measurements = select_cohort(
            measurements, studied_cohort
        )

    # Transform values
    data.bioclean = measurements

    # Plot values
    value_column = "value_as_number_normalized" if convert_units else "value_as_number"
    plot_biology_summary_measurement(measurements, value_column)

