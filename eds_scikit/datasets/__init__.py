import os
from typing import List

import pandas as pd

from .synthetic.hierarchy import load_hierarchy
from .synthetic.icd10 import load_icd10
from .synthetic.ccam import load_ccam
from .synthetic.consultation_dates import load_consultation_dates
from .synthetic.visit_merging import load_visit_merging
from .synthetic.stay_duration import load_stay_duration
from .synthetic.suicide_attempt import load_suicide_attempt
from .synthetic.tagging import load_tagging
from .synthetic.biology import load_biology_data

known_datasets = [
    filename.split(".")[0]
    for filename in os.listdir(os.path.dirname(__file__))
    if filename.endswith("csv")
]


__all__ = [
    load_ccam,
    load_consultation_dates,
    load_hierarchy,
    load_icd10,
    load_visit_merging,
    load_stay_duration,
    load_suicide_attempt,
    load_tagging,
    load_biology_data,
]


def __dir__():
    return known_datasets + [func.__name__ for func in __all__]


def __getattr__(att):
    dataset_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), att + ".csv")
    )
    if os.path.isfile(dataset_path):
        return pd.read_csv(dataset_path)
    else:
        raise AttributeError(f"Unknown dataset: {att}")


def add_dataset(table: pd.DataFrame, name: str):
    dataset_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), name + ".csv")
    )
    table.to_csv(dataset_path, index=False)


def list_all_synthetics() -> List[str]:
    """
    Helper to list all available synthetic datasets

    Returns
    -------
    List[str]
        List of datasets names
    """
    return [func.__name__ for func in __all__]
