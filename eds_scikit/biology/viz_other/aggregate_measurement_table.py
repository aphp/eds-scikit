from datetime import datetime
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
from loguru import logger

from eds_scikit.biology.utils.concept_set import (
    ConceptsSet,
    get_concept_src_to_std,
)
from eds_scikit.biology.utils.filter_measurement import (
    filter_measurement_valid,
    filter_concept_by_count,
    filter_concept_by_number,
    filter_measurement_by_date,
    filter_missing_values,
    get_measurement_std,
    normalize_unit,
)
from eds_scikit.io import settings
from eds_scikit.utils.checks import check_columns, check_tables
from eds_scikit.utils.framework import is_koalas, to
from eds_scikit.utils.typing import Data, DataFrame

"""

NB : ça serait cool de l'avoir avec les prepare, filter, etc : aggreate_table(...)

"""


"""

POUR LES VIZS BOKEH

"""

def compute_df_value_statistics(df, pivot_columns, value_column):
    #df_stats = df.groupby(pivot_columns, as_index=True)[value_column].quantile([0.05, 0.25, 0.5, 0.75, 0.95]).unstack()
    df_stats = df.groupby(pivot_columns, as_index=True)[[value_column]].describe() #ATTENTION : le describe c'est un miracle. marche avec [[...]] mais pas [...]
    df_stats = df_stats.droplevel(0, axis=1)[["25%", "50%", "75%"]]
    df_stats.columns = "q" + df_stats.columns.str[:-1]
    if is_koalas(df_stats):
        df_stats = df_stats.to_pandas()
    return df_stats

def compute_df_category_statistics(df, pivot_columns, category_column):
    df_stats = df.groupby(pivot_columns, as_index=True)[category_column].value_counts().to_frame().rename(columns={category_column : "count"}).reset_index()
    if is_koalas(df_stats):
        df_stats = df_stats.to_pandas() #Sinon résultat nawak
    df_stats["total"] = df_stats.groupby(pivot_columns)["count"].transform(sum)
    df_stats["proportion"] = df_stats["count"].div(df_stats["total"])
    df_stats = df_stats.rename(columns={category_column : "category"})
    df_stats = df_stats.drop(columns=["total", "count"]).set_index(pivot_columns)
    return df_stats

"""

POUR LES VIZS ALTAIR. CA SERAIT COOL DE L AVOIR UN PEU MOINS CODE / CARE SITE - DEPENDENT
PLUS MODULABLE

"""

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
