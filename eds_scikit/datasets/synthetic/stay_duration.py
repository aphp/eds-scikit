import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class StayDurationDataset(Dataset):
    stays: pd.DataFrame


def load_stay_duration():
    visit_occurrence_ids = ["A", "B", "C", "D", "E", "F"]
    person_ids = [999] * 6
    visit_start_datetimes = pd.to_datetime(
        [
            "2021-01-01",
            "2021-01-04",
            "2021-01-13",
            "2021-01-19",
            "2021-01-22",
            "2017-01-01",
        ]
    )
    visit_end_datetimes = pd.to_datetime(
        [
            "2021-01-05",
            "2021-01-08",
            "2021-01-14",
            "2021-01-21",
            "2021-01-27",
            None,
        ]
    )
    stay_ids = ["A", "A", "C", "D", "D", "F"]
    contiguous_stay_ids = ["A", "A", "C", "D", "E", "F"]
    stays = pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "person_id": person_ids,
            "visit_start_datetime": visit_start_datetimes,
            "visit_end_datetime": visit_end_datetimes,
            "STAY_ID": stay_ids,
            "CONTIGUOUS_STAY_ID": contiguous_stay_ids,
        }
    )

    return StayDurationDataset(stays=stays)
