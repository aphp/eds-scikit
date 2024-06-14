import numpy as np
import pandas as pd
import pytest

from eds_scikit.utils import framework
from eds_scikit.utils.sort_values_first import sort_values_first
from eds_scikit.utils.test_utils import assert_equal_no_order

# Create a DataFrame
np.random.seed(0)
size = 10000
data = {
    "A": np.random.choice(["X", "Y", "Z"], size),
    "B": np.random.randint(1, 5, size),
    "C": np.random.randint(1, 5, size),
    "D": np.random.randint(1, 5, size),
    "E": np.random.randint(1, 5, size),
}

inputs = pd.DataFrame(data)
inputs.loc[0, "B"] = 0
inputs.loc[0, "C"] = 4


@pytest.mark.parametrize(
    "module",
    ["pandas", "koalas"],
)
def test_sort_values_first(module):

    inputs_fr = framework.to(module, inputs)

    computed = framework.pandas(
        sort_values_first(inputs_fr, ["A"], ["B", "C"], ascending=True)
    )
    expected = (
        inputs.sort_values(["B", "C"], ascending=True)
        .groupby("A", as_index=False)
        .first()
    )
    assert_equal_no_order(computed, expected)

    computed = framework.pandas(
        sort_values_first(inputs_fr, ["A"], ["B", "C"], ascending=False)
    )
    expected = (
        inputs.sort_values(["B", "C"], ascending=False)
        .groupby("A", as_index=False)
        .first()
    )
    assert_equal_no_order(computed, expected)
