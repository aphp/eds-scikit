import random
from typing import Dict, List, Optional, Tuple, Union

import altair as alt
import numpy as np
import pandas as pd


def plot_event_sequences(
    df_events: pd.DataFrame,
    event_col: Optional[str] = "event",
    event_start_datetime_col: Optional[str] = "event_start_datetime",
    event_end_datetime_col: Optional[str] = "event_end_datetime",
    dim_mapping: Optional[Dict[str, Dict[str, Union[Tuple[int], str]]]] = None,
    index_date_col: Optional[str] = None,
    family_col: Optional[str] = None,
    family_to_index: Optional[Dict[str, int]] = None,
    list_person_ids: Optional[List[str]] = None,
    same_x_axis_scale: Optional[bool] = False,
    subplot_height: Optional[int] = 200,
    subplot_width: Optional[int] = 500,
    point_size: Optional[int] = 400,
    bar_height: Optional[int] = 20,
    title: Optional[str] = None,
    seed: Optional[int] = 0,
):
    """
    Plots individual sequences from an events DataFrame. Each event must be recorded with a start date, a name and a `person_id`.
    Events can be both one-time (only start date given) or longitudinal (both start and end dates).
    Events can also be aggregated in families using the `family_col` argument.
    Finally, events labelling and colors can be manually set by providing a `dim_mapping` dictionary.

    Parameters
    ----------
    df_events: pd.DataFrame
        DataFrame gathering the events information. Must contain at least `person_id`, event, t_start and t_end columns.
    event_col: Optional[str] = "event"
        Column name of the events.
    event_start_datetime_col: Optional[str] = "event_start_datetime"
        Column name of the event start datetime.
    event_end_datetime_col: Optional[str] = "event_end_datetime"
        Column name of the event end datetime.
    dim_mapping: Optional[Dict[str,Dict[str,Union[tuple(int),str]]]] = None
        Mapping dictionary to provide plotting details on events. Must be of type :
        ```python
            dim_labelling = {
                "event_1" : {"color":(255,200,150), "label":"Event 1"},
                "event_2" : {"color":(200,255,150), "label":"Event 2"}
            }
        ```
    index_date_col: Optional[str] = None
        Column name of the index date to compute relative datetimes for events. For example, it could be the date of inclusion for each patient.
    family_col: Optional[str] = None
        Column name of family events. Events of a given family will be plot on the same row.
    family_to_index: Optional[Dict[str,int]] = None
        Dictionary mapping family names towards ordering indices.
    list_person_ids: Optional[List[str]] = None
        List of person_ids to plot. If None given, all individual sequences will be plot.
    same_x_axis_scale: Optional[bool] = False
        Whether to use the same axis scale for all sequences.
    subplot_height: Optional[int] = 200
        Height of each plot.
    subplot_width: Optional[int] = 500
        Width of each plot.
    point_size: Optional[int] = 400
        Size of points for one-time events.
    bar_height: Optional[int] = 20
        Height of bars for continuous events.
    title: Optional[str] = None
        Chart title.
    seed: int = 0
        Seed to randomly draw colors when not provided.

    Returns
    -------
    chart: alt.Chart
        Chart with the plotted individual event sequences.
    """
    random.seed(seed)

    # Pre-selection of the given patients and required columns.
    if list_person_ids is not None:
        order = {val: idx for idx, val in enumerate(list_person_ids)}
        df_events = df_events.query("person_id in @list_person_ids").sort_values(
            by="person_id", key=lambda x: x.map(order)
        )

    data_plot = df_events.sort_values(by=["person_id", event_start_datetime_col])

    # Encoding events start and end dates
    if index_date_col is not None:
        data_plot["relative_event_start"] = (
            data_plot[event_start_datetime_col] - df_events[index_date_col]
        ).dt.days.astype(int)

        data_plot["event_duration"] = (
            (df_events[event_end_datetime_col] - data_plot[event_start_datetime_col])
            .dt.days.fillna(1)
            .astype(int)
        )

        data_plot["relative_event_end"] = (
            data_plot.relative_event_start + data_plot.event_duration
        )
        x_encoding = "relative_event_start:Q"
        x2_encoding = "relative_event_end:Q"

    else:
        x_encoding = f"{event_start_datetime_col}:T"
        x2_encoding = f"{event_end_datetime_col}:T"

    # Ordering events
    if family_col is not None:
        if family_to_index is None:
            family_to_index = {
                k: v for v, k in enumerate(list(data_plot[family_col].unique()))
            }

        data_plot["dim_id"] = data_plot[family_col].map(family_to_index)
    else:
        _, classes = np.unique(data_plot[event_col], return_inverse=True)
        data_plot["dim_id"] = classes

    # Mapping events towards colors and labels
    if dim_mapping is not None:
        data_plot["dim_label"] = data_plot[event_col].apply(
            lambda x: dim_mapping[x]["label"]
        )

        labels = []
        colors = []
        for event, event_dict in dim_mapping.items():
            labels.append(dim_mapping[event]["label"])
            colors.append(f"rgb{dim_mapping[event]['color']}")

    else:
        data_plot["dim_label"] = data_plot[event_col]
        labels = list(data_plot["dim_label"].unique())
        colors = [
            f"rgb{tuple([random.randint(0,255),random.randint(0,255),random.randint(0,255)])}"
            for _ in labels
        ]

    # Base chart
    raw = alt.Chart(data_plot).encode(
        x=alt.X(x_encoding),
        y=alt.Y("dim_id:O", title=""),
        color=alt.Color(
            "dim_label:O",
            scale=alt.Scale(domain=labels, range=colors),
            title="Event type",
        ),
    )

    # One-time events
    point_dim = (
        raw.transform_filter(
            {"not": alt.FieldValidPredicate(field=event_end_datetime_col, valid=True)}
        )
        .mark_point(filled=True, size=point_size, cursor="pointer")
        .encode(
            tooltip=[f"{event_col}", f"{event_start_datetime_col}"],
        )
    )

    # Continuous events
    continuous_dim = (
        raw.transform_filter(
            alt.FieldValidPredicate(event_end_datetime_col, valid=True)
        )
        .mark_bar(
            filled=True,
            cursor="pointer",
            cornerRadius=bar_height / 2,
            height=bar_height,
        )
        .encode(
            x2=x2_encoding,
            tooltip=[
                f"{event_col}",
                f"{event_start_datetime_col}",
                f"{event_end_datetime_col}",
            ],
        )
    )

    # Aggregation
    base = (point_dim + continuous_dim).properties(
        width=subplot_width,
        height=subplot_height,
    )

    # Vertical concatenation of all patients' sequences
    chart = (
        alt.vconcat()
        .configure_legend(labelFontSize=13, symbolSize=150, titleFontSize=15)
        .configure_axisY(disable=True)
    )

    for person_id in data_plot.person_id.unique():
        chart &= base.transform_filter(
            alt.expr.datum.person_id == person_id
        ).properties(title=f"Sequence of patient {person_id}")

    if same_x_axis_scale:
        chart = chart.resolve_scale(x="shared")

    if title is not None:
        chart = chart.properties(title=title)

    return chart
