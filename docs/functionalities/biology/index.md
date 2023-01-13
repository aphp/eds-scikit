# Biology


The biology module of [eds-scikit](https://github.com/aphp/eds-scikit) supports data scientists working on biological data. Its main objectives are to:

- Extract meaningful biological parameters from biological raw data for data analysis
- Manage outliers
- Provide data visualization tools

## Quick start

This is just a quick overview of what you can do with the biology module.

### 1. Load your data

First, you need to load your data. As detailed in [the dedicated section](../generic/io), eds-scikit is expecting to work with [Pandas](https://pandas.pydata.org/) or [Koalas](https://koalas.readthedocs.io/en/latest/) DataFrames.  We provide various connectors to facilitate data fetching, namely a [Hive](../generic/io/#loading-from-hive-hivedata) connector, a [Postgres](../generic/io/#loading-from-postgres-postgresdata) connector and a [Pandas](../generic/io/#persistingreading-a-sample-tofrom-disk-pandasdata) connector.

!!!danger "Big cohort"
    If your cohort size is big, we highly recommend the [Hive](../generic/io/#loading-from-hive-hivedata) connector.

=== "Using a Hive DataBase"

    ```python
    from eds_scikit.io import HiveData

    db_name = "cse_xxxxxxx_xxxxxxx" # (1)
    tables =  [
        "care_site",
        "concept",
        "concept_relationship",
        "measurement",
        "visit_occurrence",
    ]

    data = HiveData(db_name, tables_to_load=tables) # (2)
    ```

    1. The data must be in OMOP format
    2. Tables are loaded as *Koalas* DataFrames

=== "Using a Postgres DataBase"

    ```python
    from eds_scikit.io import PostgresData

    db_name = "cse_xxxxxxx_xxxxxxx"
    schema = "my_schema"
    user = "my_username"

    data = PostgresData(db_name, schema=schema, user=user) # (1)
    ```

    1. This connector expects a `.pgpass` file storing the connection parameters

=== "Using a local Pandas DataBase"

    ```python
    from eds_scikit.io import PandasData

    folder = "my_folder_path"

    data = PandasData(folder)
    ```

### 2. Clean the measurements


```python
from eds_scikit.biology import bioclean

bioclean(data, start_date="2020-01-01", end_date="2021-12-31")

data.bioclean.head()
```
| concepts_set               | LOINC_concept_code | LOINC_concept_name | AnaBio_concept_code | AnaBio_concept_name  | transformed_unit | transformed_value | max_threshold | min_threshold | outlier | value_source_value | unit_source_value |
| :------------------------- | :----------------- | :----------------- | :------------------ | :------------------- | :--------------- | :---------------- | :------------ | :------------ | :------ | :----------------- | :---------------- |
| EntityA_Blood_Quantitative | 000-0              | EntityA #Bld       | A0000               | EntityA_Blood        | x10*9/l          | 115               | 190           | 0             | False   | 115 x10*9/l        | x10*9/l           |
| EntityA_Blood_Quantitative | 000-1              | EntityA_Blood_Vol  | A0001               | EntityA_Blood_g/l    | x10*9/l          | 220               | 190           | 0             | True    | 560 g/l            | g/l               |
| EntityB_Blood_Quantitative | 001-0              | EntityB_Blood      | B0000               | EntityB_Blood_artery | mmol             | 0.45              | 8.548         | 0.542         | True    | 0.45 mmol          | mmol              |
| EntityB_Blood_Quantitative | 001-0              | EntityB_Blood      | B0001               | EntityB_Blood_vein   | mmol             | 4.52              | 8.548         | 0.542         | False   | 4.52 mmol          | mmol              |
| EntityB_Blood_Quantitative | 000-1              | EntityB Bld Auto   | B0002               | EntityB_Blood_µg/l   | mmol             | 9.58              | 8.548         | 0.542         | True    | 3587 µg/l          | µg/l              |

For more details, have a look on [the dedicated section](cleaning).

### 3. Visualize statistical summary


```python
from eds_scikit.biology import plot_biology_summary

plot_biology_summary(data)
```

It creates a folder with different plots for each [concepts-set](cleaning/#definitions). For more details, have a look on [the dedicated section](visualization).
