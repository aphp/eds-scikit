import os
from datetime import datetime
from shutil import rmtree
from typing import List, Tuple, Union

import altair as alt
import pandas as pd
from loguru import logger

from eds_scikit.biology.utils.concept_set import (
    ConceptsSet,
    fetch_all_concepts_set,
)

from eds_scikit.biology.viz_other.aggregate_measurement_table import aggregate_measurement
from eds_scikit.biology.viz.plot import plot_interactive_distribution
from eds_scikit.io import settings
from eds_scikit.utils.typing import Data, DataFrame

default_standard_terminologies = settings.standard_terminologies
default_standard_concept_regex = settings.standard_concept_regex


def plot_biology_summary(
    measurement: DataFrame,
    pd_limit_size: int = 100000,
    stats_only: bool = False,
) -> Union[alt.ConcatChart, pd.DataFrame]:
    """It aggregates, plots and saves all the concepts-sets in folders.


    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    pd_limit_size : int, optional
        The limit number of rows to convert [Koalas](https://koalas.readthedocs.io/en/latest/) DatFrame into [Pandas](https://pandas.pydata.org/) DataFrame
    stats_only : bool, optional
        If ``True``, it will only aggregate the data for the [summary table][summary-table].

    Returns
    -------
    List[alt.ConcatChart, pd.DataFrame]
        Altair plots describing the volumetric and the distribution properties of your biological data along with a pandas DataFrame with a statistical summary
    """
    
    tables = aggregate_measurement(measurement, pd_limit_size, stats_only, overall_only)
    
    
    
    
    
    
    
