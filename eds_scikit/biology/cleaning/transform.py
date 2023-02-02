from loguru import logger

from eds_scikit.biology.utils.process_measurement import normalize_unit
from eds_scikit.resources import registry
from eds_scikit.utils.framework import get_framework, to
from eds_scikit.utils.typing import DataFrame


def transform_measurement(
    measurement: DataFrame, clip: bool = False, config_name: str = "all_aphp"
) -> DataFrame:
    """Normalize units and flag outliers based on the configuration file

    Parameters
    ----------
    measurement : DataFrame
        Target DataFrame to transform
    clip : bool, optional
        If `True` extreme values are set equal to the thresholds
    config_name : str, optional
        Name of the configuration file

    Returns
    -------
    DataFrame
        Transformed DataFrame with normalized units and flagged outliers
    """
    concept_code_cols = [
        column_name
        for column_name in measurement.columns
        if "concept_code" in column_name
    ]

    config = registry.get("data", f"get_biology_config.{config_name}")()
    config = config[
        concept_code_cols
        + [
            "unit_source_value",
            "max_threshold",
            "min_threshold",
            "transformed_unit",
            "Action",
            "Coefficient",
        ]
    ]

    config = to(get_framework(measurement), config)

    logger.info("Normalizing units...")
    clean_measurement = normalize_unit(measurement)
    clean_measurement = clean_measurement.merge(
        config, on=concept_code_cols + ["unit_source_value"]
    )
    clean_measurement = clean_measurement[~(clean_measurement["Action"] == "Delete")]
    clean_measurement["transformed_value"] = clean_measurement["value_as_number"].mask(
        clean_measurement["Action"] == "Transform",
        clean_measurement["value_as_number"] * clean_measurement["Coefficient"],
    )
    clean_measurement["max_threshold"] = clean_measurement["max_threshold"].mask(
        clean_measurement["Action"] == "Transform",
        clean_measurement["max_threshold"] * clean_measurement["Coefficient"],
    )
    clean_measurement["min_threshold"] = clean_measurement["min_threshold"].mask(
        clean_measurement["Action"] == "Transform",
        clean_measurement["min_threshold"] * clean_measurement["Coefficient"],
    )
    clean_measurement = clean_measurement.drop(columns=["Action", "Coefficient"])

    logger.info("Flagging outliers...")
    clean_measurement["outlier"] = False
    clean_measurement["outlier"] = clean_measurement.outlier.mask(
        (clean_measurement["transformed_value"] > clean_measurement["max_threshold"])
        | (clean_measurement["transformed_value"] < clean_measurement["min_threshold"]),
        True,
    )

    if clip:
        logger.info("Clipping extreme values...")
        clean_measurement[
            "transformed_value"
        ] = clean_measurement.transformed_value.mask(
            clean_measurement["transformed_value"]
            >= clean_measurement["max_threshold"],
            clean_measurement["max_threshold"],
        )
        clean_measurement[
            "transformed_value"
        ] = clean_measurement.transformed_value.mask(
            clean_measurement["transformed_value"]
            <= clean_measurement["min_threshold"],
            clean_measurement["min_threshold"],
        )

    return clean_measurement
