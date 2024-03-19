# Visualizing event sequences

When studying sequences of events (e.g care trajectories, drug sequences, ...), it might be useful to visualize individual sequences. To that end, we provide the `plot_event_sequences` function to plot individual sequences given an events dataframe.

## Load a synthetic dataset

An events dataset has been created to illustrate the visualization function.
It can be load as follows :

```python
from eds_scikit.datasets.synthetic.event_sequences import load_event_sequences

df_events = load_event_sequences()
```

The `df_events` dataset contains occurrences of 12 events, derived from 7 events' families ("A", "B", "C", "D", "E", "F", "G).

Events can be both one-time and continuous.

An `index_date` is also provided and refers to the inclusion date of each patient in the cohort.

The first raws of the dataframe are as follows :

```python
df_events.head()
```
|   | person_id | event_family | event | event_start_datetime | event_end_datetime | index_date |
|---|-----------|--------------|-------|----------------------|--------------------|------------|
| 0 | 1         | A            | a1    | 2020-01-01           | 2020-01-02         | 2020-01-01 |
| 1 | 1         | A            | a2    | 2020-01-03           | 2020-01-04         | 2020-01-01 |
| 2 | 1         | B            | b1    | 2020-01-03           | 2020-01-06         | 2020-01-01 |
| 3 | 1         | C            | c1    | 2020-01-05           | NaT                | 2020-01-01 |
| 4 | 1         | C            | c2    | 2020-01-06           | 2020-01-08         | 2020-01-01 |

## Visualize individual sequences

### Basic usage

Individual sequences of events can be plotted using the `plot_event_sequences` function :

```python
from eds_scikit.plot.event_sequences import plot_event_sequences

chart = plot_event_sequences(df_events)
chart
```
<figure markdown>
  [![Image title](event_sequences_raw.png)](#)
  <figcaption></figcaption>
</figure>

### Advanced parameters

Further configuration can be provided, including :
- `dim_mapping` : dictionary to set colors and labels for each event type.
- `family_col`: column name of events' families.
- `list_person_ids`: List of specific `person_id`
- `same_x_axis_scale`: boolean to set all individual charts to the same scale

Here we provide an exemple of `dim_mapping`, and we plot sequences aggregated following the `event_family` classification.

```python
dim_mapping = {
    "a1": {"color": (255, 200, 150), "label": "eventA1"},
    "a2": {"color": (255, 150, 150), "label": "eventA2"},
    "a3": {"color": (255, 100, 150), "label": "eventA3"},
    "b1": {"color": (100, 200, 150), "label": "eventB1"},
    "c1": {"color": (50, 255, 255), "label": "eventC1"},
    "c2": {"color": (50, 200, 255), "label": "eventC2"},
    "c3": {"color": (50, 100, 255), "label": "eventC3"},
    "d1": {"color": (180, 200, 100), "label": "eventD1"},
    "d2": {"color": (180, 150, 100), "label": "eventD2"},
    "e1": {"color": (130, 60, 10), "label": "eventE1"},
    "f1": {"color": (255, 0, 0), "label": "eventF1"},
    "g1": {"color": (100, 0, 200), "label": "eventG1"},
}
```

```python
plot_event_sequences(
    df_events,
    family_col="event_family",
    dim_mapping=dim_mapping,
    same_x_axis_scale=True,
    title="Event sequences",
)
```
<figure markdown>
  [![Image title](event_sequences_agg.png)](#)
  <figcaption></figcaption>
</figure>

Please check [the documentation][eds_scikit.plot.event_sequences.plot_event_sequences] for further details on the function's parameters.
