# Visualizing age pyramid

The age pyramid is helpful to quickly visualize the age and gender distributions in a cohort.

## Load a synthetic dataset

`plot_age_pyramid` uses the "person" table:

```python
from eds_scikit.datasets.synthetic.person import load_person

df_person = load_person()
df_person.head()
```
|   | person_id | gender_source_value | birth_datetime |
|---|-----------|---------------------|----------------|
| 0 | 0         | m                   | 2010-01-01     |
| 1 | 1         | m                   | 1938-01-01     |
| 2 | 2         | f                   | 1994-01-01     |
| 3 | 3         | m                   | 1994-01-01     |
| 4 | 4         | m                   | 2004-01-01     |

## Visualize age pyramid

### Basic usage

By default, `plot_age_pyramid` will compute age as the difference between today and the date of birth:

```python
from eds_scikit.plot.age_pyramid import plot_age_pyramid

plot_age_pyramid(df_person)
```

![age_pyramid_default](age_pyramid_default.png)

### Advanced parameters

Further configuration can be provided, including :

- `datetime_ref` : Choose the reference to compute the age from.
  It can be either a single datetime (string or datetime type), an array of datetime
  (one reference for each patient) or a string representing a column of the input dataframe
- `return_array`: If set to True, return a dataframe instead of a chart.

```python
import pandas as pd
from datetime import datetime
from eds_scikit.plot.age_pyramid import plot_age_pyramid

dates_of_first_visit = pd.Series([datetime(2020, 1, 1)] * df_person.shape[0])
plot_age_pyramid(df_person, datetime_ref=dates_of_first_visit)
```

![age_pyramid_single_ref.png](age_pyramid_single_ref.png)


Please check [the documentation][eds_scikit.plot.age_pyramid.plot_age_pyramid] for further details on the function's parameters.
