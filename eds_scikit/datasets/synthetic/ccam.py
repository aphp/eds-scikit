import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class CCAMDataset(Dataset):
    procedure_occurrence: pd.DataFrame
    visit_occurrence: pd.DataFrame


def load_ccam():
    """
    Create a minimalistic dataset for the `procedures_from_ccam` function.

    Returns
    -------
    ccam_dataset: CCAMDataset, a dataclass comprised of
        procedure_occurrence and visit_occurrence.
    """
    person_ids = [1, 1, 2, 3, 4, 5]
    procedure_source_values = [
        "DZEA001",
        "DZEA003",
        "GFEA004",
        "EQQF006",
        "DZEA001",
        "DZEA001",
    ]
    procedure_datetimes = pd.to_datetime(
        [
            "2010-01-01",
            "2010-01-01",
            "2012-01-01",
            "2012-01-01",
            "2012-01-01",
            "2012-01-01",
        ]
    )
    visit_occurrence_ids = [11, 12, 13, 14, 98, 99]
    procedure_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "procedure_source_value": procedure_source_values,
            "procedure_datetime": procedure_datetimes,
            "visit_occurrence_id": visit_occurrence_ids,
        }
    )

    person_ids = [1] * 6
    visit_occurrence_ids = [11, 12, 13, 14, 98, 99]
    visit_start_datetimes = pd.to_datetime(
        [
            "2010-01-01",
            "2010-01-01",
            "2012-01-01",
            "2020-01-01",
            "2000-01-01",
            "2050-01-01",
        ]
    )
    visit_end_datetimes = pd.to_datetime(
        [
            "2010-01-01",
            "2010-01-01",
            "2012-01-01",
            "2020-01-01",
            "2020-01-01",
            "1900-01-01",
        ]
    )
    visit_occurrence = pd.DataFrame(
        {
            "person_id": person_ids,
            "visit_occurrence_id": visit_occurrence_ids,
            "visit_start_datetime": visit_start_datetimes,
            "visit_end_datetime": visit_end_datetimes,
        }
    )

    return CCAMDataset(
        procedure_occurrence=procedure_occurrence,
        visit_occurrence=visit_occurrence,
    )
