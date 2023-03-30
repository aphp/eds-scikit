from datetime import datetime
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from loguru import logger

from eds_scikit.biology.utils.process_concepts import (
    ConceptsSet,
    get_concept_src_to_std,
)
from eds_scikit.biology.utils.process_measurement import (
    filter_concept_by_count,
    filter_concept_by_number,
    filter_measurement_by_date,
    filter_missing_values,
    get_measurement_std,
    get_valid_measurement,
    normalize_unit,
)
from eds_scikit.io import settings
from eds_scikit.utils.checks import check_columns, check_tables
from eds_scikit.utils.framework import is_koalas, to
from eds_scikit.utils.typing import Data, DataFrame

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


def aggregate_concepts_set(
    data: Data,
    concepts_set: ConceptsSet,
    start_date: datetime = None,
    end_date: datetime = None,
    number_of_concept: Tuple[str, int] = None,
    limit_count: Tuple[str, int] = None,
    standard_terminologies: List[str] = default_standard_terminologies,
    standard_concept_regex: dict = default_standard_concept_regex,
    pd_limit_size: int = 100000,
    stats_only: bool = False,
) -> Dict[str, pd.DataFrame]:
    """Aggregates the data for [visualization][visualization].

    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    concepts_set : ConceptsSet
        List of concepts-sets to select
    start_date : datetime, optional
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2022-01-01"`
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
    Dict[str, pd.DataFrame]
        Aggregated tables for visualization
    """
    # Check the data
    _check_the_data_for_aggregation(data)

    # Extract tables
    measurement = (
        data.measurement[
            list(
                data.measurement.columns[
                    data.measurement.columns.isin(
                        [
                            "measurement_id",
                            "visit_occurrence_id",
                            "measurement_date",
                            "measurement_datetime",
                            "value_as_number",
                            "unit_source_value",
                            "row_status_source_value",
                            "measurement_source_concept_id",
                        ]
                    )
                ]
            )
        ]
        if "bioclean" not in dir(data)
        else data.bioclean
    )
    concept = data.concept[
        [
            "concept_id",
            "concept_name",
            "concept_code",
            "vocabulary_id",
        ]
    ]
    concept_relationship = data.concept_relationship[
        ["concept_id_1", "concept_id_2", "relationship_id"]
    ]
    visit = data.visit_occurrence[["visit_occurrence_id", "care_site_id"]]
    care_site = data.care_site[["care_site_short_name", "care_site_id"]]

    # Filter measurement by date
    measurement = filter_measurement_by_date(measurement, start_date, end_date)

    if "bioclean" in dir(data):
        measurement_std_filtered = _extract_concepts_set(measurement, concepts_set)

    else:
        # Filter valid measurement
        measurement_valid = get_valid_measurement(measurement)

        # Select concepts-set
        src_to_std = get_concept_src_to_std(
            concept,
            concept_relationship,
            concepts_set,
            standard_concept_regex,
            standard_terminologies,
        )

        if "concepts_set" in src_to_std.columns:
            src_to_std = src_to_std.drop(columns="concepts_set")

        # Extract concept-set
        measurement_std_filtered = get_measurement_std(measurement_valid, src_to_std)
        measurement_std_filtered = measurement_std_filtered.drop(
            columns="source_concept_id"
        )

    # Filter limit number of concepts
    if number_of_concept:
        measurement_std_filtered = filter_concept_by_number(
            measurement_std_filtered, number_of_concept
        )

    # Filter limit concept with enough measurements
    if limit_count:
        measurement_std_filtered = filter_concept_by_count(
            measurement_std_filtered, limit_count
        )

    # Add care_site column
    measurement_std_filtered = _add_hospital(measurement_std_filtered, visit, care_site)

    # Normalize unit string
    measurement_std_filtered = normalize_unit(measurement_std_filtered)

    # Aggregate measurement
    tables = aggregate_measurement(
        measurement=measurement_std_filtered,
        pd_limit_size=pd_limit_size,
        stats_only=stats_only,
        overall_only=stats_only,
    )
    return tables


def _check_the_data_for_aggregation(data: Data):
    check_tables(
        data,
        required_tables=[
            "measurement",
            "concept",
            "concept_relationship",
            "visit_occurrence",
            "care_site",
        ],
    )
    check_columns(
        data.measurement,
        required_columns=[
            "measurement_id",
            "visit_occurrence_id",
            "measurement_date",
            "value_as_number",
            "unit_source_value",
            "row_status_source_value",
            "measurement_source_concept_id",
        ],
    )
    check_columns(
        data.concept,
        required_columns=[
            "concept_id",
            "concept_name",
            "concept_code",
            "vocabulary_id",
        ],
    )
    check_columns(
        data.visit_occurrence,
        required_columns=["visit_occurrence_id", "care_site_id"],
    )
    check_columns(
        data.concept_relationship,
        required_columns=["concept_id_1", "concept_id_2", "relationship_id"],
    )
    check_columns(
        data.care_site,
        required_columns=["care_site_short_name", "care_site_id"],
    )


def _extract_concepts_set(measurement: DataFrame, concepts_set: ConceptsSet):

    check_columns(
        measurement,
        required_columns=[
            "measurement_id",
            "visit_occurrence_id",
            "measurement_date",
            "value_as_number",
            "transformed_value",
            "unit_source_value",
            "transformed_unit",
        ],
    )

    concept_cols = [
        column_name
        for column_name in measurement.columns
        if ("concept_code" in column_name) or ("concept_name" in column_name)
    ]
    measurement = measurement[
        [
            "measurement_id",
            "visit_occurrence_id",
            "measurement_date",
            "value_as_number",
            "transformed_value",
            "unit_source_value",
            "transformed_unit",
            "concepts_set",
        ]
        + concept_cols
    ]
    measurement = measurement[measurement["concepts_set"] == concepts_set.name]
    measurement = measurement.drop(
        columns=["value_as_number", "unit_source_value", "concepts_set"]
    ).rename(
        columns={
            "transformed_value": "value_as_number",
            "transformed_unit": "unit_source_value",
        }
    )
    return measurement


def _add_hospital(measurement: DataFrame, visit: DataFrame, care_site: DataFrame):
    check_columns(
        df=visit,
        required_columns=["visit_occurrence_id", "care_site_id"],
        df_name="visit",
    )
    check_columns(
        df=care_site,
        required_columns=["care_site_short_name", "care_site_id"],
        df_name="care_site",
    )

    measurement = measurement.merge(visit, on="visit_occurrence_id", how="left")
    measurement = measurement.merge(care_site, on="care_site_id", how="left")
    measurement = measurement.drop(columns=["care_site_id", "visit_occurrence_id"])
    measurement.fillna({"care_site_short_name": "Unknown"}, inplace=True)

    return measurement


def aggregate_measurement(
    measurement: DataFrame,
    pd_limit_size: int,
    stats_only: bool,
    overall_only: bool,
):

    check_columns(
        df=measurement,
        required_columns=[
            "measurement_id",
            "unit_source_value",
            "measurement_date",
            "value_as_number",
        ],
        df_name="measurement",
    )

    # Convert DF to Pandas if small enough
    if is_koalas(measurement):
        measurement.spark.cache()
        logger.info(
            "Checking if the Koalas DataFrame is small enough to be converted into Pandas DataFrame"
        )
    size = measurement.shape[0]
    if size < pd_limit_size:
        logger.info(
            "The number of measurements identified is {} < {}. DataFrame is converting to Pandas...",
            size,
            pd_limit_size,
        )
        measurement = to("pandas", measurement)
        if measurement.empty:
            return {"measurement": measurement}
    else:
        logger.info(
            "The number of measurements identified is {}.",
            size,
        )

    # Truncate date
    measurement["measurement_month"] = (
        measurement["measurement_date"].astype("datetime64").dt.strftime("%Y-%m")
    )
    measurement = measurement.drop(columns=["measurement_date"])

    # Filter measurement with missing values
    filtered_measurement, missing_value = filter_missing_values(measurement)

    # Compute measurement statistics by code
    measurement_stats = _describe_measurement_by_code(
        filtered_measurement, overall_only
    )

    if stats_only:
        return {"measurement_stats": measurement_stats}

    # Count measurement by care_site and by code per each month
    measurement_volumetry = _count_measurement_by_care_site_and_code_per_month(
        filtered_measurement, missing_value
    )

    # Bin measurement values by care_site and by code
    measurement_distribution = _bin_measurement_value_by_care_site_and_code(
        filtered_measurement
    )

    return {
        "measurement_stats": measurement_stats,
        "measurement_volumetry": measurement_volumetry,
        "measurement_distribution": measurement_distribution,
    }


def _describe_measurement_by_code(
    filtered_measurement: DataFrame, overall_only: bool = False
):
    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            "unit_source_value",
            "measurement_month",
            "value_as_number",
            "care_site_short_name",
        ],
        df_name="filtered_measurement",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if ("concept_code" in column_name) or ("concept_name" in column_name)
    ]

    measurement_stats_overall = (
        (
            filtered_measurement[
                [
                    "unit_source_value",
                    "value_as_number",
                ]
                + concept_cols
            ]
            .groupby(
                concept_cols
                + [
                    "unit_source_value",
                ],
                dropna=False,
            )
            .describe()
        )
        .droplevel(0, 1)
        .reset_index()
    )

    # Add stats column to the measurement table
    measurement_mad = measurement_stats_overall.merge(
        filtered_measurement[concept_cols + ["value_as_number", "unit_source_value"]],
        on=concept_cols + ["unit_source_value"],
    )

    # Compute median deviation for each measurement
    measurement_mad["median_deviation"] = abs(
        measurement_mad["50%"] - measurement_mad["value_as_number"]
    )
    measurement_mad = measurement_mad.drop(columns="value_as_number")

    # Compute MAD
    measurement_mad = (
        measurement_mad.groupby(
            concept_cols
            + [
                "unit_source_value",
            ],
            as_index=False,
            dropna=False,
        )["median_deviation"]
        .median()
        .rename(columns={"median_deviation": "MAD"})
    )

    # Add MAD column to the measurement table
    measurement_stats_overall = measurement_stats_overall.merge(
        measurement_mad[concept_cols + ["MAD", "unit_source_value"]],
        on=concept_cols + ["unit_source_value"],
    )

    logger.info("The overall statistics of measurements by code are computing...")
    measurement_stats_overall = to("pandas", measurement_stats_overall)
    logger.info("The overall statistics of measurements are computed...")

    measurement_stats_overall["MAD"] = 1.48 * measurement_stats_overall["MAD"]

    measurement_stats_overall["max_threshold"] = (
        measurement_stats_overall["50%"] + 4 * measurement_stats_overall["MAD"]
    )
    measurement_stats_overall["min_threshold"] = (
        measurement_stats_overall["50%"] - 4 * measurement_stats_overall["MAD"]
    )
    measurement_stats_overall["min_threshold"] = measurement_stats_overall[
        "min_threshold"
    ].where(measurement_stats_overall["min_threshold"] >= 0, 0)

    if overall_only:
        return measurement_stats_overall

    measurement_stats_overall["care_site_short_name"] = "ALL"

    measurement_stats = (
        (
            filtered_measurement[
                [
                    "unit_source_value",
                    "care_site_short_name",
                    "value_as_number",
                ]
                + concept_cols
            ]
            .groupby(
                concept_cols
                + [
                    "care_site_short_name",
                    "unit_source_value",
                ],
                dropna=False,
            )
            .describe()
        )
        .droplevel(0, 1)
        .reset_index()
    )

    measurement_stats["MAD"] = None
    measurement_stats["max_threshold"] = None
    measurement_stats["min_threshold"] = None

    logger.info("The statistics of measurements by care site are computing...")
    measurement_stats = to("pandas", measurement_stats)
    logger.info("The statistics of measurements by care site are computed...")

    measurement_stats = pd.concat([measurement_stats_overall, measurement_stats])

    return measurement_stats


def _count_measurement_by_care_site_and_code_per_month(
    filtered_measurement: DataFrame, missing_value: DataFrame
):
    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            "unit_source_value",
            "measurement_month",
            "care_site_short_name",
        ],
        df_name="filtered_measurement",
    )

    check_columns(
        df=missing_value,
        required_columns=[
            "measurement_id",
            "unit_source_value",
            "measurement_month",
            "care_site_short_name",
        ],
        df_name="missing_value",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if "concept_code" in column_name
    ]

    measurement_count = (
        filtered_measurement[
            [
                "measurement_id",
                "unit_source_value",
                "care_site_short_name",
                "measurement_month",
            ]
            + concept_cols
        ]
        .groupby(
            concept_cols
            + [
                "unit_source_value",
                "care_site_short_name",
                "measurement_month",
            ],
            as_index=False,
            dropna=False,
        )
        .agg({"measurement_id": "count"})
        .rename(columns={"measurement_id": "# measurements"})
    )
    missing_value_count = (
        missing_value[
            [
                "measurement_id",
                "unit_source_value",
                "care_site_short_name",
                "measurement_month",
            ]
            + concept_cols
        ]
        .groupby(
            concept_cols
            + [
                "unit_source_value",
                "care_site_short_name",
                "measurement_month",
            ],
            as_index=False,
            dropna=False,
        )
        .agg({"measurement_id": "count"})
        .rename(columns={"measurement_id": "# missing_values"})
    )

    missing_value_count[["measurement_month"]] = missing_value_count[
        ["measurement_month"]
    ].fillna("Unknown")

    logger.info(
        "The counting of measurements by care site and code for each month is processing..."
    )
    measurement_count = to("pandas", measurement_count)
    logger.info("The counting of measurements is finished...")

    logger.info(
        "The counting of missing values by care site and code for each month is processing..."
    )
    missing_value_count = to("pandas", missing_value_count)
    logger.info("The counting of missing values is finished...")

    measurement_volumetry = measurement_count.merge(
        missing_value_count,
        on=concept_cols
        + [
            "unit_source_value",
            "care_site_short_name",
            "measurement_month",
        ],
        how="outer",
    )

    # Replace None by 0
    measurement_volumetry[
        ["# missing_values", "# measurements"]
    ] = measurement_volumetry[["# missing_values", "# measurements"]].fillna(0)
    return measurement_volumetry


def _bin_measurement_value_by_care_site_and_code(
    filtered_measurement: DataFrame,
):

    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            "unit_source_value",
            "care_site_short_name",
            "value_as_number",
        ],
        df_name="filtered_measurement",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if "concept_code" in column_name
    ]

    # Compute median per code
    measurement_median = (
        filtered_measurement[
            concept_cols
            + [
                "value_as_number",
            ]
        ]
        .groupby(
            concept_cols,
            as_index=False,
            dropna=False,
        )
        .median()
        .rename(columns={"value_as_number": "median"})
    )

    # Add median column to the measurement table
    measurement_median = measurement_median.merge(
        filtered_measurement[
            concept_cols
            + [
                "value_as_number",
            ]
        ],
        on=concept_cols,
    )

    # Compute median deviation for each measurement
    measurement_median["median_deviation"] = abs(
        measurement_median["median"] - measurement_median["value_as_number"]
    )

    # Compute MAD per care site and code
    measurement_mad = (
        measurement_median[
            concept_cols
            + [
                "median",
                "median_deviation",
            ]
        ]
        .groupby(
            concept_cols
            + [
                "median",
            ],
            as_index=False,
            dropna=False,
        )
        .median()
        .rename(columns={"median_deviation": "MAD"})
    )

    measurement_mad["MAD"] = 1.48 * measurement_mad["MAD"]

    # Add MAD column to the measurement table
    measurement_binned = measurement_mad.merge(
        filtered_measurement[
            concept_cols
            + [
                "measurement_id",
                "care_site_short_name",
                "unit_source_value",
                "value_as_number",
            ]
        ],
        on=concept_cols,
    )

    # Compute binned value
    measurement_binned["max_value"] = (
        measurement_binned["median"] + 4 * measurement_binned["MAD"]
    )
    measurement_binned["min_value"] = (
        measurement_binned["median"] - 4 * measurement_binned["MAD"]
    )
    measurement_binned["min_value"] = measurement_binned["min_value"].where(
        measurement_binned["min_value"] >= 0, 0
    )
    measurement_binned["binned_value"] = measurement_binned["value_as_number"].mask(
        measurement_binned["value_as_number"] > measurement_binned["max_value"],
        measurement_binned["max_value"],
    )
    measurement_binned["binned_value"] = measurement_binned["binned_value"].mask(
        measurement_binned["value_as_number"] < measurement_binned["min_value"],
        measurement_binned["min_value"],
    )
    # Freedman–Diaconis rule (https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule)
    bin_width = (
        measurement_binned[
            concept_cols
            + [
                "binned_value",
            ]
        ]
        .groupby(
            concept_cols,
            dropna=False,
        )
        .describe()
        .droplevel(0, 1)
        .reset_index()
    )
    bin_width["bin_width"] = (
        2 * (bin_width["75%"] - bin_width["25%"]) / np.cbrt(bin_width["count"])
    )
    # Add bin width column to the measurement table
    measurement_binned = bin_width[concept_cols + ["bin_width"]].merge(
        measurement_binned,
        on=concept_cols,
    )

    measurement_binned["over_outlier"] = (
        measurement_binned["value_as_number"] > measurement_binned["max_value"]
    )
    measurement_binned["under_outlier"] = (
        measurement_binned["value_as_number"] < measurement_binned["min_value"]
    )

    measurement_binned["binned_value"] = measurement_binned["binned_value"].where(
        measurement_binned["over_outlier"] | measurement_binned["under_outlier"],
        (
            np.floor(
                measurement_binned["value_as_number"] / measurement_binned["bin_width"]
            )
            + 0.5
        )
        * measurement_binned["bin_width"],
    )

    # Count the frequencies
    measurement_distribution = (
        measurement_binned[
            concept_cols
            + [
                "care_site_short_name",
                "binned_value",
                "measurement_id",
                "over_outlier",
                "under_outlier",
            ]
        ]
        .groupby(
            concept_cols
            + [
                "care_site_short_name",
                "over_outlier",
                "under_outlier",
                "binned_value",
            ],
            dropna=False,
            as_index=False,
        )
        .agg({"measurement_id": "count"})
        .rename(columns={"measurement_id": "frequency"})
    )

    logger.info("The binning of measurements' values is processing...")
    measurement_distribution = to("pandas", measurement_distribution)
    logger.info("The binning of measurements' values is finished...")
    return measurement_distribution
