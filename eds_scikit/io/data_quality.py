import pandas as pd
from pyspark.sql import DataFrame


def clean_dates(df: DataFrame) -> DataFrame:
    date_types = ["datetime", "datetimetz", "datetime64"]
    date_cols = df.select_dtypes(date_types).columns
    for col in date_cols:
        mask_date_invalid = (df[col] > pd.Timestamp.max) | (
            df[col] < pd.Timestamp(1900, 1, 1)
        )
        df.loc[mask_date_invalid, col] = None
    return df
