import sys
from unittest.mock import patch

import pyarrow

from eds_scikit.io.improve_performance import load_koalas, set_env_variables


def test_improve_performances():
    del sys.modules["databricks.koalas"]
    load_koalas()

    with patch.object(pyarrow, "__version__", "2.1.0"):
        set_env_variables()
