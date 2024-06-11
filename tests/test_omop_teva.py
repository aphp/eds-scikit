import numpy as np
import pandas as pd
import pytest

from eds_scikit.plot import generate_omop_teva, reduce_table, visualize_table
from eds_scikit.utils import framework

from .teva_config_test import teva_config_test


class Data:
    def __init__(self, module):
        self.visit_occurrence = pd.read_parquet("tests/data/visit_occurrence")
        self.visit_occurrence = framework.to(module, self.visit_occurrence)
        self.care_site = pd.read_parquet("tests/data/care_site")
        self.care_site = framework.to(module, self.care_site)
        self.condition_occurrence = pd.read_parquet("tests/data/condition_occurrence")
        self.condition_occurrence = framework.to(module, self.condition_occurrence)
        self.note = pd.read_parquet("tests/data/note")
        self.note = framework.to(module, self.note)

    def _read_table(self, table_name: str):
        return getattr(self, table_name)


class WrongData:
    def __init__(self, module):
        self.note = pd.read_parquet("tests/data/note")
        self.note = framework.to(module, self.note)

    def _read_table(self, table_name: str):
        return getattr(self, table_name)


dataframe = pd.DataFrame(
    {
        "id": str(np.arange(1, 1001)),
        "category_1": np.random.choice(["A", "B", "C"], size=1000, p=[0.4, 0.3, 0.3]),
        "category_2": np.array([str(i) for i in range(500)] * 2),
        "location": np.random.choice(
            ["location 1", "location 2"], size=1000, p=[0.6, 0.4]
        ),
        "date": pd.to_datetime(
            np.random.choice(
                pd.date_range(start="2021-01-01", end="2022-01-01"), size=1000
            )
        ),
    }
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_omop_teva(module):

    data_fr = framework.to(module, dataframe)

    data_reduced = reduce_table(
        data_fr,
        category_columns=["location", "category_1", "category_2", "category_3"],
        date_column="date",
        start_date="2021-01-01",
        end_date="2021-12-01",
        mapper={"category_2": {"even": r"[02468]$", "odd": r"[13579]$"}},
    )

    visualize_table(data_reduced, title="synthetic dataframe table", description=True)

    data = Data(module)

    generate_omop_teva(
        data,
        start_date="2011-01-01",
        end_date="2020-01-01",
        teva_config=teva_config_test,
    )

    with pytest.raises(Exception):
        generate_omop_teva(
            WrongData(module),
            start_date="2011-01-01",
            end_date="2020-01-01",
            teva_config={
                k: v for k, v in teva_config_test.items() if k != "visit_occurrence"
            },
        )
