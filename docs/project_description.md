### Goal

EDS-Scikit is a tool to assist datascientists working on the AP-HP's Clinical Data Warehouse. It is specifically targeted for [OMOP-standardized](https://ohdsi.github.io/CommonDataModel/) data to:

- Ease access and analysis of data
- Allow a better transfer of knowledge between projects
- Improve research reproduciblity

### Main working principles

#### Dealing with various data sizes

Generally, data analysis can be done in two ways:

- **Locally**, by loading everything in RAM and working with e.g. [Pandas](https://pandas.pydata.org/docs/index.html)
- In a **distributed** fashion, when dealing with a lot of data, by using e.g. [Spark](https://spark.apache.org/)

While working with Pandas is often more convenient, its use can be problematic once working with large cohorts. Thus, making EDS-Scikit a Pandas-only library wasn't conceivable. In order to allow analysis to be conducted at scale, EDS-Scikit integrates with [Koalas](https://koalas.readthedocs.io/en/latest/).

!!! tip "Koalas"
     Koalas is a **library implementing Pandas API on top of Spark**. Basically, it allows for functions and methods developped for Pandas DataFrames to work on Spark DataFrames with close to no adjustments.

Let us see a dummy example where one wants to **count the number of visit occurrences per month**.


=== "Using Spark (via PySpark)"

     Suppose we have a **Spark** `visit_occurrence` DataFrame:
     ```python
     type(visit_occurrence_spark)
     # Out: pyspark.sql.dataframe.DataFrame
     ```



     ```python
     import pyspark.sql.functions as F

     def get_stats_spark(visit_occurrence):
         """
         Computes the number of visits per month

         Parameters
         ----------
         visit_occurrence : DataFrame

         Returns
         -------
         stats : pd.DataFrame
         """

         # Adding a month and year column
         visit_occurrence = (
             visit_occurrence
             .withColumn('year', F.year('visit_start_datetime'))
             .withColumn('month', F.month('visit_start_datetime'))
         )

         # Grouping and filtering
         stats = (
             visit_occurrence
             .groupby(["year","month"])
             .count()
             .filter((F.col("year") >= 2017))
             .toPandas()
         )

         return stats

     stats_from_spark = get_stats_spark(visit_occurrence_spark)
     ```

=== "Using Pandas"

     If the selected database contains few enough visits, we may have a `visit_occurrence` DataFrame small enough to fit in memory as a Pandas DataFrame.

     ```python
     type(visit_occurrence_pandas)
     # Out: pandas.core.frame.DataFrame
     ```

     Then run the same analysis:

     ```python
     def get_stats_pandas(visit_occurrence):
         """
         Computes the number of visits per month

         Parameters
         ----------
         visit_occurrence : DataFrame

         Returns
         -------
         stats : pd.DataFrame
         """

         # Adding a duration column
         visit_occurrence["year"] = visit_occurrence["visit_start_datetime"].dt.year
         visit_occurrence["month"] = visit_occurrence["visit_start_datetime"].dt.month

         # Grouping and filtering
         stats = (
             visit_occurrence
             .groupby(['year','month'])
             .visit_occurrence_id
             .count()
             .reset_index()
         )

         stats = stats[stats['year'] >= 2017]
         stats.columns = ['year','month','count']

         return stats

     stats_from_pandas = get_stats_pandas(visit_occurrence_pandas)
     ```

The two examples above clearly show the **syntax differences between using Pandas and using Spark**.

In order for a library to work both with Pandas and Spark, one would need to developp each function twice to accomodate for those two frameworks. Another problem might occur if you are dealing with a huge cohort, forcing you to do your final analysis in a distributed manner via Spark. In that scenario, you coudn't test your code on a small Pandas DataFrame subset.

The goal of **Koalas** is precisely to avoid this issue. It aims at allowing code to be written for Pandas DataFrames, and also run with (almost) no adjustements with Spark DataFrame:

```python
from databricks import koalas as ks

# Converting the Spark DataFrame into a Koalas DataFrame
visit_occurrence_koalas = visit_occurrence_spark.to_koalas()
```

!!! info
     The code above allows the DataFrame to stay distributed —as opposed to applying the `.toPandas()` method.

We can now use the function we designed for Pandas with a Koalas DataFrame:

```python
stats_from_koalas = get_stats_pandas(visit_occurrence_koalas)
```

Since we aggregated the data, its size is manageable so we can convert it back to Pandas for e.g. plotting

```python
stats_from_koalas = stats_from_koalas.to_pandas()
```

#### Concept

Most functions developped in the library implements a **concept**. For sake of clarity let us illustrate this notion with an example:

The function [`tag_icu_care_site()`][eds_scikit.icu.tag_icu_care_site] can be used to tag a care site as being an ICU or not. We say that it implements the concept `"IS_ICU"` because it **adds a column named `"IS_ICU"` to the input DataFrame**, as it can be seen from the docstring:

```python
"""
Returns
-------
care_site: DataFrame
    Dataframe with 1 added column corresponding to the following concept:
    - 'IS_ICU'
"""
```
This follows a **wide** data format. However, when multiple concepts are added at once, it might be done in a **long** format, such as with the [diabetes_from_icd10()][eds_scikit.event.diabetes_from_icd10] function, which stores the diabetes type in a `concept` column, and the corresponding ICD-10 code in a `value` column:

```python
"""
Returns
-------
DataFrame
    Event DataFrame in **long** format (with a `concept` and a `value` column).
    The `concept` column contains one of the following:
    - DIABETES_TYPE_I
    - DIABETES_TYPE_II
    - DIABETES_MALNUTRITION
    - DIABETES_IN_PREGNANCY
    - OTHER_DIABETES_MELLITUS
    - DIABETES_INSIPIDUS
    The `value` column contains the corresponding ICD-10 code that was extracted
"""
```

!!! question

     Check [this link](https://www.statology.org/long-vs-wide-data/) for a (very) quick explanation if you aren't familiar with **Long** vs **Wide** data format.

#### Algo

Most functions also have an argument called **`algo`**, which allows you to choose how a specific concept will be implemented in a function. Let's check the docstring of the same function [`tag_icu_care_site()`][eds_scikit.icu.tag_icu_care_site]:

```python
"""
Parameters
----------
care_site: DataFrame
algo: str
    Possible values are:
    - `"from_authorisation_type"`
    - `"from_regex_on_care_site_description"`
"""
```
The function's signature shows that `"from_authorisation_type"` is the default `algo`, used if the `algo` argument isn't filled by the user.

In the documentation, the different `"algo"` values will be displayed as tabs, along with a short description and optional algo-dependant parameters:

!!! algos "Availables algorithms (values for `"algo"`)"

    === "Algo 1 (default)"

        This `"algo"` is used by default.
        It does yadi yada.
        Specific parameters:

        - This first parameter
        - This second parameter
        - And also this third one

	=== "Algo 2"

	    This second `"algo"` works differently.
        It has no additional parameters

Please check the available `algos` when using a function from EDS-Scikit, to understand what each of them is doing and which one might fits you best.
