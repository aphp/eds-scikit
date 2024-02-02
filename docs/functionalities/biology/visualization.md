# Visualization

This library provides a visualization tool that aggregates computed measurements to provide two interactive dashboards and a summary table describing various statistical properties of your biological data.

## Input

It expects a [Data](../../generic/io) object containing the following **OMOP** format tables:

- [Measurement](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:measurement)
- [Concept](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept)
- [Concept Relationship](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept_relationship)
- [Visit Occurrence](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:visit_occurrence)
- [Care Site](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:care_site)


!!!info "Measurement"
    The function can be used on raw data or on the transformed data returned by the [``bioclean`` function ](../cleaning).

```python
from eds_scikit.io import HiveData
from eds_scikit.biology import plot_biology_summary

db_name = "cse_xxxxxxx_xxxxxxx"
tables =  ["measurement", "concept", "concept_relationship", "visit_occurrence", "care_site"]

data = HiveData(db_name, tables_to_load=tables)

plot_biology_summary(data)
```
## Output

`plot_biology_summary()` creates a folder for each concepts-set. For instance, let us see what you will find in the folder *Glucose_Blood_Quantitative*`.

## Summary table

A statistical summary table as below:


--8<-- "_static/biology/viz/stats_summary.html"


## Volumetry dashboard

An interactive dashboard describing the volumety properties over time.

An example is available [here](../../_static/biology/viz/interactive_volumetry.html).


## Distribution dashboard

An interactive dashboard describing the distribution properties.

An example is available [here](../../_static/biology/viz/interactive_distribution.html).
