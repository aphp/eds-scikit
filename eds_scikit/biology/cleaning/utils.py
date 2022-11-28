from eds_scikit.utils.checks import check_columns, check_tables
from eds_scikit.utils.typing import Data


def check_the_data_for_cleaning(data: Data):
    """Check the required tables and columns in the Data

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
    check_columns(
        data.measurement,
        required_columns=[
            "measurement_id",
            "visit_occurrence_id",
            "measurement_date",
            "value_as_number",
            "unit_source_value",
            "row_status_source_value",
            "measurement_source_concept_id",
        ],
    )
    check_columns(
        data.concept,
        required_columns=[
            "concept_id",
            "concept_name",
            "concept_code",
            "vocabulary_id",
        ],
    )
    check_columns(
        data.concept_relationship,
        required_columns=["concept_id_1", "concept_id_2", "relationship_id"],
    )
