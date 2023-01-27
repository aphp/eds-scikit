from typing import List, Union

from loguru import logger

from eds_scikit.utils.typing import DataFrame


def select_cohort(
    measurement: DataFrame,
    studied_pop: Union[DataFrame, List[int]],
) -> DataFrame:
    """Select the patient_ids

    Parameters
    ----------
    measurement : DataFrame
        Target DataFrame
    studied_pop : Union[DataFrame, List[int]]
        List of patient_ids to select

    Returns
    -------
    DataFrame
        Filtered DataFrame with selected patients
    """
    logger.info("Selecting cohort...")

    if isinstance(studied_pop, DataFrame.__args__):
        filtered_measures = measurement.merge(
            studied_pop,
            on="person_id",
        )
    else:
        filtered_measures = measurement[measurement.person_id.isin(studied_pop)]

    return filtered_measures
