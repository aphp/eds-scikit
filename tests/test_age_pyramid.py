from datetime import datetime, timedelta
from pathlib import Path

import altair as alt
import pytest
from pandas.core.series import Series
from pandas.testing import assert_frame_equal

from eds_scikit.datasets.synthetic.person import load_person
from eds_scikit.plot.data_quality import plot_age_pyramid
import pandas as pd 
import numpy as np

data = load_person()

person_with_inclusion_date = data.person.copy()
person_with_inclusion_date["inclusion_datetime"] = person_with_inclusion_date["birth_datetime"] + pd.to_timedelta(np.random.randint(0, 1000, len(person_with_inclusion_date)), unit='d')

@pytest.mark.parametrize(
    "datetime_ref", [datetime(2020, 1, 1), "inclusion_datetime"]
    )
def test_plot_age_pyramid(datetime_ref):
    original_person = person_with_inclusion_date.copy()
    chart, group_gender_age = plot_age_pyramid(person_with_inclusion_date, datetime_ref, savefig=False)
    assert isinstance(chart, alt.vegalite.v4.api.ConcatChart)
    assert isinstance(group_gender_age, Series)

    # Check that the data is unchanged
    assert_frame_equal(original_person, person_with_inclusion_date)

    filename = "test.html"
    _ = plot_age_pyramid(person_with_inclusion_date, savefig=True, filename=filename)
    path = Path(filename)
    assert path.exists()
    path.unlink()

    with pytest.raises(ValueError, match="You have to set a filename"):
        _ = plot_age_pyramid(person_with_inclusion_date, savefig=True, filename=None)

    with pytest.raises(
        ValueError, match="'filename' type must be str, got <class 'list'>"
    ):
        _ = plot_age_pyramid(person_with_inclusion_date, savefig=True, filename=[1])
