from datetime import datetime

import altair as alt
import numpy as np
import pandas as pd
import pytest
from pandas.core.series import Series
from pandas.testing import assert_frame_equal

from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.plot.age_pyramid import plot_age_pyramid

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
    chart = plot_age_pyramid(person_with_inclusion_date, datetime_ref)
    assert isinstance(chart, alt.ConcatChart)

    # Check that the data is unchanged
    assert_frame_equal(original_person, person_with_inclusion_date)


def test_age_pyramid_output():

    chart = plot_age_pyramid(data.person)
    assert isinstance(chart, alt.ConcatChart)

    group_gender_age = plot_age_pyramid(data.person, return_array=True)
    assert isinstance(group_gender_age, Series)


def test_plot_age_pyramid_datetime_ref_error():
    with pytest.raises(
        ValueError,
        match="`datetime_ref` must either be a column name or parseable date, got string '20x2-01-01'",
    ):
        _ = plot_age_pyramid(
            person_with_inclusion_date,
            datetime_ref="20x2-01-01",
        )

    with pytest.raises(
        TypeError,
        match="`datetime_ref` must be either None, a parseable string date, a column name or a datetime. Got type: <class 'int'>, 2022",
    ):
        _ = plot_age_pyramid(
            person_with_inclusion_date,
            datetime_ref=2022,
        )
