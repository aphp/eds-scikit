from datetime import datetime

import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class TaggingDataset(Dataset):
    events: pd.DataFrame
    tags: pd.DataFrame


def load_tagging():
    events = pd.DataFrame(
        [
            {
                "person_id": 1,
                "t_start": datetime(2019, 1, 1),
                "t_end": datetime(2020, 1, 1),
                "concept": "CIM10_INFARCTUS",
                "value": "E210",
            }
        ]
    )

    person_ids = [1] * 6
    t_start = pd.to_datetime(
        [
            "2018-01-01",
            "2019-06-01",
            "2018-06-01",
            "2019-06-01",
            "2010-06-01",
            "2030-06-01",
        ]
    )
    t_end = pd.to_datetime(
        [
            "2021-01-01",
            "2021-01-01",
            "2019-06-01",
            "2019-07-01",
            "2011-01-01",
            "2031-01-01",
        ]
    )
    concepts = ["CIM10_DIABETE"] * 6
    values = [
        "event_in_tag",
        "intersect_right",
        "intersect_left",
        "tag_in_event",
        "outside_left",
        "outside_right",
    ]
    tags = pd.DataFrame(
        {
            "person_id": person_ids,
            "t_start": t_start,
            "t_end": t_end,
            "concept": concepts,
            "value": values,
        }
    )

    return TaggingDataset(events=events, tags=tags)
