import numpy as np
import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class PersonDataset(Dataset):
    person: pd.DataFrame


def load_person(N=100):
    gender = np.random.choice(["m", "f"], size=N)
    birth_datetime = np.random.randint(1920, 2022, size=N)
    person_id = list(range(N))

    person = pd.DataFrame(
        dict(
            person_id=person_id,
            gender_source_value=gender,
            birth_datetime=birth_datetime,
        )
    )
    person["birth_datetime"] = pd.to_datetime(person["birth_datetime"], format="%Y")

    return PersonDataset(person=person)
