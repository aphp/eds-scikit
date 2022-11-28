from datetime import datetime
from typing import List

from loguru import logger

from eds_scikit.utils.framework import get_framework
from eds_scikit.utils.typing import DataFrame


def tagging(
    tag_to_df: DataFrame,
    tag_from_df: DataFrame,
    concept_to_tag: str,
    tag_to_date_cols: List[str] = ["t_start", "t_end"],
    tag_from_date_cols: List[str] = ["t_start", "t_end"],
    algo: str = "intersection",
) -> DataFrame:
    """

    Parameters
    ----------
    tag_to_df : DataFrame
    tag_from_df : DataFrame
    concept_to_tag : str
    tag_to_date_cols : List[str], optional
    tag_from_date_cols : List[str], optional
    algo : str, optional

    Returns
    -------
    DataFrame
    """
    framework = get_framework(tag_to_df)

    tag_to_df = tag_to_df.assign(event_id=tag_to_df.index)

    tag_from = tag_from_df.loc[
        tag_from_df.concept == concept_to_tag,
        ["person_id", "value"] + ["t_start", "t_end"],
    ]

    tmp = (
        tag_to_df.rename(
            columns={tag_to_date_cols[0]: "t_start_x", tag_to_date_cols[1]: "t_end_x"}
        )
        .merge(
            tag_from.rename(
                columns={
                    tag_from_date_cols[0]: "t_start_y",
                    tag_from_date_cols[1]: "t_end_y",
                }
            ),
            on="person_id",
            how="left",
        )
        .dropna(subset=["t_start_x", "t_end_x", "t_start_y", "t_end_y"])
    )

    if len(tmp) == 0:
        # TODO: is this necessary ?
        logger.warning("No matching were found between the 2 DataFrames")

        return framework.DataFrame(
            columns=["person_id", "t_start", "t_end", "concept", "value"]
        )

    tmp["tag"] = compare_intervals(
        tmp["t_start_x"],
        tmp["t_end_x"],
        tmp["t_start_y"],
        tmp["t_end_y"],
        algo=algo,
    )

    value_col = (
        "value_y"
        if (("value" in tag_to_df.columns) and ("value" in tag_from_df.columns))
        else "value"
    )

    tags = (
        tmp.groupby(["event_id", value_col])
        .tag.any()
        .unstack()
        .fillna(False)
        .reset_index()
    )
    tags = tag_to_df[["event_id"]].merge(tags, on="event_id", how="left").fillna(False)
    tags = tag_to_df.merge(tags, on="event_id", how="left").drop(columns="event_id")
    return tags


class interval_algos:
    intersection: str = "intersection"
    to_in_from: str = "to_in_from"
    from_in_to: str = "from_in_to"
    from_before_to: str = "from_before_to"
    to_before_from: str = "to_before_from"


def compare_intervals(
    A_start: datetime,
    A_end: datetime,
    B_start: datetime,
    B_end: datetime,
    algo: str = "intersection",
) -> bool:
    if algo == interval_algos.intersection:
        # https://github.com/pandas-dev/pandas/blob/9936902c5aa2396195bca0e07d40104c96ed20e1/pandas/_libs/interval.pyx#L498
        # overlaps is equivalent negation of two interval being disjoint:
        # disjoint = (A.left > B.right) or (B.left > A.right)
        # (simplifying the negation allows this to be done in less operations) which gives
        # (A.left < B.right) and (B.left < A.right)
        # we use <= to consider "touching" intervals as intersecting
        return (A_start <= B_end) & (B_start <= A_end)
    elif algo == interval_algos.to_in_from:
        return (A_start >= B_start) & (A_end <= B_end)
    elif algo == interval_algos.from_in_to:
        return (B_start >= A_start) & (B_end <= A_end)
    elif algo == interval_algos.from_before_to:
        return B_end <= A_start
    elif algo == interval_algos.to_before_from:
        return A_end <= B_start
    else:
        raise ValueError(
            f"Unknown algo: {algo}. see tagging_functions.interval_algos for valid arguments."
        )
