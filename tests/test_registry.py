import pandas as pd

from eds_scikit.resources import registry


@registry.data("get_care_site_emergency_mapping.test")
def get_care_site_emergency_mapping():
    df = pd.DataFrame(
        data=dict(
            EMERGENCY_TYPE=[
                "Urgences pédiatriques",
                "Urgences générales adulte",
                "UHCD + Post-urgences",
                "Urgences spécialisées",
                "Consultation urgences",
                "SAMU / SMUR",
            ],
            care_site_source_value=[
                "source_1",
                "source_2",
                "source_3",
                "source_4",
                "source_5",
                "source_6",
            ],
        )
    )
    return df


@registry.data("get_care_site_hierarchy.test")
def get_care_site_hierarchy():
    df = pd.DataFrame(
        data={
            "care_site_id": [
                "batiment1",
                "secteur1",
                "secteur2",
                "unité1",
                "unité2",
            ],
            "Unité Fonctionnelle (UF)": [
                None,
                "secteur1",
                "secteur2",
                "secteur1",
                "secteur2",
            ],
        }
    )
    return df
