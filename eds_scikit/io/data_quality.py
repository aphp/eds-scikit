import pandas as pd
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, when


def clean_dates(df: DataFrame) -> DataFrame:
    dates = [
        col for col, dtype in df.dtypes if dtype in {"date", "datetime", "timestamp"}
    ]
    for date in dates:
        df = df.withColumn(
            date,
            when(
                (col(date) > pd.Timestamp.max) | (col(date) < pd.Timestamp.min), None
            ).otherwise(col(date)),
        )
    return df
