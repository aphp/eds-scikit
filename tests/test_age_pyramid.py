from datetime import datetime
from pathlib import Path

import altair as alt
import numpy as np
import pytest
from pandas.core.series import Series
from pandas.testing import assert_frame_equal

from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.plot.data_quality import plot_age_pyramid

data = load_person()


@pytest.mark.parametrize(
    "datetime_ref",
    [
        None,
        datetime(2020, 1, 1),
        np.full(data.person.shape[0], datetime(2020, 1, 1)),
    ],
)
def test_age_pyramid_datetime_ref_format(datetime_ref):
    original_person = data.person.copy()

    chart = plot_age_pyramid(
        data.person, datetime_ref, savefig=False, return_vector=False
    )
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)

    # Check that the data is unchanged
    assert_frame_equal(original_person, data.person)


def test_age_pyramid_output():

    filename = "test.html"
    plot_age_pyramid(data.person, savefig=True, filename=filename)
    path = Path(filename)
    assert path.exists()
    path.unlink()

    group_gender_age = plot_age_pyramid(
        data.person, savefig=True, return_vector=True, filename=filename
    )
    assert isinstance(group_gender_age, Series)

    chart, group_gender_age = plot_age_pyramid(
        data.person, savefig=False, return_vector=True
    )
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)
    assert isinstance(group_gender_age, Series)

    chart = plot_age_pyramid(data.person, savefig=False, return_vector=False)
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)

    with pytest.raises(ValueError, match="You have to set a filename"):
        _ = plot_age_pyramid(data.person, savefig=True, filename=None)

    with pytest.raises(
        ValueError, match="'filename' type must be str, got <class 'list'>"
    ):
        _ = plot_age_pyramid(data.person, savefig=True, filename=[1])
