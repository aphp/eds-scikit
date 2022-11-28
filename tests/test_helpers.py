from typing import List, Optional

import pandas as pd
import pytest

from eds_scikit.utils.checks import _get_arg_value, algo_checker, concept_checker
from eds_scikit.utils.typing import DataFrame


def decorator_wrapper(
    concepts: List[str] = None,
    only_adds_concepts: bool = True,
):
    @concept_checker(
        concepts=concepts,
        only_adds_concepts=only_adds_concepts,
    )
    def f(
        df: DataFrame,
        to_add_concepts: Optional[List[str]] = None,
    ):
        if to_add_concepts is None:
            return df
        for concept in to_add_concepts:
            df[concept] = "added"
        return df

    return f


def test_incorrect_type():
    with pytest.raises(TypeError):
        decorator_wrapper()(df="A string")


def test_concept_already_present():
    df = pd.DataFrame(
        dict(
            PRESENT_CONCEPT=["value"],
        )
    )
    with pytest.raises(ValueError):
        decorator_wrapper(concepts="PRESENT_CONCEPT")(df=df)


def test_concept_not_added():
    df = pd.DataFrame(
        dict(
            INITIAL_CONCEPT=["value"],
        )
    )
    with pytest.raises(ValueError):
        decorator_wrapper(concepts="PRESENT_CONCEPT")(
            df=df,
            to_add_concepts=["OTHER_CONCEPT"],
        )


def test_other_concepts_not_added():
    df = pd.DataFrame(
        dict(
            INITIAL_CONCEPT=["value"],
        )
    )
    with pytest.raises(ValueError):
        decorator_wrapper(concepts="PRESENT_CONCEPT")(
            df=df,
            to_add_concepts=["OTHER_CONCEPT"],
        )


def test_other_concepts_added(caplog):
    df = pd.DataFrame(
        dict(
            INITIAL_CONCEPT=["value"],
        )
    )
    decorator_wrapper(concepts="PRESENT_CONCEPT")(
        df=df,
        to_add_concepts=["PRESENT_CONCEPT", "OTHER_CONCEPT"],
    )

    for record in caplog.records:
        assert record.levelname == "WARNING"
        assert "OTHER_CONCEPT" in caplog.text


def test_algo_checker():
    @algo_checker(algos=["A", "B", "C"])
    def f(algo: str):
        return

    with pytest.raises(ValueError):
        f(algo="D")


def test_getting_arg():
    def from_args(a, b):
        return

    def from_kwargs(a, *args, b):
        return

    def from_nothing(a, *args, **kwargs):
        return

    assert (
        _get_arg_value(
            from_args,
            "b",
            args=["a_value", "b_value"],
            kwargs=None,
        )
        == "b_value"
    )

    assert (
        _get_arg_value(
            from_kwargs,
            "b",
            args=None,
            kwargs={"a": "a_value", "b": "b_value"},
        )
        == "b_value"
    )

    with pytest.raises(ValueError):
        _get_arg_value(
            from_nothing,
            "b",
            args=["a_value", "b_value"],
            kwargs={"a": "a_value", "b": "b_value"},
        )
