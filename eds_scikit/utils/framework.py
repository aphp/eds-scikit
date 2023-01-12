from collections import Counter
from functools import partial
from types import ModuleType
from typing import Dict, Optional

import pandas as pd
from databricks import koalas as ks
from loguru import logger

from eds_scikit.utils.typing import DataObject

from .custom_implem.custom_implem import CustomImplem

VALID_FRAMEWORKS = [pd, ks]


# TODO: All non class-methods functions below need to be remove


def get_framework(obj: DataObject) -> Optional[ModuleType]:  # pragma: no cover
    for framework in VALID_FRAMEWORKS:
        if obj.__class__.__module__.startswith(framework.__name__):
            return framework
    # raise ValueError(f"Object from unknown framework: {obj}")
    return None


def is_pandas(obj: DataObject) -> bool:  # pragma: no cover
    return get_framework(obj) == pd


def is_koalas(obj: DataObject) -> bool:  # pragma: no cover
    return get_framework(obj) == ks


def to(framework: str, obj: DataObject) -> DataObject:  # pragma: no cover
    if framework == "koalas" or framework is ks:
        return koalas(obj)
    elif framework == "pandas" or framework is pd:
        return pandas(obj)
    else:
        raise ValueError(f"Unknown framework: {framework}")


def dict_to(
    framework: str, d: Dict[str, DataObject]
) -> Dict[str, DataObject]:  # pragma: no cover
    d_converted = dict()
    for k, v in d.items():
        if is_pandas(v) or is_koalas(v):
            d_converted[k] = to(framework, v)
        else:
            d_converted[k] = v
    return d_converted


def pandas(obj: DataObject) -> DataObject:  # pragma: no cover
    if get_framework(obj) is pd:
        return obj
    try:
        return obj.to_pandas()
    except AttributeError:
        pass
    raise ValueError("Could not convert object to pandas.")


def koalas(obj: DataObject) -> DataObject:  # pragma: no cover
    if get_framework(obj) is ks:
        return obj
    try:
        return obj.to_koalas()
    except AttributeError:
        pass

    # will raise ValueError if impossible
    return ks.from_pandas(obj)


class BackendDispatcher:
    """Dispatcher between pandas, koalas and custom methods.

    In addition to the methods below, use the `BackendDispatcher` class
    to access the custom functions defined in [`CustomImplem`](../custom_implem/custom_implem).

    Examples
    --------

    Use a dispatcher function

    >>> from eds_scikit.utils.framework import bd
    >>> bd.is_pandas(pd.DataFrame())
    True

    Use a custom implemented function

    >>> df = pd.DataFrame({"categ": ["a", "b", "c"]})
    >>> bd.add_unique_id(df, col_name="id")
      categ  id
    0     a   0
    1     b   1
    2     c   2
    """

    def get_backend(self, obj) -> Optional[ModuleType]:
        """Return the backend of a given object.

        Parameters
        ----------
        obj: DataFrame or backend module among pandas or koalas.

        Returns
        -------
        backend: a backend among {pd, ks} or None

        Examples
        --------

        Get the backend from a DataFrame and create another DataFrame from it.
        This is especially useful at runtime, when you need to infer the
        backend of the input.

        >>> backend = bd.get_backend(pd.DataFrame())
        >>> backend
        <module 'pandas'>
        >>> df = backend.DataFrame()

        >>> bd.get_backend(ks.DataFrame())
        <module 'koalas'>

        For demo purposes, return the backend when provided directly

        >>> bd.get_backend(ks)
        <module 'koalas'>
        >>> bd.get_backend(spark)
        None
        """
        if isinstance(obj, str):
            return {
                "pd": pd,
                "pandas": pd,
                "ks": ks,
                "koalas": ks,
            }.get(obj)

        for backend in VALID_FRAMEWORKS:
            if (
                obj.__class__.__module__.startswith(backend.__name__)  # DataFrame()
                or getattr(obj, "__name__", None) == backend.__name__  # pd or ks
            ):
                return backend
        return None

    def is_pandas(self, obj) -> bool:
        """Return True when the obj is either a pd.DataFrame or the pandas module."""
        return self.get_backend(obj) is pd

    def is_koalas(self, obj: DataObject) -> bool:
        """Return True when the obj is either a ks.DataFrame or the koalas module."""
        return self.get_backend(obj) is ks

    def to(self, obj, backend):
        """Convert a dataframe to the provided backend.

        Parameters
        ----------
        obj: DataFrame or iterable of DataFrame (list, tuple, dict)
            The object(s) to convert to the provided backend

        backend: str, DataFrame or pandas, koalas module
            The desired output backend.

        Returns
        -------
        out: DataFrame or iterabel of DataFrame (list, tuple, dict)
          The converted object, in the same format as provided in input.

        Examples
        --------

        Convert a single DataFrame

        >>> df = pd.DataFrame({"a": [1, 2]})
        >>> kdf = bd.to(df, backend="koalas")
        >>> type(kdf)
        databricks.koalas.frame.DataFrame

        Convert a list of DataFrame

        >>> extra_kdf = ks.DataFrame({"b": [0, 1]})
        >>> another_kdf = ks.DataFrame({"c": [2, 3]})
        >>> kdf_list = [kdf, extra_kdf, another_kdf]
        >>> df_list = bd.to(kdf_list, backend="pandas")
        >>> type(df_list)
        list
        >>> len(df_list)
        3
        >>> type(df_list[0])
        pandas.core.frame.DataFrame

        Convert a dictionnary of DataFrame

        >>> df_dict = {"df_1": pd.DataFrame({"a": [1, 2]}), "df_2": pd.DataFrame({"a": [2, 3]})}
        >>> kdf_dict = bd.to(df_dict, backend="koalas")
        >>> type(kdf_dict)
        dict
        >>> kdf_dict.keys()
        dict_keys(["df_1", "df_2"])
        >>> type(kdf_dict["df_1"])
        databricks.koalas.frame.DataFrame
        """
        if isinstance(obj, (list, tuple)):
            results = []
            for _obj in obj:
                results.append(self.to(_obj, backend))
            return results

        if isinstance(obj, dict):
            results = {}
            for k, _obj in obj.items():
                results[k] = self.to(_obj, backend)
            return results

        backend = self.get_backend(backend)

        if self.is_pandas(backend):
            return self.to_pandas(obj)
        elif self.is_koalas(backend):
            return self.to_koalas(obj)
        else:
            raise ValueError("Unknown backend")

    def to_pandas(self, obj: DataObject) -> DataObject:
        if self.get_backend(obj) is pd:
            return obj
        return obj.to_pandas()

    def to_koalas(self, obj: DataObject) -> DataObject:
        if self.get_backend(obj) is ks:
            return obj
        try:
            return obj.to_koalas()
        except AttributeError:
            pass
        # Will raise ValueError if impossible
        return ks.from_pandas(obj)

    def __getattr__(self, method):
        # Any method that doesn't belong directly to `BackendDispatcher` will
        # be picked by __getattr__.
        #
        # `__getattr__` returns the self.get_params function, wrapped with
        # the queried `method` as a parameter.
        #
        # This way, `get_param` will be able to call `method`, dispatched between
        # the desired backend, with the args and kwargs initially provided.
        return partial(self.get_params, method)

    def get_params(self, method, *args, backend=None, **kwargs):
        # This method should only be called by `__getattr__`.
        #
        # `get_params` dispatches the call to a backend (pandas or koalas)
        # chosen with simple heuristics.
        if backend is not None:
            backend = self.get_backend(backend)
            if backend is None:
                raise ValueError("Unknown backend")
        else:
            backend = self._get_backend_from_params(
                *args, **kwargs
            ) or self._get_backend_from_method(method)

        if method in dir(backend):
            # Use the native method
            return getattr(backend, method)(*args, **kwargs)
        elif method in dir(CustomImplem):
            # Use our implementation
            return getattr(CustomImplem, method)(*args, backend=backend, **kwargs)
        else:
            raise NotImplementedError(
                f"Method '{method}' doesn't belong to pandas or koalas "
                f"and is not implemented in eds_scikit yet."
            )

    def _get_backend_from_params(self, *args, **kwargs):
        counter = Counter()
        all_args = [*args, *kwargs.values()]
        self._count_backend_from_args(all_args, counter)
        if bool(counter["ks"]) and bool(counter["pd"]):
            raise ValueError(
                "Inputs have mixed types of Koalas and Pandas dataframes,"
                "which is not supported.\n"
                "Please convert your dataframes using fw.to_pandas(df) or fw.to_koalas(df)"
            )
        elif counter["pd"]:
            return pd
        elif counter["ks"]:
            return ks
        else:
            return None

    def _count_backend_from_args(self, all_args, counter):
        for arg in all_args:
            if isinstance(arg, (list, set, tuple)):
                self._count_backend_from_args(arg, counter)
            counter["pd"] += self.is_pandas(arg)
            counter["ks"] += self.is_koalas(arg)

    def _get_backend_from_method(self, method):
        backends = []
        for backend in VALID_FRAMEWORKS:
            methods = [
                d for d in dir(backend) if ("__" not in d) and (not d.startswith("_"))
            ]
            if method in methods:
                backends.append(backend)

        if len(backends) == 0:
            return None

        if len(backends) > 1:
            logger.warning(
                f"Both Pandas and Koalas have method {method}."
                "Pandas will be used by default."
                "You can change this behaviour by setting 'backend':\n\n"
                f"    fw.{method}(..., backend='koalas', ...)"
            )
            return pd

        return backends[0]


bd = BackendDispatcher()
