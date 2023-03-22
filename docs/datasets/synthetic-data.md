# Small Datasets for testing functionalities

## Presentation

eds-scikit was build to work seamlessly on a pre-existing OMOP database. However, the library also provides some *toy datasets* so that you can try out some features even without having access to a database.

## Usage

First, you can display all availables synthetic datasets:

```python
from eds_scikit import datasets
datasets.list_all_synthetics()
# Out: ['load_ccam', 'load_consultation_dates', 'load_hierarchy', 'load_icd10', 'load_visit_merging', 'load_stay_duration', 'load_suicide_attempt', 'load_tagging', 'load_biology_data', 'load_event_sequences']
```

To load a specific dataset, simply run:

```python
data = datasets.load_icd10()
data
# Out: ICD10Dataset(condition_occurrence, visit_occurrence)
```

The `data` object is similar to objects available in [eds_scikit.io][io-getting-data], namely:

- [HiveData][eds_scikit.io.HiveData]
- [PostgresData][eds_scikit.io.PostgresData]
- [PandasData][eds_scikit.io.PandasData]

For instance, tables are available as attributes:

```python
data.condition_occurrence
# Out:   person_id condition_source_value condition_start_datetime condition_status_source_value  visit_occurrence_id
0          1                    C10               2010-01-01                            DP                   11
1          1                   E112               2010-01-01                           DAS                   12
2          1                    D20               2012-01-01                           DAS                   13
3          1                    A20               2020-01-01                            DP                   14
4          1                    A21               2000-01-01                            DP                   15
5          1                    X20               2000-01-01                            DP                   16
6          1                    C10               2010-01-01                            DP                   16
7          1                    C10               2010-01-01                            DP                   17
```

As shown in the [tutorial][using-icd-10-and-ccam], you can now try out the corresponding [`conditions_from_icd10()`][eds_scikit.event.icd10.conditions_from_icd10] function.
