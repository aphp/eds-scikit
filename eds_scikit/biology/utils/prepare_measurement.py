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
    filter_measurement_by_date,
    filter_measurement_valid,
    normalize_unit,
    tag_measurement_anomaly,
)
from eds_scikit.io.settings import mapping
from eds_scikit.utils.framework import is_koalas, to
from eds_scikit.utils.typing import Data, DataFrame


def prepare_measurement_table(
    data: Data,
    start_date: datetime = None,
    end_date: datetime = None,
    concept_sets: List[ConceptsSet] = None,
    get_all_terminologies=True,
    convert_units=False,
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
            "Lazy preparation not available if convert_units=True. Computed table will be cached."
        )
        measurement.cache()
        conversion_table = to("koalas", get_conversion_table(measurement, concept_sets))
        measurement = measurement.merge(
            conversion_table, on=["concept_set", "unit_source_value"]
        )
        measurement["value_as_number_normalized"] = (
            measurement["value_as_number"] * measurement["factor"]
        )

    if is_koalas(measurement):
        measurement.cache()
        logger.info("Done. Once computed, measurement will be cached.")

    return measurement


def get_conversion_table(
    measurement: DataFrame, concepts_sets: List[ConceptsSet]
) -> DataFrame:

    """Given measurement dataframe and list of concepts_sets output conversion table to be merged with measurement.

    Parameters
    ----------
    measurement : DataFrame
    concepts_sets : List[ConceptsSet]

    Returns
    -------
    DataFrame
        Conversion table to be merged with measurement
    """
    conversion_table = (
        measurement.groupby("concept_set")["unit_source_value"]
        .unique()
        .explode()
        .to_frame()
        .reset_index()
    )
    conversion_table = to("pandas", conversion_table)
    conversion_table["unit_source_value_normalized"] = conversion_table[
        "unit_source_value"
    ]
    conversion_table["factor"] = conversion_table.apply(
        lambda x: 1 if x.unit_source_value_normalized else 0, axis=1
    )

    for concept_set in concepts_sets:
        unit_source_value_normalized = concept_set.units.target_unit
        conversion_table.loc[
            conversion_table.concept_set == concept_set.name,
            "unit_source_value_normalized",
        ] = conversion_table.apply(
            lambda x: unit_source_value_normalized
            if concept_set.units.can_be_converted(
                x.unit_source_value, unit_source_value_normalized
            )
            else concept_set.units.get_unit_base(x.unit_source_value),
            axis=1,
        )
        conversion_table.loc[
            conversion_table.concept_set == concept_set.name, "factor"
        ] = conversion_table.apply(
            lambda x: concept_set.units.convert_unit(
                x.unit_source_value, x.unit_source_value_normalized
            ),
            axis=1,
        )

    conversion_table = conversion_table.fillna(1)

    return conversion_table
