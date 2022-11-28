from copy import deepcopy

import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class SuicideAttemptDataset(Dataset):
    condition_occurrence: pd.DataFrame
    visit_occurrence: pd.DataFrame


def load_suicide_attempt():
    person_ids = [1, 1, 2, 3, 4]
    condition_source_values = ["X65", "S13", "S15", "E10", "X80"]
    condition_status_source_values = ["DAS", "DP", "DP", "DP", "DAS"]
    condition_start_datetimes = pd.to_datetime(["2010-01-01"] * 5)
    visit_occurrence_ids = [11, 11, 13, 14, 16]
    condition_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "condition_source_value": condition_source_values,
            "condition_status_source_value": condition_status_source_values,
            "condition_start_datetime": condition_start_datetimes,
            "visit_occurrence_id": visit_occurrence_ids,
        }
    )

    visit_occurrence_ids = [11, 12, 13, 14, 16]
    visit_start_datetimes = deepcopy(condition_start_datetimes)
    visit_end_datetimes = deepcopy(condition_start_datetimes)
    visit_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "visit_occurrence_id": visit_occurrence_ids,
            "visit_start_datetime": visit_start_datetimes,
            "visit_end_datetime": visit_end_datetimes,
        }
    )

    return SuicideAttemptDataset(
        condition_occurrence=condition_occurrence,
        visit_occurrence=visit_occurrence,
    )
