import pytest

from eds_scikit.datasets import load_tagging
from eds_scikit.period import tagging_functions
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_index, make_df

ds = load_tagging()
df_tag_result_intersection = make_df(
    """
    person_id, t_start, t_end, concept, value, event_in_tag, intersect_right, intersect_left, tag_in_event, outside_left, outside_right
    1, 2019-01-01 00:00:00, 2020-01-01 00:00:00, CIM10_INFARCTUS, E210, True, True, True, True, False, False
"""  # noqa: E501
)

df_tag_result_event_in_tags = make_df(
    """
    person_id, t_start, t_end, concept, value, event_in_tag, intersect_right, intersect_left, tag_in_event, outside_left, outside_right
    1, 2019-01-01 00:00:00, 2020-01-01 00:00:00, CIM10_INFARCTUS, E210, True, False, False, False, False, False
"""  # noqa: E501
)

df_tag_result_tag_in_event = make_df(
    """
    person_id, t_start, t_end, concept, value, event_in_tag, intersect_right, intersect_left, tag_in_event, outside_left, outside_right
    1, 2019-01-01 00:00:00, 2020-01-01 00:00:00, CIM10_INFARCTUS, E210, False, False, False, True, False, False
"""  # noqa: E501
)

algos = {
    tagging_functions.interval_algos.intersection: df_tag_result_intersection,
    tagging_functions.interval_algos.to_in_from: df_tag_result_event_in_tags,
    tagging_functions.interval_algos.from_in_to: df_tag_result_tag_in_event,
}


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize("algo", list(algos))
def test_tagging(module, algo):
    expected_result = algos[algo]

    events_backup = ds.events.copy()
    events = framework.to(module, ds.events)
    tags = framework.to(module, ds.tags)

    tagged = tagging_functions.tagging(events, tags, "CIM10_DIABETE", algo=algo)
    tagged = framework.pandas(tagged)
    events = framework.pandas(events)

    assert_equal_no_index(tagged, expected_result, check_like=True)

    # checking that the original data was not modified
    assert_equal_no_index(events, events_backup)
