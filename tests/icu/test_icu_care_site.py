import pytest

from eds_scikit.icu import tag_icu_care_site
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order, make_df

# Dictionnary of the form {algo_name : [input_df, expected_output_df]}
algos = dict(
    from_authorisation_type=[
        make_df(
            """
    care_site_id,place_of_service_source_value
    263,REA ADULTE
    352,SC ADULTE
    494,USI ADULTE
    551,USI NEONAT
    600,REA NEONAT
    767,SC PED
    1062,REA PED
    17,NON RENSEIGNE
    56,None
"""
        ),
        make_df(
            """
    care_site_id,place_of_service_source_value,IS_ICU
    263,REA ADULTE,True
    352,SC ADULTE,True
    494,USI ADULTE,True
    551,USI NEONAT,True
    600,REA NEONAT,True
    767,SC PED,True
    1062,REA PED,True
    17,NON RENSEIGNE,False
    56,None,False
"""
        ),
    ],
    from_regex_on_care_site_description=[
        make_df(
            """
    care_site_id,care_site_name,care_site_type_source_value
    1,UNITE REA ADULTE,UDS
    2,REANIMATION,UDS
    3,SOINS DE READAPTATION,UDS
    4,UNITE DE SURV CONT,UDS
    5,UNITE DE SURVEILLANCE CONTINUE,UDS
    6,UNITE DE SURV CONT,UDS
    7,BCH USC COVID,UDS
    8,SOINS INTENSIFS,UDS
    9,CARDIO UNITE USIC,UDS
    10,SERUSIER CHAMBRE 02,UDS
    11,UF REA,UF / UC
"""
        ),
        make_df(
            """
    care_site_id,care_site_name,care_site_type_source_value,IS_ICU
    1,UNITE REA ADULTE,UDS,True
    2,REANIMATION,UDS,True
    3,SOINS DE READAPTATION,UDS,False
    4,UNITE DE SURV CONT,UDS,True
    5,UNITE DE SURVEILLANCE CONTINUE,UDS,True
    6,UNITE DE SURV CONT,UDS,True
    7,BCH USC COVID,UDS,True
    8,SOINS INTENSIFS,UDS,True
    9,CARDIO UNITE USIC,UDS,True
    10,SERUSIER CHAMBRE 02,UDS,False
    11,UF REA,UF / UC,False
"""
        ),
    ],
)


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize("algo", list(algos.keys()))
def test_tagging(module, algo):
    input_df = algos[algo][0].copy()
    expected_result = algos[algo][1]

    converted_input_df = framework.to(module, input_df)
    output = tag_icu_care_site(converted_input_df, algo=algo)

    assert_equal_no_order(framework.pandas(output), expected_result, check_like=True)
