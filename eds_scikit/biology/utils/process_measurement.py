from datetime import datetime
from typing import List

from eds_scikit.biology.utils.process_concepts import ConceptsSet
from eds_scikit.utils.checks import check_columns
from eds_scikit.utils.framework import cache, is_koalas, to
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


def convert_measurement_units(
    measurement: DataFrame, concepts_sets: List[ConceptsSet]
) -> DataFrame:

    """Add value_as_number_normalized, unit_source_value_normalized and factor columns to measurement dataframe based on concepts_sets and units.

    Parameters
    ----------
    measurement : DataFrame
    concepts_sets : List[ConceptsSet]

    Returns
    -------
    DataFrame
        Measurement with added columns value_as_number_normalized, unit_source_value_normalized and factor.
    """

    if is_koalas(measurement):
        measurement = cache(measurement)
        measurement.shape
        conversion_table = to(
            "koalas", get_conversion_table(measurement, concepts_sets)
        )
    else:
        conversion_table = get_conversion_table(measurement, concepts_sets)

    measurement = measurement.merge(
        conversion_table, on=["concept_set", "unit_source_value"]
    )
    measurement["value_as_number_normalized"] = (
        measurement["value_as_number"] * measurement["factor"]
    )

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
