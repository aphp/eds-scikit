import importlib
import os
import sys
import time
from packaging import version
from typing import List, Tuple
from pathlib import Path

import pyarrow
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

BASE_DIR = Path(__file__).parent

def load_koalas():

    ks = sys.modules.get("databricks.koalas", None)

    if ks is not None:
        importlib.reload(ks)

    else:
        import databricks.koalas as ks

    return ks


def koalas_options() -> None:
    """
    Set necessary options to optimise Koalas
    """

    # Reloading Koalas to use the new configuration
    ks = load_koalas()

    ks.set_option("compute.default_index_type", "distributed")
    ks.set_option("compute.ops_on_diff_frames", True)
    ks.set_option("display.max_rows", 50)

def set_env_variables() -> None:
    # From https://github.com/databricks/koalas/blob/master/databricks/koalas/__init__.py
    if version.parse(pyspark.__version__) < version.parse("3.0"):
        if version.parse(pyarrow.__version__) >= version.parse("0.15"):
            os.environ["ARROW_PRE_0_15_IPC_FORMAT"] = "1"

    if version.parse(pyarrow.__version__) >= version.parse("2.0.0"):
        os.environ["PYARROW_IGNORE_TIMEZONE"] = "0"

def improve_performances(
    to_add_conf: List[Tuple[str, str]] = [],
    quiet_spark: bool = True,
    app_name: str = "",
) -> Tuple[SparkSession, SparkContext, SparkSession.sql]:
    """
    (Re)defines various Spark variable with some configuration changes
    to improve performances by enabling Arrow
    This has to be done
    - Before launching a SparkCOntext
    - Before importing Koalas
    Those two points are being taken care on this function.
    If a SparkSession already exists, it will copy its configuration before
    creating a new one

    Returns
    -------
    Tuple of
    - A SparkSession
    - The associated SparkContext
    - The associated ``sql`` object to run SQL queries
    """

    # Check if a spark Session is up
    global spark, sc, sql

    spark = SparkSession.builder.getOrCreate()
    sc = spark.sparkContext

    if quiet_spark:
        sc.setLogLevel("ERROR")

    conf = sc.getConf()

    # Synchronizing TimeZone
    tz = os.environ.get("TZ", "UTC")
    os.environ["TZ"] = tz
    time.tzset()

    to_add_conf.extend(
        [
            ("spark.app.name", f"{os.environ.get('USER')}_{app_name}_scikit"),
            ("spark.sql.session.timeZone", tz),
            ("spark.sql.execution.arrow.enabled", "true"),
            ("spark.sql.execution.arrow.pyspark.enabled", "true"),
        ]
    )

    for key, value in to_add_conf:
        conf.set(key, value)

    # Stopping context to add necessary env variables
    sc.stop()
    spark.stop()

    set_env_variables()

    spark = SparkSession.builder.enableHiveSupport().config(conf=conf).getOrCreate()

    sc = spark.sparkContext

    if quiet_spark:
        sc.setLogLevel("ERROR")

    sql = spark.sql

    koalas_options()

    return spark, sc, sql
