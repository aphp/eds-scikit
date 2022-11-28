import logging
import os

import pandas as pd
import pytest
from _pytest.logging import caplog as _caplog  # noqa F401
from databricks import koalas as ks
from loguru import logger

from eds_scikit import improve_performances

from . import test_registry  # noqa: F401 --> To register functions


def configure_environment_in_jupyterlab():
    # SUR LE CLUSTER JUPYTERLAB
    # a priori ce n'est plus la peine de modifier le pythonpath
    # : ce qui compte c'est d'utiliser pyspark==2.4.3
    # import sys
    # sys.path.insert(0, "/usr/hdp/current/spark2.4.3-client/python")
    # sys.path.insert(0, "/usr/hdp/current/spark2.4.3-client/python/lib/py4j-0.10.7-src.zip")

    # Attention: SPARK_HOME est mal définit par défaut dans le terminal jupyterlab
    spark_home_eds = "/usr/hdp/current/spark2.4.3-client/"
    if os.path.exists(spark_home_eds):
        os.environ["SPARK_HOME"] = spark_home_eds
    # Je pensais que le fait de définir le JAVA_HOME (et pas SPARK_HOME) aurait
    # suffit mais je n'arrive pas à lancer les tests avec cette config:
    # java_home_eds = "/usr/jdk64/jdk1.8.0_112/"
    # if os.path.exists(java_home_eds):
    #     os.environ["JAVA_HOME"] = java_home_eds

    # EN LOCAL SUR MON MACBOOK
    # Après mon installation locale de java 8 (brew install openjdk@8)
    # je n'ai pas besoin de définir la variable d'environnement JAVA_HOME
    # puisque `java` existe comme exécutable dans mon terminal
    # s.environ["JAVA_HOME"] = "/usr/local/opt/openjdk/"

    pass


configure_environment_in_jupyterlab()


@pytest.fixture
def caplog(_caplog):  # noqa F811
    """
    To capture loguru's logs
    """

    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    logger.add(PropogateHandler(), format="{message}")
    yield _caplog


def pytest_collection_modifyitems(session, config, items):
    # adding the marker "koalas" to all tests that use the "[koalas]" framework in parametrize
    for item in items:
        if "koalas" in item.name:
            item.add_marker("koalas")


@pytest.fixture(
    scope="session",
    autouse=True,
)
def spark_session(pytestconfig, tmpdir_factory):

    if "not koalas" in pytestconfig.getoption("-m"):
        # I could not find a way to look at all the markers from the selected tests
        # I am using the command line option instead
        yield
    else:
        print("!! Creating spark session !!")

        from pyspark import SparkConf

        temp_warehouse_dir = tmpdir_factory.mktemp("spark")
        conf = (
            SparkConf()
            .setMaster("local")
            .setAppName("testing")
            # used to overwrite hive tables
            .set(
                "spark.sql.legacy.allowCreatingManagedTableUsingNonemptyLocation",
                "true",
            )
            # Path to data and metastore
            # Note: the option "hive.metastore.warehouse.dir" is deprecated
            # But javax.jdo.option.ConnectionURL can be used for the path of 'metastrore_db'
            # https://stackoverflow.com/questions/31459439/testing-hive-spark-python-programs-locally
            .set("spark.sql.warehouse.dir", temp_warehouse_dir)
            .set("spark.sql.execution.arrow.enabled", "true")
            .set("spark.default.parallelism", 1)
            .set("spark.sql.shuffle.partitions", 1)
            .set(
                "javax.jdo.option.ConnectionURL",
                f"jdbc:derby:;databaseName={temp_warehouse_dir}/metastore_db;create=true",
            )
        )

        session, _, _ = improve_performances(to_add_conf=list(conf.getAll()))

        # session is ready
        yield session

        # Teardown
        session.stop()


@pytest.fixture(
    autouse=True,
)
def example_objects():
    return dict(
        pandas=[
            pd.DataFrame({"col": [1, 2, 3]}),
            pd.Series([4, 5, 6]),
        ],
        koalas=[
            ks.DataFrame({"val": [7, 8, 9]}),
            ks.Series([10, 11, 12]),
        ],
    )
