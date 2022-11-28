from datetime import datetime

import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class ICD10Dataset(Dataset):
    condition_occurrence: pd.DataFrame
    visit_occurrence: pd.DataFrame


def load_icd10():

    person_ids = [1] * 8
    condition_source_values = ["C10", "E112", "D20", "A20", "A21", "X20", "C10", "C10"]
    condition_start_datetimes = [
        2010,
        2010,
        2012,
        2020,
        2000,
        2000,
        2010,
        2010,
    ]
    condition_start_datetimes = [
        datetime(year, 1, 1) for year in condition_start_datetimes
    ]
    condition_status_source_values = ["DP", "DAS", "DAS", "DP", "DP", "DP", "DP", "DP"]
    visit_occurrence_ids = [11, 12, 13, 14, 15, 16, 16, 17]
    condition_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "condition_source_value": condition_source_values,
            "condition_start_datetime": condition_start_datetimes,
            "condition_status_source_value": condition_status_source_values,
            "visit_occurrence_id": visit_occurrence_ids,
        }
    )

    person_ids = [1] * 7
    visit_occurrence_ids = list(range(11, 18))
    visit_start_datetimes = [2010, 2010, 2012, 2020, 2020, 1900, 2050]
    visit_start_datetimes = [datetime(year, 1, 1) for year in visit_start_datetimes]
    visit_end_datetimes = [2010, 2010, 2012, 2020, 2020, 1900, 2050]
    visit_end_datetimes = [datetime(year, 1, 1) for year in visit_end_datetimes]
    visit_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "visit_occurrence_id": visit_occurrence_ids,
            "visit_start_datetime": visit_start_datetimes,
            "visit_end_datetime": visit_end_datetimes,
        }
    )

    return ICD10Dataset(
        condition_occurrence=condition_occurrence,
        visit_occurrence=visit_occurrence,
    )
