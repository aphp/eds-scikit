# OMOP Teva - Quick use

This tutorial demonstrates how the OMOP teva module can be quickly used to generate OMOP tables dashboard.

Simply apply ```generate_omop_teva``` function after loading the data. It will create a directory with one HTML per OMOP table.

??? warning "It is recommended to run generate_omop_teva within spark-submit script"
    Koalas framework with high volumetry processing might cause computationnal delays and memory issues.

??? tip "Loading dataset"

    ```python
    from eds_scikit.io.hive import HiveData

    data = HiveData(
        spark_session=spark,
        database_name="project_xxxxxxxx",
        tables_to_load=[
            "care_site",
            "visit_occurrence",
            "concept",
            "concept_relationship",
            "note",
            "procedure_occurrence",
            "condition_occurrence",
            "drug_exposure_prescription",
            "drug_exposure_administration",
        ],
    )
    ```

```python
from eds_scikit.plot import generate_omop_teva

start_date, end_date = "2021-01-01", "2021-12-01"
generate_omop_teva(data=data, start_date=start_date, end_date=end_date)
```

=== "Visit occurrence"

    ``` vegalite
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
      "config": {
        "view": {
          "continuousHeight": 300,
          "continuousWidth": 300
        }
      },
      "data": {
        "name": "data-b12cdc97854a522ae1f1412cfb19ca93"
      },
      "datasets": {
        "data-b12cdc97854a522ae1f1412cfb19ca93": [
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2011-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2011-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2011-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2011-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2011-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2011-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2011-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2011-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2011-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2011-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2011-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 7.0,
            "datetime": "2012-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2012-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2012-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 9.0,
            "datetime": "2012-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 8.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2013-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2013-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2013-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2013-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2013-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2013-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2013-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 7.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2013-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2013-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2013-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 8.0,
            "datetime": "2013-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2013-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2014-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2014-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 7.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2014-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2014-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 16.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 8.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 13.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 11.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 11.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 12.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 11.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 11.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 8.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 7.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 13.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 8.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 8.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 7.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 8.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 12.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2017-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 11.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 6.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 8.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 12.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 11.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 13.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 6.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-08-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 12.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 5.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2018-10-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 11.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-11-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 5.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 8.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-01-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 4.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 6.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-02-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 10.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-04-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 7.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 4.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 7.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 10.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-05-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 9.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 10.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 4.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-06-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 8.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 3.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 2.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 9.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SSR",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 5.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 2.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "Psychiatrie",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-07-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "consultation"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 2.0,
            "datetime": "2019-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "stay_source_value": "MCO",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "urgences"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "stay_source_value": "SLD",
            "visit_occurrence_id": "not NaN",
            "visit_source_value": "hospitalis\u00e9s"
          }
        ]
      },
      "params": [
        {
          "bind": "legend",
          "name": "param_1",
          "select": {
            "clear": "dblclick",
            "fields": [
              "visit_occurrence_id"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_1"
          ]
        },
        {
          "bind": "legend",
          "name": "param_2",
          "select": {
            "clear": "dblclick",
            "fields": [
              "care_site_short_name"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_2"
          ]
        },
        {
          "bind": "legend",
          "name": "param_3",
          "select": {
            "clear": "dblclick",
            "fields": [
              "stay_source_value"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_3"
          ]
        },
        {
          "bind": "legend",
          "name": "param_4",
          "select": {
            "clear": "dblclick",
            "fields": [
              "visit_source_value"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_4"
          ]
        }
      ],
      "resolve": {
        "scale": {
          "color": "independent"
        }
      },
      "vconcat": [
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_1",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "visit_occurrence_id",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_1",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_2"
                          },
                          {
                            "param": "param_3"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_1",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_2"
                          },
                          {
                            "param": "param_3"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "visit_occurrence_id"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-2",
                      "H\u00f4pital-3",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_2",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "care_site_short_name",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_2",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_3"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-2",
                      "H\u00f4pital-3",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_2",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_3"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "care_site_short_name"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "stay_source_value",
                  "scale": {
                    "domain": [
                      "MCO",
                      "Psychiatrie",
                      "SLD",
                      "SSR"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c",
                      "#d62728"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_3",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "stay_source_value",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_3",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_2"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "stay_source_value",
                  "scale": {
                    "domain": [
                      "MCO",
                      "Psychiatrie",
                      "SLD",
                      "SSR"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c",
                      "#d62728"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_3",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_2"
                          }
                        ]
                      },
                      {
                        "param": "param_4"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "stay_source_value"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "visit_source_value",
                  "scale": {
                    "domain": [
                      "urgences",
                      "consultation",
                      "hospitalis\u00e9s"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_4",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "visit_source_value",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_4",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_2"
                          }
                        ]
                      },
                      {
                        "param": "param_3"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "visit_source_value",
                  "scale": {
                    "domain": [
                      "urgences",
                      "consultation",
                      "hospitalis\u00e9s"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_4",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_1"
                          },
                          {
                            "param": "param_2"
                          }
                        ]
                      },
                      {
                        "param": "param_3"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "visit_source_value"
        }
      ]
    }
    ```

=== "Note"

    ``` vegalite
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
      "config": {
        "view": {
          "continuousHeight": 300,
          "continuousWidth": 300
        }
      },
      "data": {
        "name": "data-bfebc373be24aab7da2ee0850998a9d7"
      },
      "datasets": {
        "data-bfebc373be24aab7da2ee0850998a9d7": [
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2011-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2012-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2012-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2013-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2014-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2014-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2014-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2014-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2014-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2014-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-01-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2015-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2015-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2015-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 3.0,
            "datetime": "2015-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2015-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2015-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 3.0,
            "datetime": "2015-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2015-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2015-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2015-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2015-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2015-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2015-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2015-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2015-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2015-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 2.0,
            "datetime": "2015-11-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2015-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-11-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2015-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2015-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2015-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2016-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2016-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2016-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2016-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2016-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2016-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2016-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2016-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2016-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2016-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2016-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2016-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2016-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2016-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2016-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 3.0,
            "datetime": "2016-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2016-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2016-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 25.0,
            "datetime": "2016-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2016-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 25.0,
            "datetime": "2016-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2016-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2016-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2016-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2016-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2016-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2016-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2016-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2016-09-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2016-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2016-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2016-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2016-10-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2016-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2016-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2016-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2016-11-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2016-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2016-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2016-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2016-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2017-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2017-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2017-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2017-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2017-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-02-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2017-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2017-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2017-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2017-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2017-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2017-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2017-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2017-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2017-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2017-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2017-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 29.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2017-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2017-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2017-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2017-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2018-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 23.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 24.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 24.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 23.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2018-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 25.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 30.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2018-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 23.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2018-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 28.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 32.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 33.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2018-09-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 22.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2018-10-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 22.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 22.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2018-11-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 23.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2018-12-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2019-01-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 19.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-02-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 6.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 7.0,
            "datetime": "2019-03-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 22.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 9.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2019-04-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 16.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 11.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 14.0,
            "datetime": "2019-05-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 18.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 17.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 20.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 5.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 8.0,
            "datetime": "2019-06-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 21.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 12.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 13.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "count": 15.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 10.0,
            "datetime": "2019-07-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 3.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "count": 4.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "CRH",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "LT",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "count": 1.0,
            "datetime": "2019-08-01T00:00:00",
            "note_class_source_value": "Other",
            "visit_occurrence_id": "not NaN"
          }
        ]
      },
      "params": [
        {
          "bind": "legend",
          "name": "param_9",
          "select": {
            "clear": "dblclick",
            "fields": [
              "visit_occurrence_id"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_9"
          ]
        },
        {
          "bind": "legend",
          "name": "param_10",
          "select": {
            "clear": "dblclick",
            "fields": [
              "care_site_short_name"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_10"
          ]
        },
        {
          "bind": "legend",
          "name": "param_11",
          "select": {
            "clear": "dblclick",
            "fields": [
              "note_class_source_value"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_11"
          ]
        },
        {
          "bind": "legend",
          "name": "param_12",
          "select": {
            "clear": "dblclick",
            "fields": [
              "cdm_source"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_12"
          ]
        }
      ],
      "resolve": {
        "scale": {
          "color": "independent"
        }
      },
      "vconcat": [
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_9",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "visit_occurrence_id",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_9",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_10"
                          },
                          {
                            "param": "param_11"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_9",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_10"
                          },
                          {
                            "param": "param_11"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "visit_occurrence_id"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-1",
                      "H\u00f4pital-2"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_10",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "care_site_short_name",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_10",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_11"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-1",
                      "H\u00f4pital-2"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_10",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_11"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "care_site_short_name"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "note_class_source_value",
                  "scale": {
                    "domain": [
                      "LT",
                      "Other",
                      "CRH"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_11",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "note_class_source_value",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_11",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_10"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "note_class_source_value",
                  "scale": {
                    "domain": [
                      "LT",
                      "Other",
                      "CRH"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_11",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_10"
                          }
                        ]
                      },
                      {
                        "param": "param_12"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "note_class_source_value"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_12",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "cdm_source",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_12",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_10"
                          }
                        ]
                      },
                      {
                        "param": "param_11"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_12",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_9"
                          },
                          {
                            "param": "param_10"
                          }
                        ]
                      },
                      {
                        "param": "param_11"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "cdm_source"
        }
      ]
    }
    ```

=== "Condition occurrence"
    ``` vegalite
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
      "config": {
        "view": {
          "continuousHeight": 300,
          "continuousWidth": 300
        }
      },
      "data": {
        "name": "data-2328446a20eab1cc715e10870b79500d"
      },
      "datasets": {
        "data-2328446a20eab1cc715e10870b79500d": [
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2011-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2011-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 30.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 44.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 26.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 27.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 3.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 47.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 31.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 39.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 29.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 56.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 46.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 3.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 3.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 53.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 38.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 61.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 65.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 27.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 67.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 57.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 43.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 27.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 35.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 40.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 33.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 39.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 37.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 40.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 34.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 35.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 50.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 42.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 39.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 33.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 43.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 29.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 53.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 31.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 68.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 26.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 33.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 70.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 26.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 72.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 39.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 34.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 41.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 48.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 47.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 43.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 51.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 31.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 54.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 46.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 37.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 34.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 48.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 30.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 64.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 71.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 52.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 44.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 33.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 43.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 34.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 41.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 51.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 27.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 40.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 26.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 50.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 48.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 15.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 62.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 59.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 38.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 4.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 7.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 29.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 41.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 45.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 50.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 45.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 38.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 77.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 46.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 74.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 22.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 30.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 78.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 27.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 49.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 49.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 80.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 34.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 33.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 69.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 46.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 76.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 9.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 12.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 30.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 51.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 48.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 37.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 18.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 59.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 26.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 54.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 29.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 46.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 39.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 10.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 31.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 17.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 38.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 21.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 53.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 44.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 13.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 19.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 51.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 28.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 40.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 25.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 63.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 38.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 32.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 35.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 75.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 36.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 8.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 11.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 24.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 44.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 16.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 14.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 23.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 20.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 3.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 6.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 5.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "not NaN",
            "count": 2.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "not NaN",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          }
        ]
      },
      "params": [
        {
          "bind": "legend",
          "name": "param_5",
          "select": {
            "clear": "dblclick",
            "fields": [
              "visit_occurrence_id"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_5"
          ]
        },
        {
          "bind": "legend",
          "name": "param_6",
          "select": {
            "clear": "dblclick",
            "fields": [
              "care_site_short_name"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_6"
          ]
        },
        {
          "bind": "legend",
          "name": "param_7",
          "select": {
            "clear": "dblclick",
            "fields": [
              "condition_source_value"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_7"
          ]
        },
        {
          "bind": "legend",
          "name": "param_8",
          "select": {
            "clear": "dblclick",
            "fields": [
              "cdm_source"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_8"
          ]
        }
      ],
      "resolve": {
        "scale": {
          "color": "independent"
        }
      },
      "vconcat": [
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_5",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "visit_occurrence_id",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_5",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_6"
                          },
                          {
                            "param": "param_7"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_5",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_6"
                          },
                          {
                            "param": "param_7"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "visit_occurrence_id"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-2",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_6",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "care_site_short_name",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_6",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_7"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-2",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_6",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_7"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "care_site_short_name"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "condition_source_value",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_7",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "condition_source_value",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_7",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_6"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "condition_source_value",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_7",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_6"
                          }
                        ]
                      },
                      {
                        "param": "param_8"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "condition_source_value"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "AREM",
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_8",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "cdm_source",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_8",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_6"
                          }
                        ]
                      },
                      {
                        "param": "param_7"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "AREM",
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_8",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_5"
                          },
                          {
                            "param": "param_6"
                          }
                        ]
                      },
                      {
                        "param": "param_7"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "cdm_source"
        }
      ]
    }
    ```

=== "Condition occurrence (diabete)"

    !!! warning "In this example ```condition_source_value``` is splited between diabetic and non-diabetic conditions."
        You can modify dashboard configuration by importing ```eds_scikit.plot.default_omop_teva_config``` and customizing it. See next section for details on how to do it.

    ```vegalite
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
      "config": {
        "view": {
          "continuousHeight": 300,
          "continuousWidth": 300
        }
      },
      "data": {
        "name": "data-1d0fd0ace6c43f5e025c5daf44a85809"
      },
      "datasets": {
        "data-1d0fd0ace6c43f5e025c5daf44a85809": [
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2011-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2011-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2011-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2011-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2011-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2011-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2011-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2011-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2011-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2012-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2012-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2012-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2012-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2012-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2012-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2012-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2012-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2012-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2012-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2012-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2012-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2013-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2013-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2013-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2013-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2013-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2013-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2013-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2013-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2013-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2013-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2013-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2013-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2014-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2014-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2014-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2014-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2014-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2014-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 27.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 20.0,
            "datetime": "2014-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2014-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2014-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2014-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2014-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 17.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2014-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 23.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 37.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2015-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 23.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 23.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2015-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 34.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2015-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2015-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 36.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 25.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 45.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 20.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2015-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 39.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 28.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 32.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 25.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2015-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 29.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2015-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 31.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 17.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 23.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2015-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2015-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 25.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2016-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 28.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 25.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2016-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 44.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 24.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 44.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 26.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2016-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 44.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 28.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2016-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 27.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2016-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2016-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 21.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 32.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 22.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2016-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 31.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2017-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2017-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 31.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 33.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 44.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 27.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 29.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 23.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2017-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2017-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 26.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 26.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 25.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 28.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 22.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 30.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2017-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 32.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 30.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 38.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 21.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2017-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2017-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2018-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2018-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 32.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 20.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2018-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 34.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 21.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 2.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2018-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 44.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 33.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 28.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2018-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 46.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 28.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2018-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 47.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 31.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 28.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 21.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2018-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 26.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 43.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 23.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 37.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2018-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 42.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 27.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 26.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 20.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 46.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 30.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2018-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 28.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 23.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2018-11-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 23.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2018-12-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 40.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 19.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 16.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 28.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 26.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 11.0,
            "datetime": "2019-01-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 32.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 7.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 17.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 14.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 17.0,
            "datetime": "2019-02-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 21.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 17.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 4.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2019-03-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 37.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 16.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 24.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 20.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2019-04-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 11.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 29.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 22.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 10.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 25.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 15.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 5.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2019-05-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 18.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 35.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 28.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 17.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 20.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 18.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 19.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2019-06-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 23.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 53.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 12.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 22.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 22.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 6.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 5.0,
            "datetime": "2019-07-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 15.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 31.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 9.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 13.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 13.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 7.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 10.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 8.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 9.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 6.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 14.0,
            "datetime": "2019-08-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 12.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-1",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 8.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 4.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 2.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "has_diabete",
            "count": 3.0,
            "datetime": "2019-09-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-2",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "ORBIS",
            "condition_source_value": "Other",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          },
          {
            "care_site_short_name": "H\u00f4pital-3",
            "cdm_source": "AREM",
            "condition_source_value": "has_diabete",
            "count": 1.0,
            "datetime": "2019-10-01T00:00:00",
            "visit_occurrence_id": "not NaN"
          }
        ]
      },
      "params": [
        {
          "bind": "legend",
          "name": "param_29",
          "select": {
            "clear": "dblclick",
            "fields": [
              "visit_occurrence_id"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_29"
          ]
        },
        {
          "bind": "legend",
          "name": "param_30",
          "select": {
            "clear": "dblclick",
            "fields": [
              "care_site_short_name"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_30"
          ]
        },
        {
          "bind": "legend",
          "name": "param_31",
          "select": {
            "clear": "dblclick",
            "fields": [
              "condition_source_value"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_31"
          ]
        },
        {
          "bind": "legend",
          "name": "param_32",
          "select": {
            "clear": "dblclick",
            "fields": [
              "cdm_source"
            ],
            "on": "click",
            "type": "point"
          },
          "views": [
            "view_32"
          ]
        }
      ],
      "resolve": {
        "scale": {
          "color": "independent"
        }
      },
      "vconcat": [
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_29",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "visit_occurrence_id",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_29",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_30"
                          },
                          {
                            "param": "param_31"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "visit_occurrence_id",
                  "scale": {
                    "domain": [
                      "not NaN"
                    ],
                    "range": [
                      "#1f77b4"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_29",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_30"
                          },
                          {
                            "param": "param_31"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "visit_occurrence_id"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-2",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_30",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "care_site_short_name",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_30",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_31"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "care_site_short_name",
                  "scale": {
                    "domain": [
                      "H\u00f4pital-3",
                      "H\u00f4pital-2",
                      "H\u00f4pital-1"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e",
                      "#2ca02c"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_30",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_31"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "care_site_short_name"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "condition_source_value",
                  "scale": {
                    "domain": [
                      "Other",
                      "has_diabete"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_31",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "condition_source_value",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_31",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_30"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "condition_source_value",
                  "scale": {
                    "domain": [
                      "Other",
                      "has_diabete"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_31",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_30"
                          }
                        ]
                      },
                      {
                        "param": "param_32"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "condition_source_value"
        },
        {
          "hconcat": [
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "AREM",
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_32",
                    "value": 1
                  },
                  "value": 0.3
                },
                "tooltip": [
                  {
                    "field": "cdm_source",
                    "type": "nominal"
                  }
                ],
                "x": {
                  "aggregate": "sum",
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "mark": {
                "type": "bar"
              },
              "name": "view_32",
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_30"
                          }
                        ]
                      },
                      {
                        "param": "param_31"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "encoding": {
                "color": {
                  "field": "cdm_source",
                  "scale": {
                    "domain": [
                      "AREM",
                      "ORBIS"
                    ],
                    "range": [
                      "#1f77b4",
                      "#ff7f0e"
                    ]
                  },
                  "type": "nominal"
                },
                "opacity": {
                  "condition": {
                    "param": "param_32",
                    "value": 1
                  },
                  "value": 0.3
                },
                "x": {
                  "field": "datetime",
                  "timeUnit": "yearmonth",
                  "type": "temporal"
                },
                "y": {
                  "aggregate": "sum",
                  "axis": {
                    "format": "s"
                  },
                  "field": "count",
                  "type": "quantitative"
                }
              },
              "height": 50,
              "mark": {
                "type": "line"
              },
              "transform": [
                {
                  "filter": {
                    "and": [
                      {
                        "and": [
                          {
                            "param": "param_29"
                          },
                          {
                            "param": "param_30"
                          }
                        ]
                      },
                      {
                        "param": "param_31"
                      }
                    ]
                  }
                }
              ],
              "width": 300
            }
          ],
          "title": "cdm_source"
        }
      ]
    }

    ```
