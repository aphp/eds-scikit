from datetime import datetime

import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class ConsultationDataset(Dataset):
    visit_occurrence: pd.DataFrame
    note: pd.DataFrame
    note_nlp: pd.DataFrame


def load_consultation_dates():
    """
    Create a minimalistic dataset for the `get_consultation_dates` function.

    Returns
    -------
    consultation_dataset: ConsultationDataset, a dataclass comprised of
        visit_occurence, note and note_nlp.
    """
    n_visits = 4
    visit_occurrence_ids = list(range(n_visits))
    visit_source_value = [
        "consultation externe",
        "consultation externe",
        "hospitalisation",
        "consultation externe",
    ]
    visit_occurrence = pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "visit_source_value": visit_source_value,
        }
    )

    n_notes = 10
    visit_occurrence_ids = [n_visits * idx // n_notes for idx in range(n_notes)]
    note_ids = list(range(n_notes))
    note_datetimes = [1, 1, 5, 6, 7, 1, 1, 2, 3, 8]
    note_datetimes = [datetime(2020, 1, day) for day in note_datetimes]
    note_class_source_value = (n_notes // 2) * ["CR-CONS"] + (n_notes // 2) * [
        "CR-HOSP"
    ]
    note = pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_ids,
            "note_id": note_ids,
            "note_datetime": note_datetimes,
            "note_class_source_value": note_class_source_value,
        }
    )

    n_note_nlp = 20
    starts = [
        4,
        14,
        0,
        7,
        5,
        11,
        8,
        18,
        6,
        19,
        15,
        9,
        17,
        1,
        12,
        2,
        3,
        16,
        10,
        13,
    ]
    note_ids = [n_notes * idx // n_note_nlp for idx in range(n_note_nlp)]
    consultation_dates = 2 * [1, 1, 5, 6, 7, 1, 2, 3, 9, 12]
    consultation_dates = [datetime(2020, 1, day) for day in consultation_dates]
    note_nlp = pd.DataFrame(
        {
            "note_id": note_ids,
            "consultation_date": consultation_dates,
            "start": starts,
        }
    )

    return ConsultationDataset(
        visit_occurrence=visit_occurrence,
        note=note,
        note_nlp=note_nlp,
    )
