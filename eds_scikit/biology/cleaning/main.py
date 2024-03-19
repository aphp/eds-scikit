from datetime import datetime
from typing import List, Union

from loguru import logger

from eds_scikit.biology.cleaning.cohort import select_cohort
from eds_scikit.biology.utils.prepare_measurement import prepare_measurement_table
from eds_scikit.biology.utils.process_concepts import (
    ConceptsSet,
    fetch_all_concepts_set,
)
from eds_scikit.biology.viz.wrapper import plot_biology_summary
from eds_scikit.utils.typing import Data, DataFrame


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
    start_date : datetime, optional
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2022-05-01"`
    convert_units : bool, optional
        If True, convert units based on ConceptsSets Units object. Eager execution., by default False
    studied_cohort : Union[DataFrame, np.iterable, set], optional
        List of patient_ids to select

    Returns
    -------
    Data
        Same as the input with the transformed `bioclean` table
    """

    if concepts_sets is None:
        logger.info("No concepts sets provided. Loading default concepts sets.")
        concepts_sets = fetch_all_concepts_set()

    measurements = prepare_measurement_table(
        data, start_date, end_date, concepts_sets, False, convert_units
    )
    # Filter Measurement.
    if studied_cohort:
        measurements = select_cohort(measurements, studied_cohort)
    # Transform values
    data.bioclean = measurements

    measurements = measurements.merge(
        data.visit_occurrence[["care_site_id", "visit_occurrence_id"]],
        on="visit_occurrence_id",
    )
    measurements = measurements.merge(
        data.care_site[["care_site_id", "care_site_short_name"]], on="care_site_id"
    )
    # Plot values
    value_column = "value_as_number_normalized" if convert_units else "value_as_number"
    unit_column = (
        "unit_source_value_normalized" if convert_units else "unit_source_value"
    )

    plot_biology_summary(measurements, value_column, unit_column)
