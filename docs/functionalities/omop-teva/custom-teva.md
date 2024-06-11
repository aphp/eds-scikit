# Custom Teva

OMOP-Teva module can also be applied to any dataframe. User must use ```reduce_table``` and ```visualize_table``` from ```eds_scikit.plot.table_viz```.

<figure markdown>
  [![Image title](omop_teva.png)](#)
  <figcaption></figcaption>
</figure>

!!! warning "Make sure to specify categorical columns with less then 50 values."
    Use the function ```eds_scikit.plot.table_viz.map_column``` to reduce columns volumetry.

??? tip "Creating synthetic dataset"

    ```python
    import numpy as np
    import pandas as pd

    data = pd.DataFrame(
        {
            "id": str(np.arange(1, 1001)),
            "category_1": np.random.choice(["A", "B", "C"], size=1000, p=[0.4, 0.3, 0.3]),
            "category_2": np.array([str(i) for i in range(500)] * 2),
            "location": np.random.choice(
                ["location 1", "location 2"], size=1000, p=[0.6, 0.4]
            ),
            "date": pd.to_datetime(
                np.random.choice(
                    pd.date_range(start="2021-01-01", end="2022-01-01"), size=1000
                )
            ),
        }
    )
    ```

```python
from eds_scikit.plot import reduce_table, visualize_table

data_reduced = reduce_table(
    data,
    category_columns=["location", "category_1", "category_2"],
    date_column="date",
    start_date="2021-01-01",
    end_date="2021-12-01",
    mapper={"category_2": {"even": r"[02468]$", "odd": r"[13579]$"}},
)

chart = visualize_table(
    data_reduced, title="synthetic dataframe table", description=True
)
```

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
    "name": "data-6c8e9658b16d48f64ac39e6b052cf917"
  },
  "datasets": {
    "data-6c8e9658b16d48f64ac39e6b052cf917": [
      {
        "category_1": "A",
        "category_2": "even",
        "count": 8,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 11,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 11,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 12,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 4,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 8,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-01-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 11,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-02-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 12,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 13,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 11,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 10,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 13,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-03-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 11,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 12,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 2,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 2,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-04-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 18,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 8,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 10,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 11,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 2,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 1,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-05-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 11,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 13,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 2,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 2,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 3,
        "datetime": "2021-06-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 10,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 4,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 1,
        "datetime": "2021-07-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 7,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 2,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 1,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 4,
        "datetime": "2021-08-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 12,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 12,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 3,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 4,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 4,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-09-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 10,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 9,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 5,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 8,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 3,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 9,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 3,
        "datetime": "2021-10-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 8,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 13,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 14,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 8,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 6,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 10,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 7,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "odd",
        "count": 6,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 4,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "even",
        "count": 5,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "C",
        "category_2": "odd",
        "count": 1,
        "datetime": "2021-11-01T00:00:00",
        "location": "location 2"
      },
      {
        "category_1": "A",
        "category_2": "even",
        "count": 1,
        "datetime": "2021-12-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "even",
        "count": 1,
        "datetime": "2021-12-01T00:00:00",
        "location": "location 1"
      },
      {
        "category_1": "B",
        "category_2": "odd",
        "count": 1,
        "datetime": "2021-12-01T00:00:00",
        "location": "location 2"
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
      "name": "param_41",
      "select": {
        "clear": "dblclick",
        "fields": [
          "location"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_41"
      ]
    },
    {
      "bind": "legend",
      "name": "param_42",
      "select": {
        "clear": "dblclick",
        "fields": [
          "category_1"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_42"
      ]
    },
    {
      "bind": "legend",
      "name": "param_43",
      "select": {
        "clear": "dblclick",
        "fields": [
          "category_2"
        ],
        "on": "click",
        "type": "point"
      },
      "views": [
        "view_43"
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
      "synthetic dataframe table"
    ]
  },
  "vconcat": [
    {
      "hconcat": [
        {
          "encoding": {
            "color": {
              "field": "location",
              "scale": {
                "domain": [
                  "location 1",
                  "location 2"
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
                "param": "param_41",
                "value": 1
              },
              "value": 0.3
            },
            "tooltip": [
              {
                "field": "location",
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
          "name": "view_41",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "param": "param_42"
                  },
                  {
                    "param": "param_43"
                  }
                ]
              }
            }
          ]
        },
        {
          "encoding": {
            "color": {
              "field": "location",
              "scale": {
                "domain": [
                  "location 1",
                  "location 2"
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
                "param": "param_41",
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
                    "param": "param_42"
                  },
                  {
                    "param": "param_43"
                  }
                ]
              }
            }
          ],
          "width": 300
        }
      ],
      "title": "location"
    },
    {
      "hconcat": [
        {
          "encoding": {
            "color": {
              "field": "category_1",
              "scale": {
                "domain": [
                  "A",
                  "B",
                  "C"
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
                "param": "param_42",
                "value": 1
              },
              "value": 0.3
            },
            "tooltip": [
              {
                "field": "category_1",
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
          "name": "view_42",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "param": "param_41"
                  },
                  {
                    "param": "param_43"
                  }
                ]
              }
            }
          ]
        },
        {
          "encoding": {
            "color": {
              "field": "category_1",
              "scale": {
                "domain": [
                  "A",
                  "B",
                  "C"
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
                "param": "param_42",
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
                    "param": "param_41"
                  },
                  {
                    "param": "param_43"
                  }
                ]
              }
            }
          ],
          "width": 300
        }
      ],
      "title": "category_1"
    },
    {
      "hconcat": [
        {
          "encoding": {
            "color": {
              "field": "category_2",
              "scale": {
                "domain": [
                  "even",
                  "odd"
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
                "param": "param_43",
                "value": 1
              },
              "value": 0.3
            },
            "tooltip": [
              {
                "field": "category_2",
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
          "name": "view_43",
          "transform": [
            {
              "filter": {
                "and": [
                  {
                    "param": "param_41"
                  },
                  {
                    "param": "param_42"
                  }
                ]
              }
            }
          ]
        },
        {
          "encoding": {
            "color": {
              "field": "category_2",
              "scale": {
                "domain": [
                  "even",
                  "odd"
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
                "param": "param_43",
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
                    "param": "param_41"
                  },
                  {
                    "param": "param_42"
                  }
                ]
              }
            }
          ],
          "width": 300
        }
      ],
      "title": "category_2"
    }
  ]
}
```
