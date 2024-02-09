from datetime import datetime

from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.typing import DataFrame


def filter_measurement_valid(measurement: DataFrame) -> DataFrame:
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
    return measurement_valid


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

    measurement.measurement_date = measurement.measurement_date.astype("datetime64[ns]")

    measurement.dropna(subset=["measurement_date"], inplace=True)

    if start_date:
        measurement = measurement[measurement["measurement_date"] >= start_date]
    if end_date:
        measurement = measurement[measurement["measurement_date"] <= end_date]

    return measurement


def filter_missing_values(measurement: DataFrame):
    missing_value = measurement[measurement["value_as_number"].isna()]
    filtered_measurement = measurement[~(measurement["value_as_number"].isna())]
    return (filtered_measurement, missing_value)


def tag_measurement_anomaly(measurement: DataFrame) -> DataFrame:
    """

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
    """

    measurement["range_high_anomaly"] = (~measurement.range_high.isna()) & (
        measurement["value_as_number"] > measurement["range_high"]
    )
    measurement["range_low_anomaly"] = (~measurement.range_low.isna()) & (
        measurement["value_as_number"] < measurement["range_low"]
    )

    return measurement


def normalize_unit(measurement: DataFrame):
    measurement["unit_source_value"] = (
        measurement["unit_source_value"].str.lower().fillna("Unknown")
    )
    return measurement
