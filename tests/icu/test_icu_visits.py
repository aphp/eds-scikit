import pytest

from eds_scikit.icu import tag_icu_visit
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order, make_df

visit_detail = make_df(
    """
    visit_detail_id,care_site_id
    1,1
    2,2
    3,3
    4,4
    5,5
    6,6
    7,7
    8,8
    9,9
"""
)

care_site = make_df(
    """
    care_site_id,place_of_service_source_value
    1,REA PED
    2,SC
    3,USI
    4,Non renseigné
    5,Inconnu
    6,REA NEONAT
    7,Inconnu
    8,Inconnu
    9,Inconnu
"""
)

result = make_df(
    """
    visit_detail_id,care_site_id,IS_ICU
    1,1,True
    2,2,True
    3,3,True
    4,4,False
    5,5,False
    6,6,True
    7,7,False
    8,8,False
    9,9,False
    """
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_tagging_icu(module):

    vd = framework.to(module, visit_detail).copy()
    cs = framework.to(module, care_site).copy()
    expected_result = framework.to(module, result)

    output = tag_icu_visit(
        visit_detail=vd, care_site=cs, algo="from_authorisation_type"
    )

    assert_equal_no_order(framework.pandas(output), expected_result, check_like=True)
