from inspect import getfullargspec
from typing import Any, Callable, List, Optional, Tuple, Union

import pandas as pd
from databricks import koalas as ks
from decorator import decorator
from loguru import logger

from eds_scikit.utils.typing import Data, DataFrame


@decorator
def concept_checker(
    function: Callable,
    concepts: List[str] = None,
    only_adds_concepts: bool = True,
    *args,
    **kwargs,
) -> Any:
    """
    Decorator to use on functions that
    - Takes a DataFrame as first argument
    - Adds a concept to it

    The decorator checks:
    - If the first argument is a DataFrame
    - If the concepts to be added aren't already in the DataFrame
    - If the function correctly adds the concepts
    - If no additionnal columns are added (if only_adds_concepts is True)

    If one of this checks fails, raises an error
    """
    # Is the first argument a DataFrame
    df = args[0]
    if (type(df) != ks.DataFrame) & (type(df) != pd.DataFrame):
        raise TypeError(
            f"The first argument of '{function.__module__}.{function.__name__}' "
            "should be a Pandas or Koalas DataFrame"
        )

    # Initial columns
    initial_cols = set(df.columns)

    # Is the concept already present
    if type(concepts) == str:
        concepts = [concepts]
    present_concepts = set(concepts) & set(df.columns)
    if present_concepts:
        raise ValueError(
            f"The concepts {present_concepts} are already present in the input dataframe "
            f"of  '{function.__module__}.{function.__name__}'.\n"
            "You can either rename the column(s) or delete them before running "
            "the function again."
        )

    result = function(*args, **kwargs)

    # Was the concept correctly added
    missing_concepts = set(concepts) - set(result.columns)
    if len(missing_concepts) > 0:
        raise ValueError(
            f"The concept(s) '{missing_concepts}' were not added to the DataFrame."
        )

    # Check that no other columns were added

    if only_adds_concepts:
        result_cols = set(result.columns)
        additionnal_cols = result_cols - (initial_cols | set(concepts))
        if additionnal_cols:
            logger.warning(
                "The columns"
                + "".join([f"\n- {s}" for s in additionnal_cols])
                + f"\nwere added/renamed by '{function.__module__}.{function.__name__}',"
                + f"although it should normally only add the columns {concepts}"
            )

    return result


@decorator
def algo_checker(
    function: Callable,
    algos: Optional[str] = None,
    *args,
    **kwargs,
) -> Any:
    """
    Decorator to use on wrapper that calls specific functions based on the 'algo' argument

    The decorator checks if the provided algo is an implemented one.

    If this checks fails, raises an error
    """

    algo = _get_arg_value(function, "algo", args, kwargs)

    # Stripping eventual version suffix
    algo = algo.split(".")[0]

    if algo not in algos:
        raise ValueError(
            f"Method {algo} unknown for '{function.__module__}.{function.__name__}'.\n"
            f"Available algos are {algos}"
        )
    result = function(*args, **kwargs)
    return result


def _get_arg_value(
    function: Callable, argname: str, args, kwargs, return_index_or_key=False
) -> Any:
    """
    Get the value of the 'argname' argument defined in 'function'
    Looks for arguments or keyword argument
    Raises an error if not found
    """
    specs = getfullargspec(function)

    if argname in specs.args:
        arg_index = specs.args.index(argname)
        if return_index_or_key:
            return args[arg_index], arg_index
        return args[arg_index]

    if argname in specs.kwonlyargs:
        if return_index_or_key:
            return kwargs[argname], argname
        return kwargs[argname]

    raise ValueError(
        f"Argument {argname} not defined in '{function.__module__}.{function.__name__}'"
    )


class MissingConceptError(Exception):
    """Exception raised when a concept is missing"""

    def __init__(
        self,
        required_concepts: Union[List[str], List[Tuple[str, str]]],
        df_name: str = "",
    ):

        if all(isinstance(concept, tuple) for concept in required_concepts):
            to_display_per_concept = [
                f"- {concept} ({msg})" for concept, msg in required_concepts
            ]
        else:
            to_display_per_concept = [f"- {concept}" for concept in required_concepts]
        str_to_display = "\n".join(to_display_per_concept)

        if df_name:
            df_name = f" {df_name} "
        message = (
            f"The {df_name}DataFrame is missing some columns, "
            "namely:\n"
            f"{str_to_display}"
        )

        super().__init__(message)


class MissingTableError(Exception):
    """Exception raised when a table is missing in the Data"""

    def __init__(
        self,
        required_tables: Union[List[str], List[Tuple[str, str]]],
        data_name: str = "",
    ):

        if all(isinstance(table, tuple) for table in required_tables):
            to_display_per_table = [
                f"- {table} ({msg})" for table, msg in required_tables
            ]
        else:
            to_display_per_table = [f"- {table}" for table in required_tables]
        str_to_display = "\n".join(to_display_per_table)

        if data_name:
            data_name = f" {data_name} "
        message = (
            f"The {data_name}Data is missing some tables, "
            "namely:\n"
            f"{str_to_display}"
        )

        super().__init__(message)


def check_columns(df: DataFrame, required_columns: List[str], df_name: str = ""):
    present_columns = set(df.columns)
    missing_columns = set(required_columns) - present_columns
    if missing_columns:
        raise MissingConceptError(missing_columns, df_name=df_name)


def check_tables(data: Data, required_tables: List[str], data_name: str = ""):
    present_tables = set(data.available_tables)
    missing_tables = set(required_tables) - present_tables
    if missing_tables:
        raise MissingTableError(missing_tables, data_name=data_name)
