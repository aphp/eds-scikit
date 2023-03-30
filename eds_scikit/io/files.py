import os
from typing import List

import pandas as pd

from .base import BaseData


class PandasData(BaseData):  # pragma: no cover
    def __init__(
        self,
        folder: str,
    ):
        """Pandas interface to OMOP data stored as local parquet files/folders.


        Parameters
        ----------
        folder: str
            absolute path to a folder containing several parquet files with OMOP data

        Examples
        --------
        >>> data = PandasData(folder="/export/home/USER/my_data/")
        >>> person = data.person
        >>> person.shape
        (100, 10)

        """
        super().__init__()
        self.folder = folder
        self.available_tables = self.list_available_tables()
        self.tables_paths = self.get_table_path()
        if not self.available_tables:
            raise ValueError(f"Folder {folder} does not contain any parquet omop data.")

    def list_available_tables(self) -> List[str]:
        available_tables = []
        for filename in os.listdir(self.folder):
            table_name, extension = os.path.splitext(filename)
            if extension == ".parquet":
                available_tables.append(table_name)

        return available_tables

    def get_table_path(self) -> List[str]:
        tables_paths = {}
        for filename in os.listdir(self.folder):
            table_name, extension = os.path.splitext(filename)
            if extension == ".parquet":
                abspath = os.path.abspath(os.path.join(self.folder, filename))
                tables_paths[table_name] = abspath

        return tables_paths

    def _read_table(self, table_name: str) -> pd.DataFrame:
        path = self.tables_paths[table_name]
        return pd.read_parquet(path)

    def __getattr__(self, table_name: str) -> pd.DataFrame:
        if table_name in self.available_tables:
            return self._read_table(table_name)
        else:
            raise AttributeError(
                f"Table '{table_name}' does is not available in chosen folder."
            )
