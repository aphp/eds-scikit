from types import ModuleType
from typing import Dict, Optional

import pandas as _pandas
from databricks import koalas as _koalas

from eds_scikit.utils.typing import DataFrame, DataObject

VALID_FRAMEWORKS = {
    "pandas": _pandas,
    "koalas": _koalas,
}


def get_framework(obj: DataObject) -> Optional[ModuleType]:
    for _, framework in VALID_FRAMEWORKS.items():
        if obj.__class__.__module__.startswith(framework.__name__):
            return framework
    # raise ValueError(f"Object from unknown framework: {obj}")
    return None


def is_pandas(obj: DataObject) -> bool:
    return get_framework(obj) == _pandas


def is_koalas(obj: DataObject) -> bool:
    return get_framework(obj) == _koalas


def to(framework: str, obj: DataObject) -> DataObject:
    possible_values = set(VALID_FRAMEWORKS.keys()).union(VALID_FRAMEWORKS.values())
    assert framework in possible_values
    if framework == "koalas" or framework is _koalas:
        return koalas(obj)
    elif framework == "pandas" or framework is _pandas:
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
    if get_framework(obj) is _pandas:
        return obj
    try:
        return obj.to_pandas()
    except AttributeError:
        pass
    raise ValueError("Could not convert object to pandas.")


def koalas(obj: DataObject) -> DataObject:
    if get_framework(obj) is _koalas:
        return obj
    try:
        return obj.to_koalas()
    except AttributeError:
        pass

    # will raise ValueError if impossible
    return _koalas.from_pandas(obj)


def add_unique_id(obj: DataFrame, col_name: str = "id") -> DataFrame:
    fw = get_framework(obj)
    if fw == _pandas:
        obj[col_name] = range(len(obj))
        return obj
    else:
        return obj.koalas.attach_id_column(id_type="distributed", column=col_name)
