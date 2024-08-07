# OMOP Teva example

The dashboard below provides an example of OMOP Teva dashboard for the __visit_occurrence__ table.

??? question "Explore this dashboard to identify any abnormal data distributions that could lead to bias."
    __Solution :__ The Psychological department at care site 1 appears to produce unusual NaN values after June.

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
  "config": {
    "legend": {
      "columns": 4,
      "symbolLimit": 0
    },
    "view": {
      "continuousHeight": 300,
      "continuousWidth": 300
    }
  },
  "data": {
    "name": "data-8ebd6cc9cd8e33a2c58b3179f42f592a"
  },
  "datasets": {
    "data-8ebd6cc9cd8e33a2c58b3179f42f592a": [
      {
        "care_site_short_name": "care site 1",
        "count": 12,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 5,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 5,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 4,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 6,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 10,
        "datetime": "2021-01-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 9,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 10,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-02-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 4,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-03-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 5,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 4,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 7,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-04-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 12,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 5,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 9,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 4,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-05-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 9,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 14,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-06-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 3,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 12,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 8,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 13,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 14,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 10,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 7,
        "datetime": "2021-08-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 10,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 5,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 21,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 7,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 6,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-09-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 11,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 10,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 13,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 19,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 5,
        "datetime": "2021-10-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 2,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 8,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 17,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 7,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 6,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 10,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 2,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 3,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 2",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "MCO",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 4,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "consult"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 2,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      },
      {
        "care_site_short_name": "care site 3",
        "count": 3,
        "datetime": "2021-11-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-12-01T00:00:00",
        "stay_source_value": "Other",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "hospit"
      },
      {
        "care_site_short_name": "care site 1",
        "count": 1,
        "datetime": "2021-12-01T00:00:00",
        "stay_source_value": "PSY",
        "visit_occurrence_id": "not NaN",
        "visit_source_value": "NaN"
      }
    ]
  },
  "padding": {
    "bottom": 50,
    "left": 50,
    "right": 50,
    "top": 50
  },
  "params": [
    {
      "bind": "legend",
      "name": "param_17",
      "select": {
        "clear": "dblclick",
        "fields": [
          "visit_occurrence_id"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_17"
      ]
    },
    {
      "bind": "legend",
      "name": "param_18",
      "select": {
        "clear": "dblclick",
        "fields": [
          "care_site_short_name"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_18"
      ]
    },
    {
      "bind": "legend",
      "name": "param_19",
      "select": {
        "clear": "dblclick",
        "fields": [
          "stay_source_value"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_19"
      ]
    },
    {
      "bind": "legend",
      "name": "param_20",
      "select": {
        "clear": "dblclick",
        "fields": [
          "visit_source_value"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_20"
      ]
    }
  ],
  "resolve": {
    "scale": {
      "color": "independent"
    }
  },
  "title": {
    "fontSize": 25,
    "offset": 30,
    "subtitle": [
      "ALT + SHIFT to select multiple categories",
      "Double-click on legend to unselect",
      "Reduce table column and values size for better interactivity"
    ],
    "subtitleFontSize": 15,
    "subtitlePadding": 20,
    "text": [
      "visit_occurrence table"
    ]
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
                "param": "param_17",
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
          "name": "view_17",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "and": [
                      {
                        "param": "param_18"
                      },
                      {
                        "param": "param_19"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                "param": "param_17",
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
                        "param": "param_18"
                      },
                      {
                        "param": "param_19"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                  "care site 1",
                  "care site 2",
                  "care site 3"
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
                "param": "param_18",
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
          "name": "view_18",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "and": [
                      {
                        "param": "param_17"
                      },
                      {
                        "param": "param_19"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                  "care site 1",
                  "care site 2",
                  "care site 3"
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
                "param": "param_18",
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
                        "param": "param_17"
                      },
                      {
                        "param": "param_19"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                  "Other",
                  "PSY"
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
                "param": "param_19",
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
          "name": "view_19",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "and": [
                      {
                        "param": "param_17"
                      },
                      {
                        "param": "param_18"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                  "Other",
                  "PSY"
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
                "param": "param_19",
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
                        "param": "param_17"
                      },
                      {
                        "param": "param_18"
                      }
                    ]
                  },
                  {
                    "param": "param_20"
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
                  "consult",
                  "hospit",
                  "NaN"
                ],
                "range": [
                  "#1f77b4",
                  "#ff7f0e",
                  "black"
                ]
              },
              "type": "nominal"
            },
            "opacity": {
              "condition": {
                "param": "param_20",
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
          "name": "view_20",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "and": [
                      {
                        "param": "param_17"
                      },
                      {
                        "param": "param_18"
                      }
                    ]
                  },
                  {
                    "param": "param_19"
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
                  "consult",
                  "hospit",
                  "NaN"
                ],
                "range": [
                  "#1f77b4",
                  "#ff7f0e",
                  "black"
                ]
              },
              "type": "nominal"
            },
            "opacity": {
              "condition": {
                "param": "param_20",
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
                        "param": "param_17"
                      },
                      {
                        "param": "param_18"
                      }
                    ]
                  },
                  {
                    "param": "param_19"
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
