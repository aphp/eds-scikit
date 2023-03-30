from datetime import datetime
from pathlib import Path

import altair as alt
import numpy as np
import pandas as pd
import pytest
from pandas.core.series import Series
from pandas.testing import assert_frame_equal

from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.plot.data_quality import plot_age_pyramid

data = load_person()

person_with_inclusion_date = data.person.copy()
N = len(person_with_inclusion_date)
delta_days = pd.to_timedelta(np.random.randint(0, 1000, N), unit="d")

person_with_inclusion_date["inclusion_datetime"] = (
    person_with_inclusion_date["birth_datetime"] + delta_days
)


@pytest.mark.parametrize(
    "datetime_ref", [datetime(2020, 1, 1), "inclusion_datetime", "2020-01-01"]
)
def test_plot_age_pyramid(datetime_ref):
    original_person = person_with_inclusion_date.copy()
    chart = plot_age_pyramid(person_with_inclusion_date, datetime_ref, savefig=False)
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)

    # Check that the data is unchanged
    assert_frame_equal(original_person, person_with_inclusion_date)


def test_age_pyramid_output():

    filename = "test.html"
    plot_age_pyramid(data.person, savefig=True, filename=filename)
    path = Path(filename)
    assert path.exists()
    path.unlink()

    group_gender_age = plot_age_pyramid(
        data.person, savefig=True, return_array=True, filename=filename
    )
    assert isinstance(group_gender_age, Series)

    chart, group_gender_age = plot_age_pyramid(
        data.person, savefig=False, return_array=True
    )
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)
    assert isinstance(group_gender_age, Series)

    chart = plot_age_pyramid(data.person, savefig=False, return_array=False)
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)

    with pytest.raises(ValueError, match="You have to set a filename"):
        plot_age_pyramid(person_with_inclusion_date, savefig=True, filename=None)

    with pytest.raises(
        ValueError, match="'filename' type must be str, got <class 'list'>"
    ):
        plot_age_pyramid(person_with_inclusion_date, savefig=True, filename=[1])


def test_plot_age_pyramid_datetime_ref_error():
    with pytest.raises(
        ValueError,
        match="`datetime_ref` must either be a column name or parseable date, got string '20x2-01-01'",
    ):
        _ = plot_age_pyramid(
            person_with_inclusion_date, datetime_ref="20x2-01-01", savefig=False
        )
    with pytest.raises(
        TypeError,
        match="`datetime_ref` must be either None, a parseable string date, a column name or a datetime. Got type: <class 'int'>, 2022",
    ):
        _ = plot_age_pyramid(
            person_with_inclusion_date, datetime_ref=2022, savefig=False
        )
