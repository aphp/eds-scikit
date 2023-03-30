import pytest

from eds_scikit.emergency import tag_emergency_visit
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order, make_df

visit_detail = make_df(
    """
    visit_detail_id,care_site_id, visit_occurrence_id
    1,1,91
    2,2,91
    3,3,91
    4,4,92
    5,5,92
    6,6,93
    7,7,93
    8,8,94
    9,9,95
"""
)

visit_occurrence = make_df(
    """
    visit_occurrence_id, visit_source_value
    91,urgence
    92,urgence
    93,hospitalisation
    94,hospitalisation
    95,hospitalisation
    """
)

care_site = make_df(
    """
    care_site_id,care_site_source_value
    1,source_1
    2,source_2
    3,source_3
    4,source_4
    5,source_5
    6,source_6
    7,source_7
    8,source_8
    9,source_9
    """
)

# Dictionnary of the form {algo_name : [input_df, expected_output_df]}

params = [
    dict(
        visit_detail=visit_detail,
        care_site=care_site,
        visit_occurrence=None,
        algo="from_mapping.test",
    ),
    dict(
        visit_detail=visit_detail,
        care_site=None,
        visit_occurrence=visit_occurrence,
        algo="from_vo_visit_source_value",
    ),
]

results = [
    make_df(
        """
    visit_detail_id,care_site_id, visit_occurrence_id,EMERGENCY_TYPE,IS_EMERGENCY
    1,1,91,Urgences pédiatriques,True
    2,2,91,Urgences générales adulte,True
    3,3,91,UHCD + Post-urgences,True
    4,4,92,Urgences spécialisées,True
    5,5,92,Consultation urgences,True
    6,6,93,SAMU / SMUR,True
    7,7,93,NaN,False
    8,8,94,NaN,False
    9,9,95,NaN,False
    """
    ),
    make_df(
        """
    visit_detail_id,care_site_id, visit_occurrence_id,IS_EMERGENCY
    1,1,91,True
    2,2,91,True
    3,3,91,True
    4,4,92,True
    5,5,92,True
    6,6,93,False
    7,7,93,False
    8,8,94,False
    9,9,95,False
    """
    ),
]


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_tagging(module):

    for param, expected_result in zip(params, results):
        param = framework.dict_to(module, param)
        expected_result = framework.to(module, expected_result)

        output = tag_emergency_visit(**param)

        assert_equal_no_order(
            framework.pandas(output), expected_result, check_like=True
        )
