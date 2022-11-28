import pandas as pd
import pytest
from databricks import koalas as ks

from eds_scikit.utils import framework

# pytestmark = pytest.mark.koalas


def is_koalas(obj, example_objects):
    return any(isinstance(obj, type(other)) for other in example_objects["koalas"])


def is_pandas(obj, example_objects):
    return any(isinstance(obj, type(other)) for other in example_objects["pandas"])


def test_identify_pandas(example_objects):
    for obj in example_objects["pandas"]:
        assert framework.is_pandas(obj) is True
        assert framework.is_koalas(obj) is False
        assert framework.get_framework(obj) is pd


def test_identify_koalas(example_objects):
    for obj in example_objects["koalas"]:
        assert framework.is_pandas(obj) is False
        assert framework.is_koalas(obj) is True
        assert framework.get_framework(obj) is ks


def test_framework_pandas(example_objects):
    for obj in example_objects["pandas"]:
        converted = framework.pandas(obj)
        assert converted is obj
    for obj in example_objects["koalas"]:
        converted = framework.pandas(obj)
        assert is_pandas(converted, example_objects)


def test_framework_koalas(example_objects):
    for obj in example_objects["pandas"]:
        converted = framework.koalas(obj)
        assert is_koalas(converted, example_objects)

    for obj in example_objects["koalas"]:
        converted = framework.koalas(obj)
        assert converted is obj


def test_unconvertible_objects():
    objects = [1, "coucou", {"a": [1, 2]}, [1, 2, 3], 2.5, ks, pd]
    for obj in objects:
        with pytest.raises(ValueError):
            framework.pandas(obj)

    for obj in objects:
        with pytest.raises(ValueError):
            framework.koalas(obj)
