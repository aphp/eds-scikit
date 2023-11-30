from datetime import datetime
from typing import List, Union

from eds_scikit.biology.cleaning.cohort import select_cohort
from eds_scikit.biology.cleaning.transform import transform_measurement
from eds_scikit.biology.cleaning.utils import check_data_and_select_columns
from eds_scikit.biology.utils.process_concepts import (
    ConceptsSet,
    fetch_all_concepts_set,
    get_concept_src_to_std,
)
from eds_scikit.biology.utils.process_measurement import (
    filter_measurement_by_date,
    get_measurement_std,
    get_valid_measurement,
)
from eds_scikit.io import settings
from eds_scikit.utils.typing import Data, DataFrame

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


def bioclean(
    data: Data,
    concepts_sets: List[ConceptsSet] = None,
    config_name: str = None,
    start_date: datetime = None,
    end_date: datetime = None,
    studied_cohort: Union[DataFrame, List[int]] = None,
    clip: bool = False,
    standard_terminologies: List[str] = default_standard_terminologies,
    standard_concept_regex: dict = default_standard_concept_regex,
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
    # Check the data and extract them
    measurement, concept, concept_relationship = check_data_and_select_columns(data)

    # Filter valid measurement
    measurement_valid = get_valid_measurement(measurement)

    # Filter measurement by date
    measurement_timed = filter_measurement_by_date(
        measurement_valid, start_date, end_date
    )

    # Query concepts-set information
    if concepts_sets is None:
        concepts_sets = fetch_all_concepts_set()
        
    biology_relationship_table = prepare_biology_relationship(data, source_terminologies, mapping)
    measurement_timed = measurement_timed.merge(biology_relationship_table, on="")
        
    # Extract concept-set
    measurement_std_filtered = get_measurement_std(measurement_timed, src_to_std)

    # Filter Measurement
    if studied_cohort:
        measurement_std_filtered = select_cohort(
            measurement_std_filtered, studied_cohort
        )

    # Transform values
    data.bioclean = transform_measurement(measurement_std_filtered, clip, config_name)
