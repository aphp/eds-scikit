from datetime import datetime
from typing import Tuple

from loguru import logger

from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.framework import get_framework, to
from eds_scikit.utils.typing import DataFrame


def get_valid_measurement(measurement: DataFrame) -> DataFrame:
    """Filter valid observations based on the `row_status_source_value` column

    Parameters
    ----------
    measurement : DataFrame
        DataFrame to filter

    Returns
    -------
    DataFrame
        DataFrame with valid observations only
    """
    check_columns(
        df=measurement,
        required_columns=["row_status_source_value"],
        df_name="measurment",
    )
    measurement_valid = measurement[measurement["row_status_source_value"] == "Validé"]
    measurement_valid = measurement_valid.drop(columns=["row_status_source_value"])
    logger.info("Valid measurements have been selected")
    return measurement_valid


def _select_adequate_date_column(measurement: DataFrame):
    missing_date = measurement.measurement_date.isna().sum()
    if missing_date > 0:
        missing_datetime = measurement.measurement_datetime.isna().sum()
        if missing_date > missing_datetime:
            measurement = measurement.drop(columns="measurement_date").rename(
                columns={"measurement_datetime": "measurement_date"}
            )
            logger.warning(
                "As the measurement_date column is not reliable ({} missing dates), it has been replaced by the measurement_datetime column ({} missing datetimes)",
                missing_date,
                missing_datetime,
            )
            missing_date = missing_datetime
        else:
            measurement = measurement.drop(columns="measurement_datetime")
    else:
        measurement = measurement.drop(columns="measurement_datetime")
    return measurement


def filter_measurement_by_date(
    measurement: DataFrame, start_date: datetime = None, end_date: datetime = None
) -> DataFrame:
    """Filter observations that are inside the selected time window

    Parameters
    ----------
    measurement : DataFrame
        DataFrame to filter
    start_date : datetime, optional
        **EXAMPLE**: `"2019-05-01"`
    end_date : datetime, optional
        **EXAMPLE**: `"2022-05-01"`

    Returns
    -------
    DataFrame
        DataFrame with observations inside the selected time window only
    """
    check_columns(
        df=measurement, required_columns=["measurement_date"], df_name="measurment"
    )

    if "measurement_datetime" in measurement.columns:
        measurement = _select_adequate_date_column(measurement=measurement)

    measurement.measurement_date = measurement.measurement_date.astype("datetime64[ns]")

    measurement.dropna(subset=["measurement_date"], inplace=True)

    if start_date:
        measurement = measurement[measurement["measurement_date"] >= start_date]
        logger.info("Measurements conducted after {} have been selected", start_date)
    if end_date:
        measurement = measurement[measurement["measurement_date"] <= end_date]
        logger.info("Measurements conducted before {} have been selected", end_date)

    return measurement


def filter_missing_values(measurement: DataFrame):
    missing_value = measurement[measurement["value_as_number"].isna()]
    filtered_measurement = measurement[~(measurement["value_as_number"].isna())]
    return (filtered_measurement, missing_value)


def filter_concept_by_count(
    measurement_std: DataFrame, terminology_limit_count: Tuple[str, int]
):
    terminology, limit_count = terminology_limit_count
    code_set = (
        measurement_std[["measurement_id", "{}_concept_code".format(terminology)]]
        .groupby("{}_concept_code".format(terminology), as_index=False)
        .agg({"measurement_id": "count"})
        .rename(columns={"measurement_id": "# measures_code"})
    )
    code_set = code_set[code_set["# measures_code"] >= limit_count]
    return measurement_std.merge(
        code_set, on="{}_concept_code".format(terminology), how="inner"
    )


def filter_concept_by_number(
    measurement_std: DataFrame, terminology_limit_number: Tuple[str, int]
):
    terminology, limit_number = terminology_limit_number
    code_set = (
        measurement_std[["measurement_id", "{}_concept_code".format(terminology)]]
        .groupby("{}_concept_code".format(terminology), as_index=False)
        .agg({"measurement_id": "count"})
        .rename(columns={"measurement_id": "# measures_code"})
    )
    code_set = code_set.nlargest(n=limit_number, columns="# measures_code")
    return measurement_std.merge(
        code_set, on="{}_concept_code".format(terminology), how="inner"
    )


def get_measurement_std(measurement: DataFrame, src_to_std: DataFrame):
    check_columns(
        df=measurement,
        required_columns=["measurement_source_concept_id"],
        df_name="measurement",
    )
    check_columns(
        df=src_to_std,
        required_columns=["source_concept_id"],
        df_name="src_to_std",
    )

    src_to_std = to(get_framework(measurement), src_to_std)
    measurement_std = src_to_std.merge(
        measurement,
        left_on="source_concept_id",
        right_on="measurement_source_concept_id",
    )

    measurement_std = measurement_std.drop(columns=["measurement_source_concept_id"])

    concept_cols = [
        column_name
        for column_name in measurement_std.columns
        if "concept" in column_name
    ]

    measurement_std[concept_cols] = measurement_std[concept_cols].fillna("Unknown")

    return measurement_std


def normalize_unit(measurement: DataFrame):
    measurement["unit_source_value"] = (
        measurement["unit_source_value"].str.lower().fillna("Unknown")
    )
    return measurement
