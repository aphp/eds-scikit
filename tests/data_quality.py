from datetime import datetime
from typing import Optional, Tuple

import altair as alt
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.core.series import Series

from ..utils.checks import check_columns


def plot_age_pyramid(
    person: DataFrame,
    datetime_ref: datetime = None,
    savefig: bool = False,
    filename: Optional[str] = None,
) -> Tuple[alt.Chart, Series]:
    """Plot an age pyramid from a 'person' pandas DataFrame.

    Parameters
    ----------
    person : pd.DataFrame (ks.DataFrame not supported),
        The person table. Must have the following columns:
        - `birth_datetime`, dtype : datetime or str
        - `person_id`, dtype : any
        - `gender_source_value`, dtype : str, {'m', 'f'}

    datetime_ref : datetime,
        The reference date to compute population age from.
        If set to None, datetime.today() will be used instead.

    savefig : bool,
        If set to True, filename must be set.
        The plot will be saved at the specified filename.

    filename : Optional[str],
        The path to save figure at.

    Returns
    -------
    chart : alt.Chart,
        If savefig set to True, returns None.

    group_gender_age : Series,
        The total number of patients grouped by gender and binned age.
    """
    check_columns(person, ["person_id", "birth_datetime", "gender_source_value"])

    if savefig:
        if filename is None:
            raise ValueError("You have to set a filename")
        if not isinstance(filename, str):
            raise ValueError(f"'filename' type must be str, got {type(filename)}")

    person_ = person.copy()

    if datetime_ref:
        today = pd.to_datetime(datetime_ref)
    else:
        today = datetime.today()
    person_["age"] = (today - person_["birth_datetime"]).dt.total_seconds()
    person_["age"] /= 365 * 24 * 3600

    bins = np.arange(0, 100, 10)
    labels = [f"{left}-{right}" for left, right in zip(bins[:-1], bins[1:])]
    person_["age_bins"] = pd.cut(person_["age"], bins=bins, labels=labels)
    person_["age_bins"] = person_["age_bins"].astype(str).str.replace("nan", "90+")

    person_ = person_.loc[person_["gender_source_value"].isin(["m", "f"])]
    group_gender_age = person_.groupby(["gender_source_value", "age_bins"])[
        "person_id"
    ].count()

    male = group_gender_age["m"].reset_index()
    female = group_gender_age["f"].reset_index()

    left = (
        alt.Chart(male)
        .mark_bar()
        .encode(
            y=alt.Y("age_bins", axis=None, sort=alt.SortOrder("descending")),
            x=alt.X("person_id", sort=alt.SortOrder("descending")),
        )
        .properties(title="Male")
    )

    right = (
        alt.Chart(female)
        .mark_bar(color="coral")
        .encode(
            y=alt.Y("age_bins", axis=None, sort=alt.SortOrder("descending")),
            x=alt.X("person_id", title="N"),
        )
        .properties(title="Female")
    )

    middle = (
        alt.Chart(male)
        .mark_text()
        .encode(
            y=alt.Text("age_bins", axis=None, sort=alt.SortOrder("descending")),
            text=alt.Y("age_bins"),
        )
    )

    chart = alt.concat(left, middle, right, spacing=5)

    if savefig:
        chart.save(filename)
    else:
        return chart, group_gender_age
