from typing import List

from eds_scikit.utils.framework import to
from eds_scikit.utils.typing import DataFrame


def measurement_values_summary(
    measurement: DataFrame,
    category_cols: List[str] = [
        "concept_set",
        "GLIMS_ANABIO_concept_code",
    ],
    value_column: str = "value_as_number",
    unit_column: str = "unit_source_value",
) -> DataFrame:
    """Compute measurement values and units summary by category_cols.

    Parameters
    ----------
    measurement : DataFrame
        measurement dataframe
    category_cols : List[str], optional
        columns on which to groupby the summary, by default ["concept_set", "GLIMS_ANABIO_concept_code",]
    value_column : str, optional
        value column to summarize, by default "value_as_number" but can be value_as_number_normalized if units conversion is applied.
    unit_column : str, optional
        units column to summarize, by default "unit_source_value" but can be unit_source_value_normalized if units conversion is applied.

    Returns
    -------
    DataFrame
        statistic summary dataframe
    """

    measurement.shape

    no_units = (measurement[unit_column] == "non renseigne") | (
        measurement[unit_column] == "Unkown"
    )

    stats_summary = (
        measurement[no_units]
        .groupby(category_cols)
        .agg(no_units=("measurement_id", "count"))
        .reset_index()
    )

    # Count measurements

    measurement_count = (
        measurement.groupby([*category_cols, unit_column])
        .agg(measurement_count=("measurement_id", "count"))
        .reset_index()
    )

    stats_summary = stats_summary.merge(
        measurement_count, how="right", on=category_cols
    )

    # Describe stats measurements

    measurement_stats = (
        measurement[~no_units]
        .groupby([*category_cols, unit_column])[[value_column]]
        .describe()
    )

    measurement_stats.columns = [
        "_".join(map(str, col)) for col in measurement_stats.columns
    ]

    measurement_stats = measurement_stats.reset_index()
    stats_summary = measurement_stats.merge(
        stats_summary, how="left", on=([*category_cols, unit_column])
    )

    # Count anomalies

    occurrences_to_count = {
        "range_high_anomaly_count": measurement[~no_units].range_high_anomaly,
        "range_low_anomaly_count": measurement[~no_units].range_low_anomaly,
    }

    for key, to_count in occurrences_to_count.items():
        additional_summary = (
            measurement[~no_units][to_count]
            .groupby([*category_cols, unit_column])[["measurement_id"]]
            .count()
            .rename(columns={"measurement_id": key})
            .reset_index()
        )
        stats_summary = stats_summary.merge(
            additional_summary, how="left", on=[*category_cols, unit_column]
        )

    stats_summary = stats_summary.fillna(0)
    stats_summary = stats_summary.set_index(
        [*category_cols, "no_units", unit_column]
    ).sort_index()
    stats_summary = stats_summary[
        [*stats_summary.columns[::-1][:3], *stats_summary.columns[:-3]]
    ]

    stats_summary = to("pandas", stats_summary)

    return stats_summary
