from copy import copy
from datetime import datetime
from typing import Tuple

import altair as alt
import numpy as np
import pandas as pd
from loguru import logger
from pandas.core.series import Series

from ..utils.checks import check_columns
from ..utils.framework import bd
from ..utils.typing import DataFrame


def plot_age_pyramid(
    person: DataFrame,
    datetime_ref: datetime = None,
    return_array: bool = False,
) -> Tuple[alt.ConcatChart, Series]:
    """Plot an age pyramid from a 'person' pandas DataFrame.

    Parameters
    ----------
    person : pd.DataFrame (ks.DataFrame not supported),
        The person table. Must have the following columns:
        - `birth_datetime`, dtype : datetime or str
        - `person_id`, dtype : any
        - `gender_source_value`, dtype : str, {'m', 'f'}

    datetime_ref : Union[datetime, str], default None
        The reference date to compute population age from.
        If a string, it searches for a column with the same name in the person table: each patient has his own datetime reference.
        If a datetime, the reference datetime is the same for all patients.
        If set to None, datetime.today() will be used instead.

    filename : str, default None
        The path to save figure at.

    savefig : bool, default False
        If set to True, filename must be set.
        The plot will be saved at the specified filename.

    return_array : bool, default False
        If set to True, return chart and its pd.Dataframe representation.

    Returns
    -------
    chart : alt.ConcatChart,
        If savefig set to True, returns None.

    group_gender_age : Series,
        The total number of patients grouped by gender and binned age.
    """
    check_columns(person, ["person_id", "birth_datetime", "gender_source_value"])

    datetime_ref_raw = copy(datetime_ref)

    if datetime_ref is None:
        datetime_ref = datetime.today()
    elif isinstance(datetime_ref, datetime):
        datetime_ref = pd.to_datetime(datetime_ref)
    elif isinstance(datetime_ref, str):
        # A string type for datetime_ref could be either
        # a column name or a datetime in string format.
        if datetime_ref in person.columns:
            datetime_ref = person[datetime_ref]
        else:
            datetime_ref = pd.to_datetime(
                datetime_ref, errors="coerce"
            )  # In case of error, will return NaT
            if pd.isnull(datetime_ref):
                raise ValueError(
                    f"`datetime_ref` must either be a column name or parseable date, "
                    f"got string '{datetime_ref_raw}'"
                )
    else:
        raise TypeError(
            f"`datetime_ref` must be either None, a parseable string date"
            f", a column name or a datetime. Got type: {type(datetime_ref)}, {datetime_ref}"
        )

    cols_to_keep = ["person_id", "birth_datetime", "gender_source_value"]
    person_ = bd.to_pandas(person[cols_to_keep])

    person_["age"] = (datetime_ref - person_["birth_datetime"]).dt.total_seconds()
    person_["age"] /= 365 * 24 * 3600

    # Remove outliers
    mask_age_inliners = (person_["age"] > 0) & (person_["age"] < 125)
    n_outliers = (~mask_age_inliners).sum()
    if n_outliers > 0:
        perc_outliers = 100 * n_outliers / person_.shape[0]
        logger.warning(
            f"{n_outliers} ({perc_outliers:.4f}%) individuals' "
            "age is out of the (0, 125) interval, we skip them."
        )
    person_ = person_.loc[mask_age_inliners]

    # Aggregate rare age categories
    mask_rare_age_agg = person_["age"] > 90
    person_.loc[mask_rare_age_agg, "age"] = 99

    bins = np.arange(0, 100, 10)
    labels = [f"{left}-{right}" for left, right in zip(bins[:-1], bins[1:])]
    person_["age_bins"] = pd.cut(person_["age"], bins=bins, labels=labels)

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
            y=alt.Y("age_bins", axis=None, sort=alt.SortOrder("descending")),
            text=alt.Text("age_bins"),
        )
    )

    chart = alt.concat(left, middle, right, spacing=5)

    if return_array:
        return group_gender_age

    return chart
