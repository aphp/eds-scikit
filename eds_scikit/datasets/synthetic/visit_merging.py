import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class VisitDataset(Dataset):
    visit_occurrence: pd.DataFrame


def load_visit_merging():
    """
    Create a minimalistic dataset for the `visit_merging` function.

    Returns
    -------
    visit_dataset : VisitDataset, a dataclass comprised of
    visit_occurence.
    """
    visit_occurrence = pd.DataFrame(
        {
            "visit_occurrence_id": ["A", "B", "C", "D", "E", "F", "G"],
            "person_id": ["999"] * 7,
            "visit_start_datetime": [
                "2021-01-01",
                "2021-01-04",
                "2021-01-12",
                "2021-01-13",
                "2021-01-19",
                "2021-01-25",
                "2017-01-01",
            ],
            "visit_end_datetime": [
                "2021-01-05",
                "2021-01-08",
                "2021-01-18",
                "2021-01-14",
                "2021-01-21",
                "2021-01-27",
                None,
            ],
            "visit_source_value": [
                "hospitalisés",
                "hospitalisés",
                "hospitalisés",
                "urgence",
                "hospitalisés",
                "hospitalisés",
                "hospitalisés",
            ],
            "row_status_source_value": [
                "supprimé",
                "courant",
                "courant",
                "courant",
                "courant",
                "courant",
                "courant",
            ],
            "care_site_id": ["1", "1", "1", "1", "2", "1", "1"],
        }
    )

    for col in ["visit_start_datetime", "visit_end_datetime"]:
        visit_occurrence[col] = pd.to_datetime(visit_occurrence[col])

    return VisitDataset(visit_occurrence=visit_occurrence)
