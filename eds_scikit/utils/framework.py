from collections import Counter
from functools import partial
from types import ModuleType
from typing import Optional

import pandas as pd
from databricks import koalas as ks

from eds_scikit.utils.typing import DataObject

from .custom_implem import CustomImplem

VALID_FRAMEWORKS = [pd, ks]


class BaseFramework:
    """Dispatcher between pandas, koalas and custom method."""

    def get_framework(self, obj: DataObject) -> Optional[ModuleType]:
        for framework in VALID_FRAMEWORKS:
            if obj.__class__.__module__.startswith(framework.__name__):
                return framework
        return None

    def is_pandas(self, obj: DataObject) -> bool:
        return self.get_framework(obj) is pd

    def is_koalas(self, obj: DataObject) -> bool:
        return self.get_framework(obj) is ks

    def to_pandas(self, obj: DataObject) -> DataObject:
        if self.get_framework(obj) is pd:
            return obj
        try:
            return obj.to_pandas()
        except AttributeError:
            raise ValueError("Could not convert object to pandas.")

    def to_koalas(self, obj: DataObject) -> DataObject:
        if self.get_framework(obj) is ks:
            return obj
        try:
            return obj.to_koalas()
        except AttributeError:
            pass
        # Will raise ValueError if impossible
        return ks.from_pandas(obj)

    def __getattr__(self, method):
        return partial(self.get_params, method)

    def get_params(self, method, *args, **kwargs):
        fk = self._get_framework_from_params(*args, **kwargs)
        if method in dir(fk):
            # Use the native method
            return getattr(fk, method)(*args, **kwargs)
        elif method in dir(CustomImplem):
            # Look for our implementation
            use_pd = self.is_pandas(fk)
            return getattr(CustomImplem, method)(*args, use_pd=use_pd, **kwargs)
        else:
            raise NotImplementedError(
                f"Method {method} doesn't belong to {fk.__name__} "
                f"and is not implemented in eds_scikit yet."
            )

    def _get_framework_from_params(self, *args, **kwargs):
        counter = Counter()
        all_args = [*args, *kwargs.values()]
        self._count_framework_from_args(all_args, counter)
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

    def _count_framework_from_args(self, all_args, counter):
        for arg in all_args:
            if isinstance(arg, (list, set, tuple)):
                self._count_framework_from_args(arg, counter)
            counter["pd"] += self.is_pandas(arg)
            counter["ks"] += self.is_koalas(arg)


fw = BaseFramework()
