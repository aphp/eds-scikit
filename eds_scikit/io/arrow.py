import os

import pandas as pd
import pyarrow as pa


class arrowConnector:  # pragma: no cover
    def __init__(self, sql, database_name: str):
        self.database_name = database_name
        self.db = (
            sql(f"DESCRIBE DATABASE EXTENDED {database_name}")
            .filter("database_description_item=='Location'")
            .collect()[0]
            .database_description_value
        )

    def get_pd_fragment(
        self,
        table_name: str,
    ):

        self.path_table = os.path.join(self.db, table_name)

        # Import the parquet as ParquetDataset
        parquet_ds = pa.parquet.ParquetDataset(
            self.path_table, use_legacy_dataset=False
        )

        # Partitions of ds
        fragments = iter(parquet_ds.pieces)

        yield from fragments

    def get_pd_table(
        self,
        table_name=None,
        types_mapper=None,
        integer_object_nulls=True,
        date_as_object=False,
        person_ids=None,
    ):

        filtered = []
        for fragment in self.get_pd_fragment(table_name=table_name):
            table = fragment.to_table()

            # Import to pandas the fragment
            table_pd = table.to_pandas(
                types_mapper=types_mapper,
                integer_object_nulls=integer_object_nulls,
                date_as_object=date_as_object,
            )
            if (person_ids is not None) and ("person_id" in table_pd.columns):
                table_pd = table_pd[table_pd.person_id.isin(person_ids)]
            filtered.append(table_pd)

        return pd.concat(filtered)
