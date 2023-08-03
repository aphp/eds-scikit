import altair as alt
import pytest

from eds_scikit.datasets import load_event_sequences
from eds_scikit.plot.event_sequences import plot_event_sequences

df_events = load_event_sequences()
dim_mapping = dim_mapping = {
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

family_to_index = {k: v for v, k in enumerate(df_events["event_family"].unique())}


@pytest.mark.parametrize("dim_mapping", [None, dim_mapping])
@pytest.mark.parametrize("index_date_col", [None, "index_date"])
@pytest.mark.parametrize("family_col", [None, "event_family"])
@pytest.mark.parametrize("family_to_index", [None, family_to_index])
@pytest.mark.parametrize("list_person_ids", [None, [1]])
@pytest.mark.parametrize("same_x_axis_scale", [True, False])
@pytest.mark.parametrize("title", [None, "Test"])
def test_event_sequences(
    dim_mapping,
    index_date_col,
    family_col,
    family_to_index,
    list_person_ids,
    same_x_axis_scale,
    title,
):
    chart = plot_event_sequences(
        df_events,
        dim_mapping=dim_mapping,
        index_date_col=index_date_col,
        family_col=family_col,
        family_to_index=family_to_index,
        list_person_ids=list_person_ids,
        same_x_axis_scale=same_x_axis_scale,
        title=title,
    )
    assert type(chart) == alt.VConcatChart
