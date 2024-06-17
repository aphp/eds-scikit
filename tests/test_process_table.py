import pandas as pd
import pytest

from eds_scikit.utils import framework
from eds_scikit.utils.process_table import (
    tag_table_by_type,
    tag_table_period_length,
    tag_table_with_age,
)

# Generate random data for the first dataframe
num_rows = 1000
table = {
    "condition_source_value": ["E100", "E101", "E110", "A001", "B002"],
    "visit_start_datetime": [
        "2021-05-16",
        "2018-08-16",
        "2023-03-14",
        "2023-05-09",
        "2022-07-17",
    ],
    "visit_end_datetime": [
        "2021-05-26",
        "2018-09-16",
        "2023-03-15",
        "2023-10-10",
        "2022-07-18",
    ],
    "person_id": [0, 1, 2, 3, 4],
}

table = pd.DataFrame(table)
table["visit_start_datetime"] = pd.to_datetime(table["visit_start_datetime"])
table["visit_end_datetime"] = pd.to_datetime(table["visit_end_datetime"])

# Generate random data for the second dataframe
person = {
    "person_id": [0, 1, 2, 3, 4],
    "birth_datetime": [
        "2000-03-29",
        "1990-04-08",
        "1975-09-28",
        "1970-04-28",
        "1975-10-03",
    ],
}
person["birth_datetime"] = pd.to_datetime(person["birth_datetime"])

person = pd.DataFrame(person)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_tag_table_with_age(module):

    person_fr = framework.to(module, person)
    table_fr = framework.to(module, table)

    table_with_age = tag_table_with_age(
        table_fr, "visit_start_datetime", person_fr, age_ranges=[24, 30, 40]
    )
    table_with_age = framework.to("pandas", table_with_age)
    assert (
        table_with_age["age_range"]
        == pd.Series(
            ["age <= 24", "24 < age <= 30", "age > 40", "age > 40", "age > 40"],
            name="age_range",
        )
    ).all()

    table_with_age = tag_table_with_age(
        table_fr, "visit_start_datetime", person_fr, age_ranges=None
    )
    table_with_age = framework.to("pandas", table_with_age)
    assert (table_with_age["age"] == pd.Series([21, 29, 48, 54, 48], name="age")).all()


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_table_by_type(module):

    table_fr = framework.to(module, table)

    table_by_type = tag_table_by_type(
        table_fr,
        type_groups={"DIABETES_TYPE_I": r"^E10", "DIABETES_TYPE_II": r"^E11"},
        source_col="condition_source_value",
        target_col="tag",
    )
    table_by_type = framework.to("pandas", table_by_type)
    assert (
        table_by_type["tag"]
        == pd.Series(
            [
                "DIABETES_TYPE_I",
                "DIABETES_TYPE_I",
                "DIABETES_TYPE_II",
                "OTHER",
                "OTHER",
            ],
            name="tag",
        )
    ).all()
    table_by_type = tag_table_by_type(
        table_fr,
        type_groups={"DIABETES_TYPE_I": r"^E10", "DIABETES_TYPE_II": r"^E11"},
        source_col="condition_source_value",
        target_col="tag",
        filter_table=True,
    )
    table_by_type = framework.to("pandas", table_by_type)
    assert (
        table_by_type["tag"]
        == pd.Series(
            ["DIABETES_TYPE_I", "DIABETES_TYPE_I", "DIABETES_TYPE_II"], name="tag"
        )
    ).all()


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_tag_table_period_length(module):

    table_fr = framework.to(module, table)

    table_period_length = tag_table_period_length(table_fr, length_of_stays=[7, 14])
    table_period_length = framework.to("pandas", table_period_length)
    assert (
        table_period_length["length_of_stay"]
        == pd.Series(
            ["7 days - 14 days", ">= 14 days", "<= 7 days", ">= 14 days", "<= 7 days"],
            name="tag",
        )
    ).all()
