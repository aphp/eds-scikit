from eds_scikit.utils.checks import check_columns, check_tables
from eds_scikit.utils.typing import Data


def check_data_and_select_columns_measurement(data: Data):
    """Check the required tables and columns in the Data and extract them.

    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    """
    check_tables(
        data,
        required_tables=[
            "measurement",
            "concept",
            "concept_relationship",
        ],
    )

    _measurement_required_columns = [
        "measurement_id",
        "person_id",
        "visit_occurrence_id",
        "measurement_date",
        "measurement_datetime",
        "value_source_value",
        "value_as_number",
        "unit_source_value",
        "row_status_source_value",
        "measurement_source_concept_id",
        "range_high",
        "range_low",
    ]

    _concept_required_columns = [
        "concept_id",
        "concept_name",
        "concept_code",
        "vocabulary_id",
    ]

    _relationship_required_columns = ["concept_id_1", "concept_id_2", "relationship_id"]

    check_columns(
        data.measurement,
        required_columns=_measurement_required_columns,
    )
    check_columns(data.concept, required_columns=_concept_required_columns)
    check_columns(
        data.concept_relationship,
        required_columns=_relationship_required_columns,
    )

    measurement = data.measurement
    concept = data.concept[_concept_required_columns]
    concept_relationship = data.concept_relationship[_relationship_required_columns]

    return measurement, concept, concept_relationship


def check_data_and_select_columns_relationship(data: Data):
    """Check the required tables and columns in the Data and extract them.

    Parameters
    ----------
    data : Data
         Instantiated [``HiveData``][eds_scikit.io.hive.HiveData], [``PostgresData``][eds_scikit.io.postgres.PostgresData] or [``PandasData``][eds_scikit.io.files.PandasData]
    """
    check_tables(
        data,
        required_tables=[
            "concept",
            "concept_relationship",
        ],
    )

    _concept_required_columns = [
        "concept_id",
        "concept_name",
        "concept_code",
        "vocabulary_id",
    ]

    _relationship_required_columns = [
        "concept_id_1",
        "concept_id_2",
        "relationship_id",
    ]

    check_columns(data.concept, required_columns=_concept_required_columns)
    check_columns(
        data.concept_relationship,
        required_columns=_relationship_required_columns,
    )

    concept = data.concept[_concept_required_columns]
    concept_relationship = data.concept_relationship[_relationship_required_columns]

    return concept, concept_relationship
