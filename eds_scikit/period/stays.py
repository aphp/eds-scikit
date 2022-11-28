from datetime import datetime, timedelta
from typing import List, Optional, Tuple, Union

from numpy import nan as NaN

from eds_scikit.utils.checks import MissingConceptError, algo_checker, concept_checker
from eds_scikit.utils.datetime_helpers import substract_datetime
from eds_scikit.utils.framework import get_framework
from eds_scikit.utils.typing import DataFrame


def cleaning(
    vo,
    long_stay_threshold: timedelta,
    long_stay_filtering: Union[str, None],
    remove_deleted_visits: bool,
    open_stay_end_datetime: datetime,
) -> Tuple[DataFrame, DataFrame]:
    """
    Preprocessing of visits before merging them in stays.
    The function will split the input `vo` DataFrame into 2, one that
    should undergo the merging procedure, and one that shouldn't.
    Depending on the input parameters, 3 type of visits can be prevented to
    undergo the merging procedure:

    - Too long visits
    - Too long AND unclosed visits
    - Removed visits

    See the [merge_visits()][eds_scikit.period.stays.merge_visits] function for details of the parameters
    """

    LONG_STAY_FILTERING_VALUES = ["all", "open", None]
    DELETED_ROW_VALUE = "supprimé"

    if long_stay_filtering not in LONG_STAY_FILTERING_VALUES:
        raise ValueError(
            f"""Unknown value for `long_stay_filtering`.
            Accepted values are {LONG_STAY_FILTERING_VALUES}"""
        )

    if remove_deleted_visits:
        deleted_visit_mask = vo["row_status_source_value"] == DELETED_ROW_VALUE
    no_starting_date_mask = vo["visit_start_datetime"].isna()
    no_ending_date_mask = vo["visit_end_datetime"].isna()

    vo[
        "visit_end_datetime_calc"
    ] = open_stay_end_datetime  # Cannot use fillna() with datetime in Koalas
    vo["visit_end_datetime_calc"] = vo["visit_end_datetime"].combine_first(
        vo["visit_end_datetime_calc"]
    )

    too_long_stays_mask = (
        substract_datetime(vo["visit_end_datetime_calc"], vo["visit_start_datetime"])
        >= long_stay_threshold.total_seconds()
    )

    mask = no_starting_date_mask

    if long_stay_filtering == "all":
        mask = mask | too_long_stays_mask

    elif long_stay_filtering == "open":
        mask = mask | (too_long_stays_mask & no_ending_date_mask)

    if remove_deleted_visits:
        mask = (mask) | deleted_visit_mask

    return vo[~mask], vo[mask]


@concept_checker(concepts=["STAY_ID", "CONTIGUOUS_STAY_ID"])
def merge_visits(
    vo: DataFrame,
    remove_deleted_visits: bool = True,
    long_stay_threshold: timedelta = timedelta(days=365),
    long_stay_filtering: Optional[str] = "all",
    open_stay_end_datetime: Optional[datetime] = None,
    max_timedelta: timedelta = timedelta(days=2),
    merge_different_hospitals: bool = False,
    merge_different_source_values: Union[bool, List[str]] = ["hospitalisés", "urgence"],
) -> DataFrame:
    """
    Merge "close" visit occurrences to consider them as a single stay
    by adding a ``STAY_ID`` and ``CONTIGUOUS_STAY_ID`` columns to the DataFrame.

    The value of these columns will be the `visit_occurrence_id` of the first (meaning the oldest)
    visit of the stay.

    From a temporal point of view, we consider that two visits belong to the same stay if either:

    - They intersect
    - The time difference between the end of the most recent and the start of the oldest
      is lower than ``max_timedelta`` (for ``STAY_ID``) or 0 (for ``CONTIGUOUS_STAY_ID``)

    Additionally, other parameters are available to further adjust the merging rules. See below.

    Parameters
    ----------
    vo : DataFrame
        The ``visit_occurrence`` DataFrame, with at least the following columns:
        - visit_occurrence_id
        - person_id
        - visit_start_datetime_calc (from preprocessing)
        - visit_end_datetime (from preprocessing)
        Depending on the input parameters, additional columns may be required:
        - care_site_id (if ``merge_different_hospitals == True``)
        - visit_source_value (if ``merge_different_source_values != False``)
        - row_status_source_value (if ``remove_deleted_visits= True``)
    remove_deleted_visits: bool
        Wether to remove deleted visits from the merging procedure.
        Deleted visits are extracted via the `row_status_source_value` column
    long_stay_filtering : Optional[str]
        Filtering method for long and/or non-closed visits. First of all, visits with no starting date
        won't be merged with any other visit, and visits with no ending date will have a temporary
        "theoretical" ending date set by ``datetime.now()``. That being said, some visits are sometimes years long
        because they weren't closed at time. If other visits occurred during this timespan,
        they could be all merged into the same stay. To avoid this issue, filtering can be done
        depending on the ``long_stay_filtering`` value:

        - ``all``: All long stays (closed and open) are removed from the merging procedure
        - ``open``: Only long open stays are removed from the merging procedure
        - ``None``: No filtering is done on long visits

        Long stays are determined by the ``long_stay_threshold`` value.
    long_stay_threshold : timedelta
        Minimum visit duration value to consider a visit as candidate for "long visits filtering"
    open_stay_end_datetime: Optional[datetime]
        Datetime to use in order to fill the `visit_end_datetime` of open visits. This is necessary in
        order to compute stay duration and to filter long stays. If not provided `datetime.now()` will be used.
        You might provide the extraction date of your data here.
    max_timedelta : timedelta
        Maximum time difference between the end of a visit and the start of another to consider
        them as belonging to the same stay. This duration is internally converted in seconds before
        comparing. Thus, if you want e.g. to merge visits happening in two consecutive days, you should use
        `timedelta(days=2)` and NOT `timedelta(days=1)` in order to take into account extreme cases such as
        an first visit ending on Monday at 00h01 AM and another one starting at 23h59 PM on Tuesday
    merge_different_hospitals : bool
        Wether to allow visits occurring in different hospitals to be merged into a same stay
    merge_different_source_values : Union[bool, List[str]]
        Wether to allow visits with different `visit_source_value` to be merged into a same stay. Values can be:

        - `True`: the `visit_source_value` isn't taken into account for the merging
        - `False`: only visits with the same `visit_source_value` can be merged into a same stay
        - `List[str]`: only visits which `visit_source_value` is in the provided list can be merged together.

        **Warning**: You should avoid merging visits where `visit_source_value == "hospitalisation incomplète"`,
        because those stays are often never closed.

    Returns
    -------
    vo : DataFrame
        Visit occurrence DataFrame with additional `STAY_ID` column

    Examples
    --------

    >>> import pandas as pd
    >>> from datetime import datetime, timedelta
    >>> data = {
        1 : ['A', 999, datetime(2021,1,1), datetime(2021,1,5), 'hospitalisés'],
        2 : ['B', 999, datetime(2021,1,4), datetime(2021,1,8), 'hospitalisés'],
        3 : ['C', 999, datetime(2021,1,12), datetime(2021,1,18), 'hospitalisés'],
        4 : ['D', 999, datetime(2021,1,13), datetime(2021,1,14), 'urgence'],
        5 : ['E', 999, datetime(2021,1,19), datetime(2021,1,21), 'hospitalisés'],
        6 : ['F', 999, datetime(2021,1,25), datetime(2021,1,27), 'hospitalisés'],
        7 : ['G', 999, datetime(2017,1,1), None, "hospitalisés"]
    }
    >>> vo = pd.DataFrame.from_dict(
        data,
        orient="index",
        columns=[
            "visit_occurrence_id",
            "person_id",
            "visit_start_datetime",
            "visit_end_datetime",
            "visit_source_value",
        ],
    )
    >>> vo
      visit_occurrence_id  person_id visit_start_datetime visit_end_datetime visit_source_value
    1                   A        999           2021-01-01         2021-01-05       hospitalisés
    2                   B        999           2021-01-04         2021-01-08       hospitalisés
    3                   C        999           2021-01-12         2021-01-18       hospitalisés
    4                   D        999           2021-01-13         2021-01-14            urgence
    5                   E        999           2021-01-19         2021-01-21       hospitalisés
    6                   F        999           2021-01-25         2021-01-27       hospitalisés
    7                   G        999           2017-01-01                NaT       hospitalisés

    >>> vo = merge_visits(
            vo,
            remove_deleted_visits=True,
            long_stay_threshold=timedelta(days=365),
            long_stay_filtering="all",
            max_timedelta=timedelta(hours=24),
            merge_different_hospitals=False,
            merge_different_source_values=["hospitalisés", "urgence"],
    )
    >>> vo
      visit_occurrence_id  person_id visit_start_datetime visit_end_datetime visit_source_value STAY_ID CONTIGUOUS_STAY_ID
    1                   A        999           2021-01-01         2021-01-05       hospitalisés       A                  A
    2                   B        999           2021-01-04         2021-01-08       hospitalisés       A                  A
    3                   C        999           2021-01-12         2021-01-18       hospitalisés       C                  C
    4                   D        999           2021-01-13         2021-01-14            urgence       C                  C
    5                   E        999           2021-01-19         2021-01-21       hospitalisés       C                  E
    6                   F        999           2021-01-25         2021-01-27       hospitalisés       F                  F
    7                   G        999           2017-01-01                NaT       hospitalisés       G                  G
    """

    # Preprocessing
    vo_to_merge, vo_to_not_merge = cleaning(
        vo,
        remove_deleted_visits=remove_deleted_visits,
        long_stay_threshold=long_stay_threshold,
        long_stay_filtering=long_stay_filtering,
        open_stay_end_datetime=open_stay_end_datetime
        if open_stay_end_datetime is not None
        else datetime.now(),
    )

    fw = get_framework(vo_to_merge)

    grouping_keys = ["person_id"]

    if not merge_different_hospitals:
        grouping_keys.append("care_site_id")

    if not merge_different_source_values:
        grouping_keys.append("visit_source_value")

    elif type(merge_different_source_values) == list:
        tmp = fw.DataFrame(
            data=dict(
                visit_source_value=merge_different_source_values,
                grouped_visit_source_value=True,
            )
        )
        vo_to_merge = vo_to_merge.merge(tmp, on="visit_source_value", how="left")
        vo_to_merge["grouped_visit_source_value"] = vo_to_merge[
            "grouped_visit_source_value"
        ].fillna(value=False)
        grouping_keys.append("grouped_visit_source_value")

    # Cartesian product
    merged = vo_to_merge.merge(
        vo_to_merge,
        on=grouping_keys,
        how="inner",
        suffixes=("_1", "_2"),
    )

    # Keeping only visits where 1 occurs before 2
    merged = merged[
        merged["visit_start_datetime_1"] <= merged["visit_start_datetime_2"]
    ]

    # Checking correct overlap
    th = max_timedelta.total_seconds()

    merged["overlap"] = substract_datetime(
        merged["visit_start_datetime_2"], merged["visit_end_datetime_calc_1"]
    )
    merged["to_merge"] = (merged["overlap"] <= th).astype(int)
    merged["contiguous"] = (merged["overlap"] <= 0).astype(int)

    def get_first(
        merged: DataFrame,
        contiguous_only: bool = False,
    ) -> Tuple[DataFrame, DataFrame]:
        """
        Returns a boolean flag for each visit, telling if the visit
        if the first of a stay.
        The ``contiguous_only`` parameter controls if the visits have to be
        contiguous in the stay
        """

        flag_col = "contiguous" if contiguous_only else "to_merge"
        flag_name = "1_is_first_contiguous" if contiguous_only else "1_is_first"
        concept_prefix = "CONTIGUOUS_" if contiguous_only else ""

        # If the only previous visit to be merged with is itself, we found our first visit !
        first_visits = merged.groupby("visit_occurrence_id_2")[flag_col].sum() == 1
        first_visits.name = flag_name

        # Adding this boolean flag to the merged DataFrame
        merged = merged.merge(
            first_visits,
            left_on="visit_occurrence_id_1",
            right_index=True,
            how="inner",
        )

        # Getting the corresponding first visit
        first_visit = (
            merged.sort_values(
                by=[flag_name, "visit_start_datetime_1"], ascending=[False, False]
            )
            .groupby("visit_occurrence_id_2")
            .first()["visit_occurrence_id_1"]
            .reset_index()
            .rename(
                columns={
                    "visit_occurrence_id_1": f"{concept_prefix}STAY_ID",
                    "visit_occurrence_id_2": "visit_occurrence_id",
                }
            )
        )

        return merged, first_visit

    merged, first_contiguous_visit = get_first(merged, contiguous_only=True)
    merged, first_visit = get_first(merged, contiguous_only=False)

    # Concatenating merge visits with previously discarded ones
    results = fw.concat(
        [
            vo_to_merge.merge(
                first_visit,
                on="visit_occurrence_id",
                how="inner",
            ).merge(
                first_contiguous_visit,
                on="visit_occurrence_id",
                how="inner",
            ),
            vo_to_not_merge,
        ]
    )

    # Adding visit_occurrence_id as STAY_ID and CONTIGUOUS_STAY_ID to discarded visits
    results["STAY_ID"] = results["STAY_ID"].combine_first(
        results["visit_occurrence_id"]
    )
    results["CONTIGUOUS_STAY_ID"] = results["CONTIGUOUS_STAY_ID"].combine_first(
        results["visit_occurrence_id"]
    )

    # Removing tmp columns

    vo = vo.drop(columns=["visit_end_datetime_calc"])

    return results.drop(
        columns=(
            set(results.columns)
            & set(["visit_end_datetime_calc", "grouped_visit_source_value"])
        )
    )


@algo_checker(algos=["sum_of_visits_duration", "visits_date_difference"])
@concept_checker(concepts=["STAY_DURATION"], only_adds_concepts=False)
def get_stays_duration(
    vo: DataFrame,
    algo: str = "sum_of_visits_duration",
    missing_end_date_handling: str = "fill",
    open_stay_end_datetime: Optional[datetime] = None,
) -> DataFrame:
    """
    Computes stay duration.
    The input DataFrame should contain the `STAY_ID` and `CONTIGUOUS_STAY_ID` columns,
    that can be computed via the `merge_visits()` function.

    Parameters
    ----------
    vo : DataFrame
        visit occurrence DataFrame with the `STAY_ID` and `CONTIGUOUS_STAY_ID` columns
    algo : str
        Which algo to use for computing stay durations. Available values are:

        - `"sum_of_visits_duration"`: The stay duration will correspond to the sum of each visit duration in the stay.
        - `"visits_date_difference"`: The stay duration will correspond to the difference between the end date of the last visit and the start date of the first visit.
    missing_end_date_handling : str
        How to handle visits with no end date. Available values are:

        - `"fill"`: Missing values are filled with `datetime.now()`
        - `"coerce"`: Missing values are handled as such, so duration of stays with open visits will be NaN.
    open_stay_end_datetime: Optional[datetime]
        Used if `missing_end_date_handling == "fill"`. Provide the `datetime` with which
        open stays should be ended. Leave to `None` in order to used `datetime.now()`

    Returns
    -------
    DataFrame
        *stay* DataFrame with `STAY_ID` as index, and the following columns:

        - `"person_id"`
        - `"t_start"`: The start date of the first visit of the stay
        - `"t_end"`: The end date of the last visit of the stay
        - `"STAY_DURATION"`: The duration (in hours) of the stay

    Raises
    ------
    MissingConceptError
        If `STAY_ID` and `CONTIGUOUS_STAY_ID` are not in the input columns.
    """

    if set(("STAY_ID", "CONTIGUOUS_STAY_ID")) - set(vo.columns):
        raise MissingConceptError(
            df_name="visit_occurence",
            required_concepts=[
                ("STAY_ID", "should be computed via 'merge_visits'"),
                ("CONTIGUOUS_STAY_ID", "should be computed via 'merge_visits'"),
            ],
        )

    if missing_end_date_handling == "fill":
        # Cannot use fillna() with datetime in Koalas
        if open_stay_end_datetime is None:
            open_stay_end_datetime = datetime.now()
        vo["visit_end_datetime_calc"] = open_stay_end_datetime
        vo["visit_end_datetime_calc"] = vo["visit_end_datetime"].combine_first(
            vo["visit_end_datetime_calc"]
        )
    elif missing_end_date_handling == "coerce":
        vo["visit_end_datetime_calc"] = vo["visit_end_datetime"]

    agg_dict = dict(
        person_id=("person_id", "first"),
        t_start=("visit_start_datetime", "min"),
        t_end=("visit_end_datetime_calc", "max"),
    )

    if algo == "sum_of_visits_duration":

        agg_dict["STAY_ID"] = ("STAY_ID", "first")

        contiguous_stays = vo.groupby("CONTIGUOUS_STAY_ID").agg(**agg_dict)
        contiguous_stays["CONTIGUOUS_STAY_DURATION"] = substract_datetime(
            contiguous_stays["t_end"], contiguous_stays["t_start"], out="hours"
        )

        agg_dict = dict(
            person_id=("person_id", "first"),
            t_start=("t_start", "min"),
            t_end=("t_end", "max"),
            STAY_DURATION=("CONTIGUOUS_STAY_DURATION", "sum"),
        )

        stays = contiguous_stays.groupby("STAY_ID").agg(**agg_dict)

    elif algo == "visits_date_difference":

        stays = vo.groupby("STAY_ID").agg(**agg_dict)
        stays["STAY_DURATION"] = substract_datetime(
            stays["t_end"], stays["t_start"], out="hours"
        )

    if missing_end_date_handling == "coerce":
        stays.loc[stays["t_end"].isna(), "STAY_DURATION"] = NaN

    return stays
