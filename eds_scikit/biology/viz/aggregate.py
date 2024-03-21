from typing import List

import numpy as np
import pandas as pd
from loguru import logger

from eds_scikit.biology.utils.process_measurement import filter_missing_values
from eds_scikit.io import settings
from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.framework import to
from eds_scikit.utils.typing import DataFrame

default_standard_terminologies = settings.measurement_config["standard_terminologies"]
default_standard_concept_regex = settings.measurement_config["standard_concept_regex"]


def aggregate_measurement(
    measurement: DataFrame,
    stats_only: bool,
    overall_only: bool,
    value_column: str,
    unit_column: str,
    category_columns=[],
    debug=False,
):
    """Aggregates measurement dataframe in three descriptive and synthetic dataframe :
      - measurement_stats
      - measurement_volumetry
      - measurement_distribution

    Useful function before plotting.

    Parameters
    ----------
    measurement : DataFrame
        _description_
    stats_only : bool
        _description_
    overall_only : bool
        _description_
    category_columns : list, optional
        _description_, by default []

    Returns
    -------
    _type_
        _description_
    """

    check_columns(
        df=measurement,
        required_columns=[
            "measurement_id",
            unit_column,
            "measurement_date",
            value_column,
        ]
        + category_columns,
        df_name="measurement",
    )

    measurement.shape

    # Truncate date
    measurement["measurement_month"] = (
        measurement["measurement_date"].astype("datetime64").dt.strftime("%Y-%m")
    )
    measurement = measurement.drop(columns=["measurement_date"])

    # Filter measurement with missing values
    filtered_measurement, missing_value = filter_missing_values(measurement)

    # Compute measurement statistics by code
    measurement_stats = _describe_measurement_by_code(
        filtered_measurement,
        overall_only,
        value_column,
        unit_column,
        category_columns,
        debug,
    )

    if stats_only:
        return {"measurement_stats": measurement_stats}

    # Count measurement by care_site and by code per each month
    measurement_volumetry = _count_measurement_by_category_and_code_per_month(
        filtered_measurement,
        missing_value,
        value_column,
        unit_column,
        category_columns,
        debug,
    )

    # Bin measurement values by care_site and by code
    measurement_distribution = _bin_measurement_value_by_category_and_code(
        filtered_measurement, value_column, unit_column, category_columns, debug
    )

    return {
        "measurement_stats": measurement_stats,
        "measurement_volumetry": measurement_volumetry,
        "measurement_distribution": measurement_distribution,
    }


def _describe_measurement_by_code(
    filtered_measurement: DataFrame,
    overall_only: bool = False,
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
    category_columns=[],
    debug: bool = False,
):
    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            unit_column,
            "measurement_month",
            value_column,
        ]
        + category_columns,
        df_name="filtered_measurement",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if ("concept_code" in column_name) or ("concept_name" in column_name)
    ] + category_columns

    measurement_stats_overall = (
        (
            filtered_measurement[
                [
                    unit_column,
                    value_column,
                ]
                + concept_cols
            ]
            .groupby(
                concept_cols
                + [
                    unit_column,
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
        filtered_measurement[concept_cols + [value_column, unit_column]],
        on=concept_cols + [unit_column],
    )

    # Compute median deviation for each measurement
    measurement_mad["median_deviation"] = abs(
        measurement_mad["50%"] - measurement_mad[value_column]
    )
    measurement_mad = measurement_mad.drop(columns=value_column)

    # Compute MAD
    measurement_mad = (
        measurement_mad.groupby(
            concept_cols
            + [
                unit_column,
            ],
            as_index=False,
            dropna=False,
        )["median_deviation"]
        .median()
        .rename(columns={"median_deviation": "MAD"})
    )

    # Add MAD column to the measurement table
    measurement_stats_overall = measurement_stats_overall.merge(
        measurement_mad[concept_cols + ["MAD", unit_column]],
        on=concept_cols + [unit_column],
    )

    logger.info(
        "The overall statistics of measurements by code are computing..."
    ) if debug else None
    measurement_stats_overall = to("pandas", measurement_stats_overall)
    logger.info(
        "The overall statistics of measurements are computed..."
    ) if debug else None

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
                    unit_column,
                    value_column,
                ]
                + concept_cols
            ]
            .groupby(
                concept_cols
                + [
                    unit_column,
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

    logger.info(
        "The statistics of measurements by care site are computing..."
    ) if debug else None
    measurement_stats = to("pandas", measurement_stats)
    logger.info(
        "The statistics of measurements by care site are computed..."
    ) if debug else None

    measurement_stats = pd.concat([measurement_stats_overall, measurement_stats])

    return measurement_stats


def _count_measurement_by_category_and_code_per_month(
    filtered_measurement: DataFrame,
    missing_value: DataFrame,
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
    category_columns=[],
    debug: bool = False,
):
    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            unit_column,
            "measurement_month",
        ]
        + category_columns,
        df_name="filtered_measurement",
    )

    check_columns(
        df=missing_value,
        required_columns=[
            "measurement_id",
            unit_column,
            "measurement_month",
        ],
        df_name="missing_value",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if "concept_code" in column_name
    ] + category_columns

    measurement_count = (
        filtered_measurement[
            [
                "measurement_id",
                unit_column,
                "measurement_month",
            ]
            + concept_cols
        ]
        .groupby(
            concept_cols
            + [
                unit_column,
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
                unit_column,
                "measurement_month",
            ]
            + concept_cols
        ]
        .groupby(
            concept_cols
            + [
                unit_column,
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
    ) if debug else None
    measurement_count = to("pandas", measurement_count)
    logger.info("The counting of measurements is finished...") if debug else None

    logger.info(
        "The counting of missing values by care site and code for each month is processing..."
    ) if debug else None
    missing_value_count = to("pandas", missing_value_count)
    logger.info("The counting of missing values is finished...") if debug else None

    measurement_volumetry = measurement_count.merge(
        missing_value_count,
        on=concept_cols
        + [
            unit_column,
            "measurement_month",
        ],
        how="outer",
    )

    # Replace None by 0
    measurement_volumetry[
        ["# missing_values", "# measurements"]
    ] = measurement_volumetry[["# missing_values", "# measurements"]].fillna(0)
    return measurement_volumetry


def _bin_measurement_value_by_category_and_code(
    filtered_measurement: DataFrame,
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
    category_columns=[],
    debug: bool = False,
):

    check_columns(
        df=filtered_measurement,
        required_columns=[
            "measurement_id",
            unit_column,
            value_column,
        ]
        + category_columns,
        df_name="filtered_measurement",
    )

    concept_cols = [
        column_name
        for column_name in filtered_measurement.columns
        if "concept_code" in column_name
    ] + category_columns

    if not (
        ("min_value" in filtered_measurement.columns)
        or ("max_value" in filtered_measurement.columns)
    ):
        filtered_measurement = add_mad_minmax(
            filtered_measurement, concept_cols, value_column
        )

    measurement_binned = filtered_measurement

    measurement_binned["min_value"] = measurement_binned["min_value"].where(
        measurement_binned["min_value"] >= 0, 0
    )
    measurement_binned["binned_value"] = measurement_binned[value_column].mask(
        measurement_binned[value_column] > measurement_binned["max_value"],
        measurement_binned["max_value"],
    )

    measurement_binned["binned_value"] = measurement_binned["binned_value"].mask(
        measurement_binned[value_column] < measurement_binned["min_value"],
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
        measurement_binned[value_column] > measurement_binned["max_value"]
    )
    measurement_binned["under_outlier"] = (
        measurement_binned[value_column] < measurement_binned["min_value"]
    )

    measurement_binned["binned_value"] = measurement_binned["binned_value"].where(
        measurement_binned["over_outlier"] | measurement_binned["under_outlier"],
        (
            np.floor(measurement_binned[value_column] / measurement_binned["bin_width"])
            + 0.5
        )
        * measurement_binned["bin_width"],
    )

    # Count the frequencies
    measurement_distribution = (
        measurement_binned[
            concept_cols
            + [
                "binned_value",
                "measurement_id",
                "over_outlier",
                "under_outlier",
            ]
        ]
        .groupby(
            concept_cols
            + [
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

    logger.info(
        "The binning of measurements' values is processing..."
    ) if debug else None
    measurement_distribution = to("pandas", measurement_distribution)
    logger.info("The binning of measurements' values is finished...") if debug else None
    return measurement_distribution


def add_mad_minmax(
    measurement: DataFrame,
    category_cols: List[str],
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
) -> DataFrame:
    """Add min_value, max_value column to measurement based on MAD criteria.

    Parameters
    ----------
    measurement : DataFrame
        measurement dataframe
    category_cols : List[str]
        measurement category columns to perform the groupby on when computing MAD
    value_column : str
        measurement value column on which MAD will be computed

    Returns
    -------
    DataFrame
        measurement dataframe with added columns min_value, max_value
    """
    measurement_median = (
        measurement[category_cols + [value_column]]
        .groupby(
            category_cols,
            as_index=False,
            dropna=False,
        )
        .median()
        .rename(columns={value_column: "median"})
    )

    # Add median column to the measurement table
    measurement_median = measurement_median.merge(
        measurement[
            category_cols
            + [
                value_column,
            ]
        ],
        on=category_cols,
    )

    # Compute median deviation for each measurement
    measurement_median["median_deviation"] = abs(
        measurement_median["median"] - measurement_median[value_column]
    )

    # Compute MAD per care site and code
    measurement_mad = (
        measurement_median[
            category_cols
            + [
                "median",
                "median_deviation",
            ]
        ]
        .groupby(
            category_cols
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
    measurement = measurement_mad.merge(
        measurement,
        on=category_cols,
    )

    # Compute binned value
    measurement["max_value"] = measurement["median"] + 4 * measurement["MAD"]
    measurement["min_value"] = measurement["median"] - 4 * measurement["MAD"]

    return measurement
