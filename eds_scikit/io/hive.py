import os
from typing import Dict, Iterable, List, Optional, Union

import pandas
from databricks import koalas
from loguru import logger
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import LongType, StructField, StructType

from . import settings

DataFrame = Union[koalas.DataFrame, pandas.DataFrame]


class HiveData:  # pragma: no cover
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
        tables_to_load : Optional[Union[Dict[str, Optional[List[str]]], List[str]]]
            By default (i.e. if ``tables_to_load is None``), loaded tables and columns loaded in each table are those listed
            [here][eds_scikit.io.settings.tables_to_load].
            A dictionnary can be provided to complement those default settings. Keys should be table names to load,
            and values should be:
            - ``None`` to load all columns
            - A list of columns to load (or to add to the default loaded columns if the table is already loaded by default)
            A list of the tables names can also be provided to load all columns of each table.
        columns_to_load : Optional[Union[Dict[str, Optional[List[str]]], List[str]]]
            *deprecated*

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
        my_person_ids = [9226726, 2092082, .... ]
        data = HiveData(spark_session=spark, database_name="edsomop_prod_a",
                            person_ids=my_person_ids)
        data.person["person_id"].count()
        # Out: 1000

        tables_to_save = ["person", "visit_occurrence"]
        data.persist_tables_to_folder(
            "./cohort_sample_1000",
            table_names=tables_to_save
        )
        # Out: writing /export/home/USER/cohort_sample_1000/person.parquet
        # Out: writing /export/home/USER/cohort_sample_1000/visit_occurrence.parquet
        # Out: ...
        ```

        """

        if columns_to_load and not tables_to_load:
            tables_to_load = columns_to_load
            logger.warning(
                "columns_to_load is a deprecated argument. Please use 'tables_to_load' instead."
            )
        self.spark_session = (
            spark_session
            if spark_session is not None
            else SparkSession.builder.enableHiveSupport().getOrCreate()
        )
        self.database_name = database_name
        self.person_ids = self._prepare_person_ids(person_ids)

        tmp_tables_to_load = settings.tables_to_load
        if isinstance(tables_to_load, dict):
            for table_name, columns in tables_to_load.items():
                if columns is None:
                    tmp_tables_to_load[table_name] = None
                else:
                    tmp_tables_to_load[table_name] = list(
                        set(tmp_tables_to_load.get(table_name, []) + columns)
                    )
        elif isinstance(tables_to_load, list):
            for table_name in tables_to_load:
                tmp_tables_to_load[table_name] = None

        self.tables_to_load = tmp_tables_to_load
        self.available_tables = self.list_available_tables()
        self._tables = {}

    def list_available_tables(self) -> List[str]:
        tables_df = self.spark_session.sql(
            f"SHOW TABLES IN {self.database_name}"
        ).toPandas()
        available_tables = [
            table_name
            for table_name in tables_df["tableName"].drop_duplicates().to_list()
            if table_name in self.tables_to_load.keys()
        ]
        return available_tables

    def rename_table(self, old_table_name: str, new_table_name: str) -> None:
        if old_table_name in self.available_tables:
            setattr(self, new_table_name, getattr(self, old_table_name))
            self.available_tables.remove(old_table_name)
            self.available_tables.append(new_table_name)
            logger.info("Table {} has been renamed {}", old_table_name, new_table_name)
        else:
            logger.info("Table {} is not available", old_table_name)

    def add_table(self, table_name: str, columns: List[str]) -> None:
        tables_df = self.spark_session.sql(
            f"SHOW TABLES IN {self.database_name}"
        ).toPandas()
        if table_name in tables_df["tableName"].drop_duplicates().to_list():
            self.tables_to_load[table_name] = list(
                set(self.tables_to_load.get(table_name, []) + columns)
            )
            self.available_tables = self.list_available_tables()
            logger.info("Table {} has been added", table_name)

    def _prepare_person_ids(self, list_of_person_ids) -> Optional[SparkDataFrame]:

        if list_of_person_ids is None:
            return None
        elif hasattr(list_of_person_ids, "to_list"):
            # Useful when list_of_person_ids are Koalas (or Pandas) Series
            unique_ids = set(list_of_person_ids.to_list())
        else:
            unique_ids = set(list_of_person_ids)

        print(f"Number of unique patients: {len(unique_ids)}")
        schema = StructType([StructField("person_id", LongType(), True)])

        filtering_df = self.spark_session.createDataFrame(
            [(int(p),) for p in unique_ids], schema=schema
        )
        return filtering_df

    def _read_table(self, table_name, person_ids=None) -> DataFrame:
        assert table_name in self.available_tables
        if person_ids is None and self.person_ids is not None:
            person_ids = self.person_ids

        df = self.spark_session.sql(f"select * from {self.database_name}.{table_name}")

        desired_columns = self.tables_to_load[table_name]
        selected_columns = (
            df.columns
            if desired_columns is None
            else [col for col in df.columns if col in desired_columns]
        )
        df = df.select(*selected_columns)

        if "person_id" in df.columns and person_ids is not None:
            df = df.join(person_ids, on="person_id", how="inner")

        return df.to_koalas()

    def persist_tables_to_folder(
        self,
        folder: str,
        person_ids: Optional[Iterable[int]] = None,
        tables: List[str] = None,
    ) -> None:
        """Save OMOP tables as parquet files in a given folder.

        Parameters
        ----------
        folder : str
            path to folder where the tables will be written.
        person_ids : iterable
            person_ids to keep in the subcohort
        tables : list of str, default None
            list of table names to save. Default value is
            :py:data:`~eds_scikit.io.settings.default_tables_to_save`

        """
        if tables is None:
            tables = settings.default_tables_to_save

        unknown_tables = [
            table for table in tables if table not in self.available_tables
        ]
        if unknown_tables:
            raise ValueError(
                f"The following tables are not available : {str(unknown_tables)}"
            )

        folder = os.path.abspath(folder)
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
            person_ids = self._prepare_person_ids(person_ids)

        for table in tables:
            filepath = os.path.join(folder, f"{table}.parquet")
            df = self._read_table(table, person_ids=person_ids)
            self._write_df_to_parquet(df, filepath)

    def _write_df_to_parquet(
        self,
        df: DataFrame,
        filepath: str,
    ) -> None:
        assert os.path.isabs(filepath)
        print(f"writing {filepath}")
        spark_filepath = "file://" + filepath
        df.to_parquet(spark_filepath, mode="overwrite")

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

    def __dir__(self) -> List[str]:
        return list(set(list(super().__dir__()) + self.available_tables))
