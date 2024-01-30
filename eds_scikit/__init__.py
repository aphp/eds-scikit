"""Top-level package for eds_scikit."""

__author__ = """eds_scikit"""
__version__ = "0.1.6"

import warnings

warnings.simplefilter(
    action="ignore", category=FutureWarning
)  # Remove pyarrow DeprecatedWarning


import pandas as pd
from loguru import logger
from .io import koalas_options, improve_performances

# Remove SettingWithCopyWarning
pd.options.mode.chained_assignment = None

logger.warning(
    """To improve performances when using Spark and Koalas, please call `eds_scikit.improve_performances()`
This function optimally configures Spark. Use it as:
`spark, sc, sql = eds_scikit.improve_performances()`
The functions respectively returns a SparkSession, a SparkContext and an sql method"""
)

koalas_options()
