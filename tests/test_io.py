import os

import pytest
from databricks import koalas as ks

from eds_scikit import io
from eds_scikit.utils.test_utils import make_df

# from eds_scikit.utils import framework as to

pytestmark = pytest.mark.koalas

DATA_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
DATABASE = "test_io_database"


@pytest.fixture(scope="module", autouse=True)
def load_tables(spark_session):
    prepare_database(spark_session)

    tables = [
        os.path.join(DATA_FOLDER, filename)
        for filename in os.listdir(DATA_FOLDER)
        if filename.endswith(".csv")
    ]
    for table in tables:
        load_table(table)
    spark_session.sql("use default")

    yield
    # Teardown
    # The code below is executed after all the tests
    spark_session.sql(f"drop database if exists {DATABASE} cascade")


def prepare_database(spark_session):
    # print(spark_session.sql(f"DESCRIBE DATABASE EXTENDED {DATABASE}").collect())
    spark_session.sql(f"drop database if exists {DATABASE} cascade")
    spark_session.sql(f"create database {DATABASE}")
    spark_session.sql(f"use {DATABASE}")


def load_table(abspath):
    # Note: instead of koalas, we could also use here
    # spark_session.sql("CREATE TABLE src (key INT, value STRING)")
    table_name, _ = os.path.splitext(os.path.basename(abspath))
    with open(abspath, "r") as f:
        csv_text = f.read()
        pd_df = make_df(csv_text)
        ks_df = ks.from_pandas(pd_df)
        ks_df.to_table(table_name, mode="overwrite")


def test_something_with_spark_session(spark_session):
    result = (
        spark_session.sql(f"Select count(*) as count from {DATABASE}.person")
        .select("count")
        .collect()
    )
    assert result[0]["count"] == 3


def test_HiveData(spark_session):
    data = io.HiveData(database_name=DATABASE, spark_session=spark_session)
    assert data.available_tables == ["person"]
    assert hasattr(data, "person")
    person = data.person
    assert isinstance(person, ks.DataFrame)
    assert person.shape[0] > 2
