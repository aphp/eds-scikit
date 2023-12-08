# This file is used to override the databricks.koalas package with the pyspark.pandas
# package, if the databricks.koalas package is not available (python >= 3.8)
import sys
import pyarrow  # noqa: E402, F401

old_sys_path = sys.path.copy()
sys.path.remove(next((p for p in sys.path if "package-override" in p), None))
databricks = sys.modules.pop("databricks")
sys.modules.pop("databricks.koalas")
try:
    from databricks.koalas import *  # noqa: E402, F401, F403
except ImportError:
    from pyspark.pandas import *  # noqa: E402, F401, F403

    sys.modules["databricks"] = databricks
    sys.modules["databricks.koalas"] = sys.modules["pyspark.pandas"]
sys.path[:] = old_sys_path
