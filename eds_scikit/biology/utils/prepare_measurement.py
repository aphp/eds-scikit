from datetime import datetime
from typing import List

from loguru import logger

from eds_scikit.biology.utils.check_data import (
    check_data_and_select_columns_measurement,
)
from eds_scikit.biology.utils.prepare_relationship import (
    prepare_biology_relationship_table,
)
from eds_scikit.biology.utils.process_concepts import ConceptsSet
from eds_scikit.biology.utils.process_measurement import (
    convert_measurement_units,
    filter_measurement_by_date,
    filter_measurement_valid,
    normalize_unit,
    tag_measurement_anomaly,
)
from eds_scikit.io.settings import measurement_config
from eds_scikit.utils.framework import cache, is_koalas
from eds_scikit.utils.typing import Data, DataFrame

mapping = measurement_config["mapping"]


def prepare_measurement_table(
    data: Data,
    start_date: datetime = None,
    end_date: datetime = None,
    concept_sets: List[ConceptsSet] = None,
    get_all_terminologies=True,
    convert_units=False,
    compute_table=False,
) -> DataFrame:
    """Returns filtered measurement table based on validity, date and concept_sets.

    The output format is identical to data.measurement but adding following columns :
    - range_high_anomaly, range_low_anomaly
    - {terminology}_code based on concept_sets terminologies
    - concept_sets
    - normalized_units and normalized_values if convert_units==True

    Parameters
    ----------
    data : Data
        Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    start_date : datetime, optional
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2022-05-01"`
    concept_sets : List[ConceptsSet], optional
        List of concepts-sets to select
    get_all_terminologies : bool, optional
        If True, all terminologies from settings terminologies will be added, by default True
    convert_units : bool, optional
        If True, convert units based on ConceptsSets Units object. Eager execution., by default False
    compute_table : bool, optional
        If True, compute table then cache it. Useful to prevent spark issues, especially when running in notebooks.

    Returns
    -------
    DataFrame
        Preprocessed measurement dataframe
    """

    measurement, _, _ = check_data_and_select_columns_measurement(data)

    # measurement preprocessing
    measurement = filter_measurement_valid(measurement)
    measurement = filter_measurement_by_date(measurement, start_date, end_date)
    measurement = normalize_unit(measurement)
    measurement = tag_measurement_anomaly(measurement)

    # measurement codes mapping
    biology_relationship_table = prepare_biology_relationship_table(
        data, concept_sets, get_all_terminologies
    )
    measurement = measurement.merge(
        biology_relationship_table,
        left_on="measurement_source_concept_id",
        right_on=f"{mapping[0][0]}_concept_id",
    )

    if convert_units:
        logger.info(
            "Lazy preparation not available if convert_units=True. Table will be computed then cached."
        )
        measurement = convert_measurement_units(measurement, concept_sets)

    measurement = cache(measurement)
    if compute_table or convert_units:
        measurement.shape

    if is_koalas(measurement):
        logger.info("Done. Once computed, measurement will be cached.")

    return measurement
