# Visualizing measurements

Once the measurement table has been computed, biology module provides ```measurement_values_summary``` and ```plot_biology_summary``` to gain better insights into their distribution and volumetry across codes, care sites, and time.

## Statistical summary

```measurement_values_summary``` generates useful statistics to identify anomalies in measurements associated with a concept set.

```python
from eds_scikit.biology import measurement_values_summary

stats_summary = measurement_values_summary(
    measurement,
    category_cols=[
        "concept_set",
        "GLIMS_ANABIO_concept_code",
        "GLIMS_LOINC_concept_code",
    ],
    value_column="value_as_number",
    unit_column="unit_source_value",
)

stats_summary
```

| concept_set | ANABIO_concept_code | no_units | unit_source_value |   range_low_anomaly_count |   range_high_anomaly_count |   measurement_count |   value_as_number_count |   value_as_number_mean |   value_as_number_std |   value_as_number_min |   value_as_number_25% |   value_as_number_50% |   value_as_number_75% |   value_as_number_max |
|:------------------|:------|----:|:--------|--------------------------:|---------------------------:|--------------------:|------------------------:|-----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|----------------------:|
| Custom_Leukocytes | A0174 | 148 | x10*9/l |                       813 |                       1099 |               11857 |                   11857 |                     21 |                    18 |                     0 |                    25 |                    50 |                    75 |                   100 |
| Custom_Leukocytes | C8824 | 121 | x10*9/l |                      1166 |                       1196 |               11821 |                   11821 |                     20 |                    20 |                     0 |                    25 |                    50 |                    75 |                   100 |
| Custom_Leukocytes | C9784 |  83 | x10*9/l |                       935 |                        902 |               11082 |                   11082 |                     10 |                    16 |                     0 |                    25 |                    50 |                    75 |                   100 |


## Plot summary

```plot_biology_summary``` generates a useful dashboard to better understand the volumetry and distribution of codes within the same concept set. The purpose is to identify and correct possible biases associated with sets of codes, time periods, or specific care sites.

```python
from eds_scikit.biology import plot_biology_summary

# First add 'care_site_short_name' column to measurement table
measurement = measurement.merge(
    data.visit_occurrence[["care_site_id", "visit_occurrence_id"]],
    on="visit_occurrence_id",
)
measurement = measurement.merge(
    data.care_site[["care_site_id", "care_site_short_name"]], on="care_site_id"
)

plot_biology_summary(measurement, value_column="value_as_number")
```

[Volumetry dashboard](../../_static/biology/viz/interactive_volumetry.html)
[Distribution dashboard](../../_static/biology/viz/interactive_distribution.html)
