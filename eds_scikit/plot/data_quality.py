from copy import copy
from datetime import datetime
from typing import Tuple, Union

import altair as alt
import numpy as np
import pandas as pd
from pandas.api.types import is_integer_dtype
from pandas.core.frame import DataFrame
from pandas.core.series import Series

from ..utils.checks import check_columns
from ..utils.framework import bd


def plot_age_pyramid(
    person: DataFrame,
    datetime_ref: Union[datetime, str] = None,
    filename: str = None,
    savefig: bool = False,
    return_vector: bool = False,
) -> Tuple[alt.Chart, Series]:
    """Plot an age pyramid from a 'person' pandas DataFrame.

    Parameters
    ----------
    person : pd.DataFrame (ks.DataFrame not supported),
        The person table. Must have the following columns:
        - `birth_datetime`, dtype : datetime or str
        - `person_id`, dtype : any
        - `gender_source_value`, dtype : str, {'m', 'f'}

    datetime_ref : Union[datetime, str],
        The reference date to compute population age from.
        If a string, it searches for a column with the same name in the person table: each patient has his own datetime reference.
        If a datetime, the reference datetime is the same for all patients.
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
    datetime_ref_original = copy(datetime_ref)

    if datetime_ref is None:
        datetime_ref = datetime.today()
    elif isinstance(datetime_ref, datetime):
        datetime_ref = pd.to_datetime(datetime_ref)
    elif isinstance(datetime_ref, str):
        if datetime_ref in person.columns:
            datetime_ref = person[datetime_ref]
        else:
            datetime_ref = pd.to_datetime(
                datetime_ref, errors="coerce"
            )  # In case of error, will return NaT
            if pd.isnull(datetime_ref):
                raise ValueError(
                    f"`datetime_ref` must either be a column name or parseable date, "
                    f"got string '{datetime_ref_original}'"
                )
    else:
        raise TypeError(
            f"`datetime_ref` must be either None, a parseable string date"
            f", a column name or a datetime. Got type: {type(datetime_ref)}, {datetime_ref}"
        )

    person = person.loc[person["gender_source_value"].isin(["m", "f"])]

    deltas = datetime_ref - person["birth_datetime"]
    if not is_integer_dtype(deltas):
        deltas = deltas.dt.total_seconds()
    person["age"] = deltas / 365 * 24 * 3600

    bins = np.arange(0, 100, 10)
    labels = [f"{left}-{right}" for left, right in zip(bins[:-1], bins[1:])]

    # This is equivalent to `pd.cut()` for pandas and this call our custom `cut`
    # implementation for koalas.
    person["age_bins"] = bd.cut(person["age"], bins=bins, labels=labels)

    # This is equivalent to `person.cache()` for koalas and this is a no-op
    # for pandas.
    # Cache the intermediate results of the transformation so that other transformation
    # runs on top of cached will perform faster.
    # TODO: try to remove it and check perfs.
    bd.cache(person)

    group_gender_age = person.groupby(["gender_source_value", "age_bins"])[
        "person_id"
    ].count()

    # Convert to pandas to ease plotting.
    group_gender_age = bd.to_pandas(group_gender_age)

    group_gender_age["age_bins"] = (
        person["age_bins"].astype(str).str.lower().str.replace("nan", "90+")
    )

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
        if return_vector:
            return group_gender_age

    if return_vector:
        return chart, group_gender_age

    return chart
