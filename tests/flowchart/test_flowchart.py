from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from eds_scikit.utils.flowchart import Flowchart
from eds_scikit.utils.test_utils import image_diff

data_as_df = pd.DataFrame(
    dict(
        person_id=list(range(10)),
        over_18=5 * [True] + 5 * [False],
        diabetes=[True, False, True, False, True, False, True, False, True, False],
        infarction=[True, True, False, False, True, True, False, False, True, True],
        final_split=[True] + 9 * [False],
    )
)

data_as_dict = dict(
    initial=list(range(10)),
    over_18=set([0, 1, 2, 3, 4]),
    diabetes=np.array([0, 2, 4, 6, 8]),
    infarction=pd.Series([0, 1, 4, 5, 8, 9]),
    final_split=pd.Series([0]).to_frame(),
)


@pytest.mark.parametrize("data", [data_as_df, data_as_dict])
def test_flowchart(data, tmpdir_factory):
    tmp_dir = Path(tmpdir_factory.mktemp("flowchart"))

    F = Flowchart(
        initial_description="Initial population",
        data=data,
    )

    F.add_criterion(
        description="Patients over 18 y.o.",
        excluded_description="",
        criterion_name="over_18",
    )

    F.add_criterion(
        description="With Type I or II diabetes",
        excluded_description="",
        criterion_name="diabetes",
    )

    F.add_criterion(
        description="With infarction",
        excluded_description="",
        criterion_name="infarction",
    )

    F.add_final_split(
        left_description="",
        right_description="",
        criterion_name="final_split",
        left_title="Cohort 1",
        right_title="Cohort 2",
    )

    _ = F.generate_flowchart(alternate=True, fontsize=10)

    out_path = str(tmp_dir / "flowchart.png")
    F.save(out_path, dpi=72)

    tgt_1 = str(Path(__file__).parent / "expected_flowchart.png")
    tgt_2 = str(Path(__file__).parent / "expected_flowchart_bis.png")

    assert image_diff(out_path, tgt_1) < 0.05 or image_diff(out_path, tgt_2) < 0.05


def test_incorrect_data():

    # Incorrect data type
    with pytest.raises(TypeError, match=r"not a <class 'int'>"):
        _ = Flowchart(initial_description="", data=1)

    # `to_count` not in DataFrame
    with pytest.raises(ValueError, match=r"not a column of `data`"):
        _ = Flowchart(
            initial_description="",
            data=pd.DataFrame(dict(a=[1, 2, 3])),
            to_count="b",
        )

    # `initial` not in dictionary
    with pytest.raises(ValueError, match=r"the initial cohort should be provided"):
        _ = Flowchart(
            initial_description="",
            data=dict(a=[1, 2, 3]),
        )
