from datetime import datetime
from typing import List

import numpy as np
import pandas as pd
from databricks import koalas as ks

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class BiologyDataset(Dataset):
    measurement: pd.DataFrame
    concept: pd.DataFrame
    concept_relationship: pd.DataFrame
    visit_occurrence: pd.DataFrame
    care_site: pd.DataFrame
    available_tables: List[str]
    t_start: datetime
    t_end: datetime
    module: str

    def convert_to_koalas(self):
        if self.module == "pandas":
            self.pd_measurement = self.measurement
            self.pd_concept = self.concept
            self.pd_concept_relationship = self.concept_relationship
            self.pd_care_site = self.care_site
            self.pd_visit_occurrence = self.visit_occurrence
            self.measurement = ks.DataFrame(self.measurement)
            self.concept = ks.DataFrame(self.concept)
            self.concept_relationship = ks.DataFrame(self.concept_relationship)
            self.care_site = ks.DataFrame(self.care_site)
            self.visit_occurrence = ks.DataFrame(self.visit_occurrence)
            self.module = "koalas"

    def reset_to_pandas(self):
        if self.module == "koalas":
            self.measurement = self.pd_measurement
            self.concept = self.pd_concept
            self.concept_relationship = self.pd_concept_relationship
            self.care_site = self.pd_care_site
            self.visit_occurrence = self.pd_visit_occurrence
            self.module = "pandas"


def load_biology_data(
    n_entity: int = 5,
    mean_measurement: int = 10000,
    n_care_site: int = 5,
    n_person: int = 5,
    n_visit_occurrence: int = 5,
    units: List[str] = ["g", "g/l", "mol", "s"],
    row_status_source_values: List[str] = [
        "Validé",
        "Discontinué",
        "Disponible",
        "Attendu",
        "Confirmé",
        "Initial",
    ],
    t_start: datetime = datetime(2017, 1, 1),
    t_end: datetime = datetime(2022, 1, 1),
    seed: int = None,
):
    """
    Create a minimalistic dataset for the `bioclean` function.

    Returns
    -------
    biology_dataset: BiologyDataset, a dataclass comprised of
        measurement, concept and concept_relationship.
    """
    if seed:
        np.random.seed(seed=seed)

    concept, concept_relationship, src_concept_name = _generate_concept(
        n_entity=n_entity, units=units
    )
    measurement = _generate_measurement(
        t_start=t_start,
        t_end=t_end,
        mean_measurement=mean_measurement,
        units=units,
        src_concept_name=src_concept_name,
        n_visit_occurrence=n_visit_occurrence,
        n_person=n_person,
        row_status_source_values=row_status_source_values,
    )
    care_site = _generate_care_site(n_care_site=n_care_site)
    visit_occurrence = _generate_visit_occurrence(
        n_visit_occurrence=n_visit_occurrence, n_care_site=n_care_site
    )

    return BiologyDataset(
        measurement=measurement,
        concept=concept,
        concept_relationship=concept_relationship,
        visit_occurrence=visit_occurrence,
        care_site=care_site,
        available_tables=[
            "measurement",
            "concept",
            "concept_relationship",
            "visit_occurrence",
            "care_site",
        ],
        t_start=t_start,
        t_end=t_end,
        module="pandas",
    )


def _generate_concept(n_entity: int, units: List[str]):

    loinc_concept_code = []
    anabio_concept_code = []
    src_concept_code = []
    loinc_concept_name = []
    anabio_concept_name = []
    src_concept_name = []
    concept_id_1 = []
    concept_id_2 = []
    for i in range(n_entity):
        n_loinc = np.random.randint(1, 4)
        loinc_codes = [str(i) + str(j) + "-0" for j in range(n_loinc)]
        loinc_concept_code.extend(loinc_codes)
        unit_values = np.random.choice(units, n_loinc)
        for loinc_code in loinc_codes:
            unit_value = np.random.choice(unit_values)
            n_anabio = np.random.randint(1, 3)
            supp_code = "9" if len(str(i)) == 1 else ""
            anabio_codes = [
                "A" + loinc_code.split("-")[0] + str(j) + supp_code
                for j in range(n_anabio)
            ]
            anabio_concept_code.extend(anabio_codes)
            loinc_concept_name.append("LOINC_" + loinc_code + "_" + unit_value)
            anabio_concept_name.extend(
                [
                    "ANABIO_" + anabio_code + "_" + unit_value
                    for anabio_code in anabio_codes
                ]
            )
            for anabio_code in anabio_codes:
                n_src = np.random.randint(1, 3)
                src_codes = [
                    loinc_code + "-" + anabio_code + "-" + str(j) for j in range(n_src)
                ]
                src_concept_code.extend(src_codes)
                src_concept_name.extend(
                    ["SRC_" + src_code + "_" + unit_value for src_code in src_codes]
                )
                for src_code in src_codes:
                    concept_id_1.extend([src_code] * 2)
                    concept_id_2.extend([anabio_code, loinc_code])

    src_vocabulary_id = ["GLIMS"] * len(src_concept_code)
    anabio_vocabulary_id = ["ANABIO"] * len(anabio_concept_code)
    loinc_vocabulary_id = list(
        np.random.choice(
            ["LOINC", "APHP - ITM - LOINC"], size=len(loinc_concept_code), p=[0.9, 0.1]
        )
    )

    concept_code = src_concept_code + anabio_concept_code + loinc_concept_code
    concept_name = src_concept_name + anabio_concept_name + loinc_concept_name
    vocabulary_id = src_vocabulary_id + anabio_vocabulary_id + loinc_vocabulary_id

    concept = pd.DataFrame(
        {
            "concept_id": concept_code,
            "concept_code": concept_code,
            "concept_name": concept_name,
            "vocabulary_id": vocabulary_id,
        }
    )

    concept_relationship = pd.DataFrame(
        {
            "concept_id_1": concept_id_1,
            "concept_id_2": concept_id_2,
            "relationship_id": ["Maps to"] * len(concept_id_1),
        }
    )

    return concept, concept_relationship, src_concept_name


def _generate_care_site(
    n_care_site: int,
):
    care_site_id = range(n_care_site)
    care_site_short_name = ["Hospital_" + str(i) for i in range(n_care_site)]
    care_site = pd.DataFrame(
        {
            "care_site_id": care_site_id,
            "care_site_short_name": care_site_short_name,
        }
    )

    return care_site


def _generate_visit_occurrence(
    n_visit_occurrence: int,
    n_care_site: int,
):

    care_site_id = np.random.randint(n_care_site, size=n_visit_occurrence)
    visit_occurrence_id = range(n_visit_occurrence)

    visit_occurrence = pd.DataFrame(
        {
            "visit_occurrence_id": visit_occurrence_id,
            "care_site_id": care_site_id,
        }
    )
    return visit_occurrence


def _generate_measurement(
    t_start: int,
    t_end: int,
    mean_measurement: int,
    src_concept_name: List[str],
    n_visit_occurrence: int,
    units: List[str],
    n_person: int = 50,
    row_status_source_values: List[str] = [
        "Validé",
        "Discontinué",
        "Disponible",
        "Attendu",
        "Confirmé",
        "Initial",
    ],
):
    measurement_datetime = []
    measurement_date = []
    measurement_source_concept_id = []
    unit_source_value = []
    value_as_number = []
    row_status_source_value = []
    visit_occurrence_id = []
    person_id = []
    for concept_name in src_concept_name:
        valid_measurement = int(
            np.random.normal(mean_measurement, mean_measurement / 5)
        )
        missing_value = int(np.random.uniform(1, valid_measurement / 10))
        n_measurement = valid_measurement + missing_value
        concept_code = concept_name.split("_")[1]
        unit = concept_name.split("_")[-1]
        mean_value = (1 + units.index(unit)) * 2
        std_value = 1

        visit_occurrence_id.extend(
            np.random.randint(n_visit_occurrence, size=n_measurement)
        )
        person_id.extend(np.random.randint(n_person, size=n_measurement))
        row_status_source_value.extend(
            np.random.choice(
                row_status_source_values,
                n_measurement,
                p=[0.95, 0.01, 0.01, 0.01, 0.01, 0.01],
            )
        )
        value_as_number.extend(
            np.random.normal(mean_value, std_value, valid_measurement)
        )
        value_as_number.extend([None] * missing_value)
        unit_source_value.extend([unit] * n_measurement)
        measurement_source_concept_id.extend([concept_code] * n_measurement)
        datetimes = pd.to_datetime(
            pd.Series(
                np.random.randint(t_start.timestamp(), t_end.timestamp(), n_measurement)
            ),
            unit="s",
        )
        measurement_datetime.extend(datetimes)
        measurement_date.extend(datetimes[:valid_measurement])
        measurement_date.extend([None] * missing_value)

    value_source_value = [
        "{} {}".format(a, b) for a, b in zip(value_as_number, unit_source_value)
    ]

    measurement = pd.DataFrame(
        {
            "measurement_id": range(len(visit_occurrence_id)),
            "person_id": person_id,
            "visit_occurrence_id": visit_occurrence_id,
            "measurement_datetime": measurement_datetime,
            "measurement_date": measurement_date,
            "value_as_number": value_as_number,
            "value_source_value": value_source_value,
            "unit_source_value": unit_source_value,
            "row_status_source_value": row_status_source_value,
            "measurement_source_concept_id": measurement_source_concept_id,
        }
    )

    return measurement
