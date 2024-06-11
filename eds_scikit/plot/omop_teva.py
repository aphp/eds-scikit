import os
import pickle

from loguru import logger

from eds_scikit.io import HiveData
from eds_scikit.io.omop_teva_default_config import default_omop_teva_config
from eds_scikit.plot.table_viz import reduce_table, visualize_table


def save_pickle(path: str, obj):
    with open(path, "wb") as outp:
        pickle.dump(obj, outp)


def generate_omop_teva(
    data: HiveData,
    start_date: str,
    end_date: str,
    teva_config: dict = default_omop_teva_config,
    output_dir="omop_teva",
):
    """
    Generate OMOP TEVA folder.

    Parameters
    ----------
    data : HiveData
        Must contain the visit_occurrence table.
    start_date : str
        The start date for data extraction.
    end_date : str
        The end date for data extraction.
    teva_config : dict, optional
        OMOP TEVA configuration, by default `default_omop_teva_config`. Must start with visit_occurrence configuration.
    output_dir : str, optional
        Output directory path, by default "omop_teva".

    Examples
    --------
    Example configuration for `teva_config`:

    default_omop_teva_config = {
        "visit_occurrence": {
            "category_columns": [
                "visit_occurrence_id",
                "care_site_short_name",
                "stay_source_value"
            ],
            "date_column": "visit_start_datetime",
            "mapper": {
                "visit_occurrence_id": {"not NaN": ".*"}
            }
        },
        "other_table": {
            "category_columns": [
                "visit_occurrence_id",
                "column A",
                "column B",
                "column C"
            ],
            "date_column": "column_datetime",
            "mapper": {
                "column A": {"not NaN": ".*"},
                "column B": {"X type": "X.*", "Y type": "Y"}
            }
        }
        ...
    }
    """
    if not os.path.exists(f"{output_dir}/"):
        os.makedirs(f"{output_dir}/")

    # First, preprocess visit_occurrence which will be merged with remaining config tables
    try:
        visit_occurrence = data.visit_occurrence
        visit_occurrence = visit_occurrence.merge(
            data.care_site[["care_site_id", "care_site_short_name"]], on="care_site_id"
        )
        teva_config["visit_occurrence"]
    except AttributeError:
        raise Exception(
            "No visit_occurrence or care_site table in input data object. visit_occurrence and care_site table must be provided."
        )

    # Iterate config tables
    for table_name, config in teva_config.items():

        logger.info(f"Starting {table_name} processing.")

        if table_name == "visit_occurrence":
            visit_columns = [
                *config["category_columns"],
                config["date_column"],
                "visit_occurrence_id",
            ]
            visit_columns = list(
                set(visit_columns).intersection(visit_occurrence.columns)
            )
            visit_occurrence = visit_occurrence[visit_columns]
            table = visit_occurrence.copy()
        else:
            try:
                table = data._read_table(table_name)
                drop_columns = (
                    set(visit_occurrence.columns).intersection(table.columns)
                ).difference(["visit_occurrence_id"])
                if drop_columns:
                    table = table.merge(
                        visit_occurrence.drop(columns=drop_columns),
                        on="visit_occurrence_id",
                        how="left",
                    )
                else:
                    table = table.merge(
                        visit_occurrence, on="visit_occurrence_id", how="left"
                    )
            except AttributeError:
                logger.warning(
                    f"No {table_name} table in input data object. Skipping {table_name}."
                )
                continue
        # Compute reduced table representation
        table["visit_occurrence_id"] = table["visit_occurrence_id"].astype(str)

        table_count = reduce_table(
            table, start_date=start_date, end_date=end_date, **config
        )
        table_count = table_count[~(table_count == 0).any(axis=1)]
        # Compute associated chart
        chart = visualize_table(table_count, title=f"{table_name} table dashboard")
        # Save computations
        save_pickle(f"{output_dir}/{table_name}_count", table_count)
        chart.save(f"{output_dir}/{table_name}_chart.html")
        logger.info(f"{table_name} processing done.")
