import glob
from pathlib import Path
from typing import List

import pandas as pd
from importlib_metadata import os
from loguru import logger

from eds_scikit.biology.utils.process_concepts import ConceptsSet
from eds_scikit.resources import registry

CONFIGS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "user_configs"))


def create_config_from_stats(
    concepts_sets: List[ConceptsSet],
    config_name: str,
    stats_folder: str = "Biology_summary",
):
    """Generate the configuration file from a statistical summary. It is needed [here][eds_scikit.biology.cleaning.transform.transform_measurement]

    Parameters
    ----------
    concepts_sets : List[ConceptsSet]
        List of concepts-sets to select
    config_name : str
        Name of the folder where the configuration will be saved.
    stats_folder : str
        Name of the statistical summary folder
    """
    my_custom_config = pd.DataFrame()
    for concepts_set in concepts_sets:
        try:
            stats = pd.read_pickle(
                "{}/{}/measurement_stats.pkl".format(stats_folder, concepts_set.name)
            )
            stats["transformed_unit"] = (
                stats.groupby("unit_source_value")["count"]
                .sum("count")
                .sort_values(ascending=False)
                .index[0]
            )
            stats["concepts_set"] = concepts_set.name
            stats["Action"] = None
            stats["Coefficient"] = None

            my_custom_config = pd.concat([my_custom_config, stats])
        except OSError:
            logger.error(
                "{} has no statistical summary saved in {}",
                concepts_set.name,
                stats_folder,
            )
            pass

    if "care_site_short_name" in my_custom_config.columns:
        # Keep only the row computed from every care site
        my_custom_config = my_custom_config[
            my_custom_config.care_site_short_name == "ALL"
        ]

    os.makedirs(CONFIGS_PATH, exist_ok=True)

    my_custom_config.to_csv("{}/{}.csv".format(CONFIGS_PATH, config_name), index=False)

    register_configs()

    # datasets.add_dataset(my_custom_config, config_name)
    # reload(datasets)


def register_configs():
    for config in glob.glob(os.path.join(CONFIGS_PATH, "*.csv")):
        config_name = Path(config).stem
        registry.data.register(
            f"get_biology_config.{config_name}",
            func=lambda: pd.read_csv(config),
        )


def list_all_configs() -> List[str]:
    """
    Helper to get the names of all saved biology configurations

    Returns
    -------
    List[str]
        The configurations names
    """
    registered = list(registry.data.get_all().keys())
    configs = [
        r.split(".")[-1] for r in registered if r.startswith("get_biology_config")
    ]
    return configs
