import pytest

from eds_scikit.emergency import tag_emergency_care_site
from eds_scikit.utils import framework
from eds_scikit.utils.test_utils import assert_equal_no_order, make_df

# Dictionnary of the form {algo_name : [input_df, expected_output_df]}
algos = {
    "from_mapping.test": [
        make_df(
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
        ),
        make_df(
            """
    care_site_id,care_site_source_value,EMERGENCY_TYPE,IS_EMERGENCY
    1,source_1,Urgences pédiatriques,True
    2,source_2,Urgences générales adulte,True
    3,source_3,UHCD + Post-urgences,True
    4,source_4,Urgences spécialisées,True
    5,source_5,Consultation urgences,True
    6,source_6,SAMU / SMUR,True
    7,source_7,NaN,False
    8,source_8,NaN,False
    9,source_9,NaN,False
"""
        ),
    ],
    "from_regex_on_care_site_description": [
        make_df(
            """
            care_site_name
            HOSP MATERNITE
            HOSP ACCUEIL URG PED (UF)
            HOSP URGENCES
            HOSP HISTORIQUE DOSSIERS
            HOSP POLYCLINIQUE
            HOSP MED BUCCO DENTAIRE (UF)
            HOSP HEPATO GASTRO ENTERO
            HOSP DEFIH
            HOSP PSYCHIATRIE
            HOSP ANESTHESIE-REA (UF)
            HOSP PEDIATRIE GEN ET SAU
            HOSP EXPLORATIONS FONCT (UF)
            HOSP CONSULT CHIRUR.
            HOSP CHIRURGIE DIGESTIVE
            HOSP NEONATOLOGIE
            HOSP PLAT AMB MEDICALE (UF)
            HOSP CONSULT EXPLO FONCT
            HOSP C.I.V.G. (UF)
            HOSP MEDECINE INTERNE
            HOSP HDJ PEDIATRIE (UF)
            HOSP REA MEDICALE
            HOSP PNEUMOLOGIE
            HOSP SURV CONT MED-C (UF)
            HOSP ONCOLOGIE (UF)
            HOSP ADDICTOLOGIE (UF)
            HOSP DRH
            HOSP ECIMUD (UF)
            HOSP CENTRE COORD MED INT
            HOSP REA NEONAT (UF)
            HOSP GERIATRIE AIGUE
            HOSP ACTES MEDICAUX
            HOSP SSR (UF)
            HOSP PSY ADOLESCENT (UF)
            HOSP CONSULT GERIATRIE (UF)
            HOSP O.R.L (UF)
            HOSP PSY NON SECTORISEE
            HOSP LABO HEMATO
            HOSP CMP CATT (UF)
            HOSP CEGIDD (UF)
            HOSP CTRE PORPHYRIES (UF)
            HOSP REED POLYVAL. (UF)
            HOSP LONG SEJOUR (UF)
            HOSP EMASP (UF)
        """
        ),
        make_df(
            """
            care_site_name, IS_EMERGENCY
            HOSP MATERNITE,False
            HOSP ACCUEIL URG PED (UF),True
            HOSP URGENCES,True
            HOSP HISTORIQUE DOSSIERS,False
            HOSP POLYCLINIQUE,False
            HOSP MED BUCCO DENTAIRE (UF),False
            HOSP HEPATO GASTRO ENTERO,False
            HOSP DEFIH,False
            HOSP PSYCHIATRIE,False
            HOSP ANESTHESIE-REA (UF),False
            HOSP PEDIATRIE GEN ET SAU,True
            HOSP EXPLORATIONS FONCT (UF),False
            HOSP CONSULT CHIRUR.,False
            HOSP CHIRURGIE DIGESTIVE,False
            HOSP NEONATOLOGIE,False
            HOSP PLAT AMB MEDICALE (UF),False
            HOSP CONSULT EXPLO FONCT,False
            HOSP C.I.V.G. (UF),False
            HOSP MEDECINE INTERNE,False
            HOSP HDJ PEDIATRIE (UF),False
            HOSP REA MEDICALE,False
            HOSP PNEUMOLOGIE,False
            HOSP SURV CONT MED-C (UF),False
            HOSP ONCOLOGIE (UF),False
            HOSP ADDICTOLOGIE (UF),False
            HOSP DRH,False
            HOSP ECIMUD (UF),False
            HOSP CENTRE COORD MED INT,False
            HOSP REA NEONAT (UF),False
            HOSP GERIATRIE AIGUE,False
            HOSP ACTES MEDICAUX,False
            HOSP SSR (UF),False
            HOSP PSY ADOLESCENT (UF),False
            HOSP CONSULT GERIATRIE (UF),False
            HOSP O.R.L (UF),False
            HOSP PSY NON SECTORISEE,False
            HOSP LABO HEMATO,False
            HOSP CMP CATT (UF),False
            HOSP CEGIDD (UF),False
            HOSP CTRE PORPHYRIES (UF),False
            HOSP REED POLYVAL. (UF),False
            HOSP LONG SEJOUR (UF),False
            HOSP EMASP (UF),False
        """
        ),
    ],
}


@pytest.mark.parametrize("module", ["pandas", "koalas"])
@pytest.mark.parametrize("algo", list(algos.keys()))
def test_tagging(module, algo):
    input_df = algos[algo][0]
    expected_result = algos[algo][1]

    converted_input_df = framework.to(module, input_df)

    output = tag_emergency_care_site(converted_input_df, algo=algo)

    assert_equal_no_order(framework.pandas(output), expected_result, check_like=True)
