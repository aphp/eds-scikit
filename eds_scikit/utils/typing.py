from typing import Union

import pandas
from databricks import koalas

from eds_scikit.io import HiveData, PandasData, PostgresData

DataFrame = Union[koalas.DataFrame, pandas.DataFrame]
Series = Union[koalas.Series, pandas.Series]
DataObject = Union[DataFrame, Series]
Data = Union[HiveData, PostgresData, PandasData]
