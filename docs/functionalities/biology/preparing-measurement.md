# Preparing measurement

This tutorial demonstrates the workflow to prepare measurement table.

!!! tip "Big volume"
    Measurement table can be large. Do not forget to set proper spark config before loading data.

## Mapping measurement table to ANABIO codes

### Defining Concept-Set

Here we work with the Glucose [pre-defined concept set](concepts_sets.md). See [quick-use](concepts_sets.md) for an example on how to create custom concept set.

```python

from eds_scikit.biology import prepare_measurement_table, ConceptsSet

glucose_blood = ConceptsSet("Glucose_Blood")

```

### Preparing measurement table

First, we prepare measurements with ```convert_units = False``` (we do not know which units are contained in the table yet).

```python

from eds_scikit.biology import measurement_values_summary

measurement = prepare_measurement_table(data, 
                                        start_date="2022-01-01", end_date="2022-05-01",
                                        concept_sets=[glucose_blood],
                                        convert_units=False, 
                                        get_all_terminologies=False
                                        )
```

### Statistical summary

A statistical summary by codes allows to get an insight on values distributions and detect possible heterogeneous units.

```python
from eds_scikit.biology import measurement_values_summary

stats_summary = measurement_values_summary(measurement, 
                                           category_cols=["concept_set", "GLIMS_ANABIO_concept_code"], 
                                           value_column="value_as_number",
                                           unit_column="unit_source_value")

stats_summary

```

|                   |       |     |         |   range_low_anomaly_count |   range_high_anomaly_count |   measurement_count |   value_as_number_count |   value_as_number_mean |   value_as_number_std |   value_as_number_min |   value_as_number_25% |   value_as_number_50% |   value_as_number_75% |   value_as_number_max |
|:------------------|:------|----:|:--------|--------------------------:|---------------------------:|--------------------:|------------------------:|-----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|
| Glucose_Blood | XXXXX | 100 | mmol/l |                       15 |                       5 |               1000 |                   1000 |                     5 |                    2 |                     0 |                    2 |                    5 |                    8 |                   9 |
| Glucose_Blood | YYYYY | 50 | mg/ml |                      20 |                       10 |               5000 |                   5000 |                     25 |                    10 |                     0 |                    20 |                    25 |                    37 |                   45 |
| Glucose_Blood | ZZZZZ |  10 | mmol/l |                       5 |                        18 |               1000 |                   1000 |                     6 |                    1 |                     0 |                    4 |                    6 |                    7 |                   10 |

### Units correction

To map all units to a common unit base we can use ```add_conversion``` and ```add_target_unit``` from ```ConceptSet``` class.

```python

glucose_blood.add_conversion("mol", "g", 180)
glucose_blood.add_target_unit("mmol/l")

```

We can check the new summary table after units conversion.

```python

stats_summary = measurement_values_summary(measurement, 
                                           category_cols=["concept_set", "GLIMS_ANABIO_concept_code"], 
                                           value_column="value_as_number_normalized",
                                           unit_column="unit_source_value_normalized")

stats_summary

```

|                   |       |     |         |   range_low_anomaly_count |   range_high_anomaly_count |   measurement_count |   value_as_number_count |   value_as_number_mean |   value_as_number_std |   value_as_number_min |   value_as_number_25% |   value_as_number_50% |   value_as_number_75% |   value_as_number_max |
|:------------------|:------|----:|:--------|--------------------------:|---------------------------:|--------------------:|------------------------:|-----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|
| Glucose_Blood | XXXXX | 100 | mmol/l |                       15 |                       5 |               1000 |                   1000 |                     5 |                    2 |                     0 |                    2 |                    5 |                    8 |                   9 |
| Glucose_Blood | YYYYY | 50 | mmol/l |                      20 |                       10 |               5000 |                   5000 |                     5 |                    2 |                     0 |                    4 |                    5 |                    7 |                   9 |
| Glucose_Blood | ZZZZZ |  10 | mmol/l |                       5 |                        18 |               1000 |                   1000 |                     6 |                    1 |                     0 |                    4 |                    6 |                    7 |                   10 |


## Plot summary

Once all units are homogeneous, we can generate more detailed dashboard for biology investigation.

```python
from eds_scikit.biology import plot_biology_summary

measurement = measurement.merge(data.visit_occurrence[["care_site_id", "visit_occurrence_id"]], on="visit_occurrence_id")
measurement = measurement.merge(data.care_site[["care_site_id", "care_site_short_name"]], on="care_site_id")

plot_biology_summary(measurement, value_column="value_as_number_normalized")

```

[Volumetry dashboard](../../_static/biology/viz/interactive_volumetry.html) 
[Distribution dashboard](../../_static/biology/viz/interactive_distribution.html)
