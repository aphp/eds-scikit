import altair as alt

from eds_scikit.datasets import load_event_sequences
from eds_scikit.plot.event_sequences import plot_event_sequences

df_events = load_event_sequences()

def test_visit_merging():
    chart = plot_event_sequences(df_events)
    assert type(chart) == alt.vegalite.v4.api.VConcatChart
