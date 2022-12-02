from datetime import datetime
from pathlib import Path

import altair as alt
import pytest
from pandas.core.series import Series
from pandas.testing import assert_frame_equal

from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.plot.data_quality import plot_age_pyramid

data = load_person()


def test_plot_age_pyramid():
    original_person = data.person.copy()

    datetime_ref = datetime(2020, 1, 1)
    chart, group_gender_age = plot_age_pyramid(data.person, datetime_ref, savefig=False)
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)
    assert isinstance(group_gender_age, Series)

    # Check that the data is unchanged
    assert_frame_equal(original_person, data.person)

    filename = "test.html"
    _ = plot_age_pyramid(data.person, savefig=True, filename=filename)
    path = Path(filename)
    assert path.exists()
    path.unlink()

    with pytest.raises(ValueError, match="You have to set a filename"):
        _ = plot_age_pyramid(data.person, savefig=True, filename=None)

    with pytest.raises(
        ValueError, match="'filename' type must be str, got <class 'list'>"
    ):
        _ = plot_age_pyramid(data.person, savefig=True, filename=[1])
