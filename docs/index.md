---
ᴴₒᴴₒᴴₒ: true
---

<p align="center">
  <img src="_static/scikit_logo_text.png" alt="eds-scikit" width="50%">
</p>

# Getting started

eds-scikit is a tool to assist data scientists working on the AP-HP’s Clinical Data Warehouse. It is specifically targeted for [OMOP-standardized data](https://ohdsi.github.io/CommonDataModel/) to:

   - Ease access and analysis of data

   - Allow a better transfer of knowledge between projects

   - Improve research reproduciblity

As an example, the following figure was obtained using various functionalities from eds-scikit.

<figure markdown>
  [![Image title](_static/introduction_image.svg){ .off-glb }](functionalities/generic/introduction.ipynb)
  <figcaption></figcaption>
</figure>

!!! question "How was it done ?"
      Click on the figure above to jump to the tutorial using various functionalities from eds-scikit, or continue reading the introduction!

## Quick start

### Installation

!!! Warning "Requirements"
    eds-scikit stands on the shoulders of [Spark 2.4](https://spark.apache.org/docs/2.4.8/index.html) which runs on [Java 8](https://www.oracle.com/java/technologies/java8.html) and [Python](https://www.python.org/) ~3.7.1. **If you work on AP-HP's CDW, those requirements are already fulfilled, so please disregard the following steps.** Else, it is essential to:

    - Install a version of Python ≥ 3.7.1 and < 3.8.
    - Install [OpenJDK 8](https://openjdk.org/projects/jdk8/), an open-source reference implementation of Java 8 wit the following command lines:

        === "Linux (Debian, Ubunutu, etc.)"
            <div class="termy">
            ```console
            $ sudo apt-get update
            $ sudo apt-get install openjdk-8-jdk
            ---> 100%
            ```
            </div>

            For more details, check this [installation guide](https://www.geofis.org/en/install/install-on-linux/install-openjdk-8-on-ubuntu-trusty/)

        === "Mac"
            <div class="termy">
            ```console
            $ brew tap AdoptOpenJDK/openjdk
            $ brew install --cask adoptopenjdk8
            ---> 100%
            ```
            </div>

            For more details, check this [installation guide](https://installvirtual.com/install-openjdk-8-on-mac-using-brew-adoptopenjdk/)

        === "Windows"

            Follow this [installation guide](https://techoral.com/blog/java/openjdk-install-windows.html)

You can install eds-scikit by cloning the git repository:

<div class="termy">

```console
$ pip install eds-scikit
---> 100%
color:green Successfully installed eds_scikit !
```

</div>

!!! danger "Improving performances on distributed data"
      It is highly recommanded (but not mandatory) to use the helper function `eds_scikit.improve_performances` to optimaly configure PySpark and Koalas. You can simply call
      ```python
      import eds_scikit
      spark, sc, sql = eds_scikit.improve_performances()
      ```
      The function will return

      - A `SparkSession`
      - A `SparkContext`
      - An `sql` function to execute *SQL* queries


### A first example: Merging visits together

Let's tackle a common problem when dealing with clinical data: Merging close/consecutive visits into **stays**.
As detailled in [the dedicated section](), eds-scikit is expecting to work with [Pandas](https://pandas.pydata.org/) or [Koalas](https://koalas.readthedocs.io/en/latest/) DataFrames.  We provide various connectors to facilitate data fetching, namely a [Hive]() connector and a [Postgres]() connector


=== "Using a Hive DataBase"

    ```python
    from eds_scikit.io import HiveData

    data = HiveData(DB_NAME)
    visit_occurrence = data.visit_occurrence # (1)
    ```

    1. With this connector, `visit_occurrence` will be a *Pandas* DataFrame

=== "Using a Postgres DataBase"

    ```python
    from eds_scikit.io import PostgresData

    DB_NAME = "my_db"
    SCHEMA = "my_schema"
    USER = "my_username"
    data = PostgresData(DB_NAME, schema=SCHEMA, user=USER) # (1)
    visit_occurrence = data.visit_occurrence # (2)
    ```

    1. This connector expects a `.pgpass` file storing the connection parameters
    2. With this connector, `visit_occurrence` will be a *Pandas* DataFrame

=== "Else"

    ``` markdown title="You can use eds-scikit with data from any source, as long as:"
    - It follows the OMOP format
    - It is a Pandas or Koalas DataFrame
    ```
    ```python
    import pandas as pd
    visit_occurrence = pd.read_csv("./data/visit_occurrence.csv")
    ```

??? summary "`visit_occurrence`"

     For the sake of the example, only **columns of interest** are shown here.

     |      | visit_occurrence_id | person_id | visit_start_datetime | visit_end_datetime  | visit_source_value | row_status_source_value | care_site_id |
     | ---: | :------------------ | --------: | :------------------- | :------------------ | :----------------- | :---------------------- | -----------: |
     |    0 | A                   |       999 | 2021-01-01 00:00:00  | 2021-01-05 00:00:00 | hospitalisés       | courant                 |            1 |
     |    1 | B                   |       999 | 2021-01-04 00:00:00  | 2021-01-08 00:00:00 | hospitalisés       | courant                 |            1 |
     |    2 | C                   |       999 | 2021-01-12 00:00:00  | 2021-01-18 00:00:00 | hospitalisés       | courant                 |            1 |
     |    3 | D                   |       999 | 2021-01-13 00:00:00  | 2021-01-14 00:00:00 | urgence            | courant                 |            1 |
     |    4 | E                   |       999 | 2021-01-19 00:00:00  | 2021-01-21 00:00:00 | hospitalisés       | courant                 |            2 |
     |    5 | F                   |       999 | 2021-01-25 00:00:00  | 2021-01-27 00:00:00 | hospitalisés       | supprimé                |            1 |
     |    6 | G                   |       999 | 2017-01-01 00:00:00  | NaT                 | hospitalisés       | courant                 |            1 |

```python
# Importing the desired functions:

from eds_scikit.period.stays import merge_visits, get_stays_duration

# Calling the first function: computing stays

visit_occurrence = merge_visits(visit_occurrence)
```

As you can see, the function added a `STAY_ID` concept, grouping visits together

??? summary "`visit_occurrence[["visit_occurrence_id","STAY_ID"]]`"

     |      | visit_occurrence_id | STAY_ID |
     | ---: | :------------------ | :------ |
     |    0 | A                   | A       |
     |    1 | B                   | A       |
     |    2 | C                   | C       |
     |    3 | D                   | C       |
     |    4 | E                   | E       |
     |    5 | F                   | F       |
     |    6 | G                   | G       |

```python
# Calling the second function: computing stays duration
stays = get_stays_duration(visit_occurrence, missing_end_date_handling="coerce")
```

Here, each stay duration was calculated, dealing with potential overlaps and inclusions.:

??? summary "`stays`"

     | STAY_ID | t_start             | t_end               | STAY_DURATION |
     | ------: | :------------------ | :------------------ | ------------: |
     |       A | 2021-01-01 00:00:00 | 2021-01-08 00:00:00 |           168 |
     |       C | 2021-01-12 00:00:00 | 2021-01-18 00:00:00 |           144 |
     |       E | 2021-01-19 00:00:00 | 2021-01-21 00:00:00 |            48 |
     |       F | 2021-01-25 00:00:00 | 2021-01-27 00:00:00 |            48 |
     |       G | 2017-01-01 00:00:00 | NaT                 |           NaN |


!!! tip "About the code above"
     As you noticed, the pipeline above is fairly straightforward, needing only the `visit_occurrence` DataFrame as input.
     However, it is also highly customizable, and you should always look into all the various availables options for the functions you're  using.  For instance, the following parameters could have been used:

     ```python
     visit_occurrence = merge_visits(
        visit_occurrence,
        remove_deleted_visits=True,
        long_stay_threshold=timedelta(days=365),
        long_stay_filtering="all",
        max_timedelta=timedelta(hours=24),
        merge_different_hospitals=False,
        merge_different_source_values=["hospitalisés", "urgence"],
     )

     stays = get_stays_duration(
        visit_occurrence,
        algo="sum_of_visits_duration",
        missing_end_date_handling="coerce"
     )
     ```

### A word about AP-HP

#### Specifics of AP-HP CDW
eds-scikit was developped by AP-HP's Data Science team with the help of [Inria's Soda](https://team.inria.fr/soda/) team. As such, it is especially well fitted for AP-HP's Data Warehouse. In this doc, **we use the following card to mention information that might be useful when using eds-scikit with AP-HP's data**:

!!! aphp "Some information"
      Here, we might for instance suggest some parameters for a function that should be used given AP-HP's data.

#### EDS-NLP
Also, a rule-based NLP library ([EDS-NLP](https://github.com/aphp/edsnlp)) designed to work on clinical texts was developped in parallel with eds-scikit. We decided not to include EDS-NLP as a dependency. Still, some functions might require an input *à la `note_nlp`*: For instance, the current function designed to extract consultation dates from a `visit_occurrence` car work either on structured data only or with dates extracted in text and compiled in a DataFrame.

**You are free to use the method of your choice to get this DataFrame**, as long as it contains the necessary columns as mentionned in the documentation. Note that **we mention with the following card the availability of an EDS-NLP dedicated pipeline**:

!!! edsnlp "A dedicated pipe"
      For the example above, a [consultation date](https://aphp.github.io/edsnlp/latest/pipelines/misc/consultation-dates/) pipeline exists.
      Moreover, [methods are available](https://aphp.github.io/edsnlp/latest/tutorials/multiple-texts/) to run an EDS-NLP pipeline on a Pandas, Spark or even Koalas DataFrame !

## Contributing to eds-scikit

We welcome contributions! Fork the project and create a pull request. Take a look at the [dedicated page](contributing.md) for details.

## Citation

If you use `eds-scikit`, please cite us as below.

```bibtex
@misc{eds-scikit,
    author = {Petit-Jean, Thomas and Remaki, Adam and Maladière, Vincent and Varoquaux, Gaël and Bey, Romain},
    doi = {10.5281/zenodo.7401549},
    title = {eds-scikit: data analysis on OMOP databases},
    url = {https://github.com/aphp/eds-scikit}
}
```
