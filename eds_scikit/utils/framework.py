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


# TODO: All functions below need to be deprecated


def get_framework(obj: DataObject) -> Optional[ModuleType]:
    for _, framework in VALID_FRAMEWORKS.items():
        if obj.__class__.__module__.startswith(framework.__name__):
            return framework
    # raise ValueError(f"Object from unknown framework: {obj}")
    return None


def is_pandas(obj: DataObject) -> bool:
    return get_framework(obj) == pd


def is_koalas(obj: DataObject) -> bool:
    return get_framework(obj) == ks


def to(framework: str, obj: DataObject) -> DataObject:
    possible_values = set(VALID_FRAMEWORKS.keys()).union(VALID_FRAMEWORKS.values())
    assert framework in possible_values
    if framework == "koalas" or framework is ks:
        return koalas(obj)
    elif framework == "pandas" or framework is pd:
        return pandas(obj)
    else:
        raise ValueError(f"Unknown framework: {framework}")


def dict_to(framework: str, d: Dict[str, DataObject]) -> Dict[str, DataObject]:
    d_converted = dict()
    for k, v in d.items():
        if is_pandas(v) or is_koalas(v):
            d_converted[k] = to(framework, v)
        else:
            d_converted[k] = v
    return d_converted


def pandas(obj: DataObject) -> DataObject:
    if get_framework(obj) is pd:
        return obj
    try:
        return obj.to_pandas()
    except AttributeError:
        pass
    raise ValueError("Could not convert object to pandas.")


def koalas(obj: DataObject) -> DataObject:
    if get_framework(obj) is ks:
        return obj
    try:
        return obj.to_koalas()
    except AttributeError:
        pass

    # will raise ValueError if impossible
    return ks.from_pandas(obj)


class BackendDispatcher:
    """Dispatcher between pandas, koalas and custom method."""

    def get_backend(self, obj: DataObject) -> Optional[ModuleType]:
        for backend in VALID_FRAMEWORKS:
            if obj.__class__.__module__.startswith(backend.__name__):
                return backend
        return None

    def is_pandas(self, obj: DataObject) -> bool:
        return self.get_backend(obj) is pd

    def is_koalas(self, obj: DataObject) -> bool:
        return self.get_backend(obj) is ks

    def to_pandas(self, obj: DataObject) -> DataObject:
        if self.get_backend(obj) is pd:
            return obj
        try:
            return obj.to_pandas()
        except AttributeError:
            raise ValueError("Could not convert object to pandas.")

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
        """Any method that doesn't belong directly to `BackendDispatcher` will
         be picked by __getattr__.

        `__getattr__` returns the self.get_params function, wrapped with
        the queried `method` as a parameter.

         This way, `get_param` will be able to call `method`, dispatched between
         the desired backend, with the args and kwargs initially provided.
        """
        return partial(self.get_params, method)

    def get_params(self, method, *args, backend=None, **kwargs):
        """
        This method should only be called by `__getattr__`.

        `get_params` dispatches the call to a backend (pandas or koalas)
        chosen with simple heuristics.
        """
        if isinstance(backend, str):
            backend = {
                "pd": pd,
                "pandas": pd,
                "ks": ks,
                "koalas": ks,
            }[backend]
        elif backend is pd or backend is ks:
            pass
        # TODO: support Dataframe
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
                f"Method {method} doesn't belong to {backend.__name__} "
                f"and is not implemented in eds_scikit yet."
            )

    def _get_backend_from_params(self, *args, **kwargs):
        counter = Counter()
        all_args = [*args, *kwargs.values()]
        self._count_backend_from_args(all_args, counter)
        if bool(counter["ks"]) and bool(counter["pd"]):  # "^" is the XOR operator
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
        for fk in VALID_FRAMEWORKS:
            methods = [
                d for d in dir(fk) if ("__" not in d) and (not d.startswith("_"))
            ]
            if method in methods:
                backends.append(fk)

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


backend_dispatcher = BackendDispatcher()
