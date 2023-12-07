"""
PySpark 2 needs pyarrow.open_stream, which was deprecated in 0.17.0 in favor of
pyarrow.ipc.open_stream. Here is the explanation of how we monkey-patch pyarrow
to add back pyarrow.open_stream for versions > 0.17 and how we make this work with
pyspark distributed computing :
1. We add this fake eds_scikit/package-override/pyarrow package to python lookup list
   (the PYTHONPATH env var) in eds_scikit/__init__.py : this env variable will be shared
   with the executors
2. When an executor starts and import packages, it looks in the packages by inspecting
   the paths in PYTHONPATH. It finds our fake pyarrow package first an executes the
   current eds_scikit/package-override/pyarrow/__init__.py file
3. In this file, we remove the fake pyarrow package path from the lookup list, unload
   the current module from python modules cache (sys.modules) and re-import pyarrow
   => the executor's python will this time load the true pyarrow and store it in
   sys.modules. Subsequent "import pyarrow" calls will return the sys.modules["pyarrow"]
   value, which is the true pyarrow module.
4. We are not finished: we add back the deprecated "open_stream" function that was
   removed in pyarrow 0.17.0 (the reason for all this hacking) by setting it
   on the true pyarrow module
5. We still export the pyarrow module content (*) such that the first import, which
   is the only one that resolves to this very module, still gets what it asked for:
   the pyarrow module's content.
"""

import sys

sys.path.remove(next((p for p in sys.path if "package-override" in p), None))
del sys.modules["pyarrow"]
import pyarrow  # noqa: E402, F401

try:
    import pyarrow.ipc

    pyarrow.open_stream = pyarrow.ipc.open_stream
except ImportError:
    pass

from pyarrow import *  # noqa: F401, F403, E402
