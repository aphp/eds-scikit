import os
from typing import List, Tuple

import pandas as pd


class PandasData:  # pragma: no cover
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

        self.available_tables, self.tables_paths = self.list_available_tables(folder)
        if not self.available_tables:
            raise ValueError(f"Folder {folder} does not contain any parquet omop data.")

    @staticmethod
    def list_available_tables(folder: str) -> Tuple[List[str], List[str]]:
        available_tables = []
        tables_paths = {}
        for filename in os.listdir(folder):
            table_name, extension = os.path.splitext(filename)
            if extension == ".parquet":
                abspath = os.path.abspath(os.path.join(folder, filename))
                tables_paths[table_name] = abspath
                available_tables.append(table_name)

        return available_tables, tables_paths

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

    def __dir__(self) -> List[str]:
        return list(super().__dir__()) + list(self.available_tables)
