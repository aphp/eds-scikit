import os
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Union

import pandas as pd
import pyarrow.parquet as pq
import pyspark.sql.functions as F
import pyspark.sql.types as T
from databricks import koalas
from loguru import logger
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import LongType, StructField, StructType

from eds_scikit.utils.framework import cache

from . import settings
from .base import BaseData
from .data_quality import clean_dates
from .i2b2_mapping import get_i2b2_table

DataFrame = Union[koalas.DataFrame, pd.DataFrame]


class HiveData(BaseData):  # pragma: no cover
    def __init__(
        self,
        database_name: str,
        spark_session: Optional[SparkSession] = None,
        person_ids: Optional[Iterable[int]] = None,
        tables_to_load: Optional[
            Union[Dict[str, Optional[List[str]]], List[str]]
        ] = None,
        columns_to_load: Optional[
            Union[Dict[str, Optional[List[str]]], List[str]]
        ] = None,
        database_type: Optional[str] = "OMOP",
        prune_omop_date_columns: bool = True,
        cache: bool = True,
    ):
        """Spark interface for OMOP data stored in a Hive database.

        This class provides a simple access to data stored in Hive.
        Data is returned as koalas dataframes that match the tables
        stored in Hive.

        Parameters
        ----------
        database_name : str
            The name of you database in Hive. Ex: "cse_82727572"
        spark_session : pyspark.sql.SparkSession
            If None, a SparkSession will be retrieved or  created via `SparkSession.builder.enableHiveSupport().getOrCreate()`
        person_ids : Optional[Iterable[int]]
            An iterable of `person_id` that is used to define a subset of the database.
        tables_to_load : dict, default=None
            *deprecated*
        columns_to_load : dict, default=None
            *deprecated*
        database_type: Optional[str] = 'OMOP'. Must be 'OMOP' or 'I2B2'
            Whether to use the native OMOP schema or to convert I2B2 inputs to OMOP.
        prune_omop_date_columns: bool, default=True
            In OMOP, most date values are stored both in a `<str>_date` and `<str>_datetime` column
            Koalas has trouble handling the `date` time, so we only keep the `datetime` column
        cache: bool, default=True
            Whether to cache each table after preprocessing or not.
            Will speed-up subsequent calculations, but can be long/infeasable for very large tables

        Attributes
        ----------
        person : koalas dataframe
            Hive data for table `person` as a koalas dataframe.
            Other OMOP tables can also be accessed as attributes
        available_tables : list of str
            names of OMOP tables that can be accessed as attributes with this
            HiveData object.

        Examples
        --------

        ```python
        data = HiveData(database_name="edsomop_prod_a")
        data.available_tables
        # Out: ["person", "care_site", "condition_occurrence", ... ]

        person = data.person
        type(person)
        # Out: databricks.koalas.frame.DataFrame

        person["person_id"].count()
        # Out: 12670874
        ```

        This class can be used to create a subset of data for a given
        list of `person_id`. This is useful because the smaller dataset
        can then be used to prototype more rapidly.

        ```python
        my_person_ids = [9226726, 2092082, ...]
        data = HiveData(
            spark_session=spark, database_name="edsomop_prod_a", person_ids=my_person_ids
        )
        data.person["person_id"].count()
        # Out: 1000

        tables_to_save = ["person", "visit_occurrence"]
        data.persist_tables_to_folder("./cohort_sample_1000", table_names=tables_to_save)
        # Out: writing /export/home/USER/cohort_sample_1000/person.parquet
        # Out: writing /export/home/USER/cohort_sample_1000/visit_occurrence.parquet
        # Out: ...
        ```

        """
        super().__init__()

        if columns_to_load is not None:
            logger.warning("'columns_to_load' is deprecated and won't be used")

        if tables_to_load is not None:
            logger.warning("'tables_to_load' is deprecated and won't be used")

        self.spark_session = (
            spark_session or SparkSession.builder.enableHiveSupport().getOrCreate()
        )
        self.database_name = database_name
        if database_type not in ["I2B2", "OMOP"]:
            raise ValueError(
                f"`database_type` must be either 'I2B2' or 'OMOP'. Got {database_type}"
            )
        self.database_type = database_type

        if self.database_type == "I2B2":
            self.database_source = "cse" if "cse" in self.database_name else "edsprod"
            self.omop_to_i2b2 = settings.i2b2_tables[self.database_source]
            self.i2b2_to_omop = defaultdict(list)
            for omop_table, i2b2_table in self.omop_to_i2b2.items():
                self.i2b2_to_omop[i2b2_table].append(omop_table)

        self.prune_omop_date_columns = prune_omop_date_columns
        self.cache = cache
        self.user = os.environ["USER"]
        self.person_ids, self.person_ids_df = self._prepare_person_ids(person_ids)
        self.available_tables = self.list_available_tables()
        self._tables = {}

    @property
    def tables_to_load(self):
        logger.warning(
            "'tables_to_load' is deprecated and will be removed in futur version"
        )
        return settings.tables_to_load

    def list_available_tables(self) -> List[str]:
        tables_df = self.spark_session.sql(
            f"SHOW TABLES IN {self.database_name}"
        ).toPandas()
        session_tables = tables_df["tableName"].drop_duplicates().to_list()

        if self.database_type == "I2B2":
            available_tables = set()
            for table_name in session_tables:
                omop_tables = self.i2b2_to_omop.get(table_name, [])
                for omop_table in omop_tables:
                    available_tables.add(omop_table)
            return list(available_tables)

        return session_tables

    def rename_table(self, old_table_name: str, new_table_name: str) -> None:
        # TODO: use _tables dict instead of self to store tables?
        if old_table_name in self.available_tables:
            setattr(self, new_table_name, getattr(self, old_table_name))
            self.available_tables.remove(old_table_name)
            self.available_tables.append(new_table_name)
            logger.info("Table {} has been renamed {}", old_table_name, new_table_name)
        else:
            logger.info("Table {} is not available", old_table_name)

    def add_table(self, table_name: str, columns: List[str]) -> None:
        logger.warning("'add_table' is deprecated and won't be used")
        return

    def _prepare_person_ids(
        self, person_ids, return_df: bool = True
    ) -> Optional[SparkDataFrame]:

        if person_ids is None:
            return (None, None) if return_df else None
        elif hasattr(person_ids, "to_list"):
            # Useful when list_of_person_ids are Koalas (or Pandas) Series
            unique_ids = set(person_ids.to_list())
        else:
            unique_ids = set(person_ids)

        if not return_df:
            return unique_ids

        schema = StructType([StructField("person_id", LongType(), True)])

        filtering_df = self.spark_session.createDataFrame(
            [(int(p),) for p in unique_ids], schema=schema
        ).cache()

        logger.info(f"Number of unique patients: {filtering_df.count()}")

        return unique_ids, filtering_df

    def _read_table(
        self,
        table_name,
        person_ids=None,
        to_koalas: Optional[bool] = None,
    ) -> DataFrame:

        if to_koalas:
            logger.warning("'to_koalas' is deprecated and won't be used")

        if table_name not in self.available_tables:
            raise ValueError(
                f"{table_name} is not available. "
                f"Available tables are: {self.available_tables}"
            )

        if self.database_type == "OMOP":
            df = self.spark_session.sql(
                f"select * from {self.database_name}.{table_name}"
            )
        else:
            df = get_i2b2_table(
                spark_session=self.spark_session,
                db_name=self.database_name,
                db_source=self.database_source,
                table=table_name,
            )

        person_ids = person_ids or self.person_ids_df
        if "person_id" in df.columns and person_ids is not None:
            df = df.join(person_ids, on="person_id", how="inner")

        if self.prune_omop_date_columns:

            # Keeping only _datetime column if corresponding _date exists
            cols = [
                c
                for c in df.columns
                if not ((c.endswith("_date") and (f"{c}time" in df.columns)))
            ]
            df = df.select(cols)

            # Casting the single _date columns to timestamp:
            for col in df.schema:
                if col.dataType == T.DateType():
                    df = df.withColumn(col.name, F.col(col.name).cast("timestamp"))
        df = df.to_koalas()

        df = clean_dates(df)

        if self.cache:
            df = cache(df)

        return df

    def persist_tables_to_folder(
        self,
        folder: str,
        person_ids: Optional[Iterable[int]] = None,
        tables: List[str] = None,
        overwrite: bool = False,
    ) -> None:
        """Save OMOP tables as parquet files in a given folder.

        Parameters
        ----------
        folder : str
            path to folder where the tables will be written.

        person_ids : iterable
            person_ids to keep in the subcohort.

        tables : list of str, default None
            list of table names to save. Default value is
            :py:data:`~eds_scikit.io.settings.default_tables_to_save`.

        overwrite : bool, default=False
            whether to overwrite files if 'folder' already exists.

        """
        # Manage tables
        if tables is None:
            tables = settings.default_tables_to_save

        unknown_tables = [
            table for table in tables if table not in self.available_tables
        ]
        if unknown_tables:
            raise ValueError(
                f"The following tables are not available : {str(unknown_tables)}"
            )

        # Create folder
        folder = Path(folder).absolute()

        if folder.exists() and overwrite:
            shutil.rmtree(folder)

        folder.mkdir(parents=True, mode=0o766)

        assert os.path.exists(folder) and os.path.isdir(
            folder
        ), f"Folder {folder} not found."

        # TODO: remove everything in this folder that is a valid
        # omop table. This prevents a user from having a
        # folder containing datasets generated from different
        # patient subsets.

        # TODO: maybe check how much the user wants to persist
        # to disk. Set a limit on the number of patients in the cohort ?

        if person_ids is not None:
            person_ids = self._prepare_person_ids(person_ids, return_df=False)

        database_path = self.get_db_path()

        for idx, table in enumerate(tables):
            if self.database_type == "I2B2":
                table_path = self._hdfs_write_orc_to_parquet(
                    table, person_ids, overwrite
                )
            else:
                table_path = os.path.join(database_path, table)

            df = self.get_table_from_parquet(table_path, person_ids=person_ids)

            local_file_path = os.path.join(folder, f"{table}.parquet")
            df.to_parquet(
                local_file_path,
                allow_truncated_timestamps=True,
                coerce_timestamps="ms",
            )
            logger.info(
                f"({idx+1}/{len(tables)}) Table {table} saved at "
                f"{local_file_path} (N={len(df)})."
            )

    def get_table_from_parquet(
        self,
        table_path,
        types_mapper=None,
        integer_object_nulls=True,
        date_as_object=False,
        person_ids=None,
    ):
        parquet_ds = pq.ParquetDataset(table_path, use_legacy_dataset=False)
        fragments = parquet_ds.pieces

        filtered = []
        for fragment in fragments:
            table = fragment.to_table()
            df = table.to_pandas(
                types_mapper=types_mapper,
                integer_object_nulls=integer_object_nulls,
                date_as_object=date_as_object,
            )
            if (person_ids is not None) and ("person_id" in df.columns):
                df = df[df.person_id.isin(person_ids)]
            # XXX: This behaviour can raise OOM errors and
            # will be updated in subsequent versions.
            filtered.append(df)

        return pd.concat(filtered)

    def get_db_path(self):
        """Get the HDFS path of the database"""
        return (
            self.spark_session.sql(f"DESCRIBE DATABASE EXTENDED {self.database_name}")
            .filter("database_description_item=='Location'")
            .collect()[0]
            .database_description_value
        )

    def _hdfs_write_orc_to_parquet(self, table, person_ids, overwrite):
        table_df = self._read_table(table)
        if "person_id" in table_df.columns and person_ids is not None:
            table_df = table_df[table_df.person_id.isin(person_ids)]

        table_path = os.path.join(f"hdfs://bbsedsi/user/{self.user}", table)
        mode = "overwrite" if overwrite else "error"
        try:
            table_df.to_parquet(table_path, mode=mode)
        except:  # noqa E722
            logger.info("Using existing ")
            pass  # data already exists
        return table_path

    def __getattr__(self, table_name: str) -> DataFrame:
        if table_name in self._tables:
            return self._tables[table_name]
        elif table_name in self.available_tables:
            # Add to cache dictionnary during the first call.
            table = self._read_table(table_name)
            self._tables[table_name] = table
            return table
        else:
            raise AttributeError(f"Table '{table_name}' unknown")
