"""Top-level package for eds_scikit."""

__author__ = """eds_scikit"""
__version__ = "0.1.8"

import warnings

warnings.simplefilter(
    action="ignore", category=FutureWarning
)  # Remove pyarrow DeprecatedWarning

import importlib
import os
import pathlib
import time
from packaging import version
from typing import List, Tuple
from pathlib import Path

import pandas as pd
import pyspark
from loguru import logger
from pyspark import SparkContext
from pyspark.sql import SparkSession

import eds_scikit.biology  # noqa: F401 --> To register functions
from eds_scikit.io import improve_performances, pyarrow_fix

# Remove SettingWithCopyWarning
pd.options.mode.chained_assignment = None

pyarrow_fix()

logger.warning(
    """To improve performances when using Spark and Koalas, please call `eds_scikit.improve_performances()`
This function optimally configures Spark. Use it as:
`spark, sc, sql = eds_scikit.improve_performances()`
The functions respectively returns a SparkSession, a SparkContext and an sql method"""
)
