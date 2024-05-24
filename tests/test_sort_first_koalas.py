import pandas as pd
import pytest
from numpy import array

from eds_scikit.utils import framework
from eds_scikit.utils.sort_first_koalas import sort_values_first_koalas
from eds_scikit.utils.test_utils import assert_equal_no_order

data = {
    "A": array(
        [
            "X",
            "Y",
            "X",
            "Y",
            "Y",
            "Z",
            "X",
            "Z",
            "X",
            "X",
            "X",
            "Z",
            "Y",
            "Z",
            "Z",
            "X",
            "Y",
            "Y",
            "Y",
            "Y",
        ],
        dtype="<U1",
    ),
    "B": array([9, 5, 4, 1, 4, 6, 1, 3, 4, 9, 2, 4, 4, 4, 8, 1, 2, 1, 5, 8]),
    "C": array([4, 3, 8, 3, 1, 1, 5, 6, 6, 7, 9, 5, 2, 5, 9, 2, 2, 8, 4, 7]),
    "D": array([8, 3, 1, 4, 6, 5, 5, 7, 5, 5, 4, 5, 5, 9, 5, 4, 8, 6, 6, 1]),
    "E": array([i for i in range(20)]),
}

all_inputs = [pd.DataFrame(data)]

all_params = dict(
    ascending=[True, False],
    cols=["A", ["A", "B"]],
    by_cols=[["B", "C", "D"], ["C", "D"]],
    disambiguate_col="E"
)
all_params = pd.DataFrame(all_params).to_dict("records")


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize(
    "params, inputs",
    [(params, inputs) for params, inputs in zip(all_params, all_inputs)],
)
def test_sort_values_first_koalas(module, params, inputs):
    expected_results = (
        inputs.sort_values([*params["cols"], params["disambiguate_col"]])
        .groupby([*params["by_cols"]])
        .first()
        .reset_index()
    )
    inputs = framework.to(module, inputs)
    results = sort_values_first_koalas(inputs, **params)
    results = framework.pandas(results)
        
    assert_equal_no_order(results, expected_results, check_dtype=False)
