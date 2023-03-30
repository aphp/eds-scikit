from typing import Dict

import pyspark.sql.types as T
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import udf as FunctionUDF

from eds_scikit.resources import registry

from .settings import (
    dict_code_UFR,
    i2b2_renaming,
    i2b2_tables,
    sex_cd_mapping,
    visit_type_mapping,
)


def get_i2b2_table(
    spark_session: SparkSession, db_name: str, db_source: str, table: str
) -> SparkDataFrame:
    """
    Convert a Spark table from i2b2 to OMOP format.

    Parameters
    ----------
    db_name: str
        Name of the database where the data is stored.
    table: str
        Name of the table to extract.

    Returns
    -------
    df: Spark DataFrame
        Spark DataFrame extracted from the i2b2 database given and converted to OMOP standard.
    """

    i2b2_table_name = i2b2_tables[db_source][table]
    # Dictionary of omop_col -> i2b2_col
    columns = i2b2_renaming.get(table)

    # Can be None if creating a table from scratch (e.g. concept_relationship
    if columns is not None:
        query = f"describe {db_name}.{i2b2_table_name}"
        available_columns = set(spark_session.sql(query).toPandas().col_name.tolist())
        if db_source == "cse":
            columns.pop("i2b2_action", None)
        cols = ", ".join(
            [
                f"{i2b2} AS {omop}"
                for omop, i2b2 in columns.items()
                if i2b2 in available_columns
            ]
        )
        query = f"SELECT {cols} FROM {db_name}.{i2b2_table_name}"
        df = spark_session.sql(query)

    # Special mapping for i2b2 :
    # CIM10
    if table == "condition_occurrence":
        df = df.withColumn(
            "condition_source_value",
            F.substring(F.col("condition_source_value"), 7, 20),
        )

    # CCAM
    elif table == "procedure_occurrence":
        df = df.withColumn(
            "procedure_source_value",
            F.substring(F.col("procedure_source_value"), 6, 20),
        )

    # Visits
    elif table == "visit_occurrence":
        df = df.withColumn(
            "visit_source_value",
            mapping_dict(visit_type_mapping, "Non Renseigné")(
                F.col("visit_source_value")
            ),
        )
        if db_source == "cse":
            df = df.withColumn("row_status_source_value", F.lit("Actif"))
            df = df.withColumn(
                "visit_occurrence_source_value", df["visit_occurrence_id"]
            )
        else:
            df = df.withColumn(
                "row_status_source_value",
                F.when(
                    F.col("row_status_source_value").isin([-1, -2]), "supprimé"
                ).otherwise("Actif"),
            )
        # Retrieve Hospital trigram
        ufr = spark_session.sql(
            f"SELECT * FROM {db_name}.{i2b2_tables[db_source]['visit_detail']}"
        )
        ufr = ufr.withColumn(
            "care_site_id",
            F.substring(F.split(F.col("concept_cd"), ":").getItem(1), 1, 3),
        )
        ufr = ufr.withColumnRenamed("encounter_num", "visit_occurrence_id")
        ufr = ufr.drop_duplicates(subset=["visit_occurrence_id"])
        ufr = ufr.select(["visit_occurrence_id", "care_site_id"])
        df = df.join(ufr, how="inner", on=["visit_occurrence_id"])

    # Patients
    elif table == "person":
        df = df.withColumn(
            "gender_source_value",
            mapping_dict(sex_cd_mapping, "Non Renseigné")(F.col("gender_source_value")),
        )

    # Documents
    elif table.startswith("note"):
        df = df.withColumn(
            "note_class_source_value",
            F.substring(F.col("note_class_source_value"), 4, 100),
        )
        if db_source == "cse":
            df = df.withColumn("row_status_source_value", F.lit("Actif"))
        else:
            df = df.withColumn(
                "row_status_source_value",
                F.when(F.col("row_status_source_value") < 0, "SUPP").otherwise("Actif"),
            )

    # Hospital trigrams
    elif table == "care_site":
        df = df.withColumn("care_site_type_source_value", F.lit("Hôpital"))
        df = df.withColumn(
            "care_site_source_value",
            F.split(F.col("care_site_source_value"), ":").getItem(1),
        )
        df = df.withColumn(
            "care_site_id", F.substring(F.col("care_site_source_value"), 1, 3)
        )
        df = df.drop_duplicates(subset=["care_site_id"])
        df = df.withColumn(
            "care_site_short_name",
            mapping_dict(dict_code_UFR, "Non Renseigné")(F.col("care_site_id")),
        )

    # UFR
    elif table == "visit_detail":
        df = df.withColumn(
            "care_site_id", F.split(F.col("care_site_id"), ":").getItem(1)
        )
        df = df.withColumn("visit_detail_type_source_value", F.lit("PASS"))
        df = df.withColumn("row_status_source_value", F.lit("Actif"))

    # measurement
    elif table == "measurement":
        df = df.withColumn(
            "measurement_source_concept_id",
            F.substring(F.col("measurement_source_concept_id"), 5, 20),
        ).withColumn("row_status_source_value", F.lit("Validé"))

    # concept
    elif table == "concept":
        df = (
            df.withColumn(
                "concept_source_value",
                F.substring(
                    F.col("concept_source_value"), 5, 20
                ),  # TODO: use regexp_extract to take substring after ':'
            )
            .withColumn("concept_id", F.col("concept_source_value"))
            .withColumn("concept_code", F.col("concept_id"))
            .withColumn("vocabulary_id", F.lit("ANABIO"))
        )

        # Adding LOINC
        if "get_additional_i2b2_concept" in registry.data.get_all():
            loinc_pd = registry.get("data", "get_additional_i2b2_concept")()
            assert len(loinc_pd.columns) == len(df.columns)
            loinc_pd = loinc_pd[df.columns]  # for columns ordering
            df = df.union(
                spark_session.createDataFrame(loinc_pd, df.schema, verifySchema=False)
            ).cache()

    # fact_relationship
    elif table == "fact_relationship":
        # Retrieve UF information
        df = df.withColumn(
            "fact_id_1",
            F.split(F.col("care_site_source_value"), ":").getItem(1),
        )
        df = df.withColumn("domain_concept_id_1", F.lit(57))  # Care_site domain

        # Retrieve hospital information
        df = df.withColumn("fact_id_2", F.substring(F.col("fact_id_1"), 1, 3))
        df = df.withColumn("domain_concept_id_2", F.lit(57))  # Care_site domain
        df = df.drop_duplicates(subset=["fact_id_1", "fact_id_2"])

        # Only UF-Hospital relationships in i2b2
        df = df.withColumn("relationship_concept_id", F.lit(46233688))  # Included in

    elif table == "concept_relationship":
        data = []
        schema = T.StructType(
            [
                T.StructField("concept_id_1", T.StringType(), True),
                T.StructField("concept_id_2", T.StringType(), True),
                T.StructField("relationship_id", T.StringType(), True),
            ]
        )
        if "get_additional_i2b2_concept_relationship" in registry.data.get_all():
            data = registry.get("data", "get_additional_i2b2_concept_relationship")()
        df = spark_session.createDataFrame(data, schema).cache()
    return df


def mapping_dict(mapping: Dict[str, str], default: str) -> FunctionUDF:
    """
    Returns a function that maps data according to a mapping dictionnary in a Spark DataFrame.

    Parameters
    ----------
    mapping: Dict
        Mapping dictionnary
    default: str
        Value to return if the function input is not find in the mapping dictionnary.

    Returns
    -------
    Callable
        Function that maps the values of Spark DataFrame column.
    """

    def f(x):
        return mapping.get(x, default)

    return F.udf(f)
