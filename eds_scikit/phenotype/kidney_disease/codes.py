from eds_scikit.biology import ConceptsSet

# structured
# from PMSI

CONFIGS_CKD_DIAG = dict(
    codes_ICD10=dict(
        CKD_stage_1=dict(
            exact=["N181"],
        ),
        CKD_stage_2=dict(
            exact=["N182"],
        ),
        CKD_stage_3=dict(
            exact=["N183"],
        ),
        CKD_stage_4=dict(
            exact=["N184"],
        ),
        CKD_stage_5=dict(
            exact=["N185"],
        ),
        CKD_stage_term=dict(
            exact=["N180"],
        ),
    ),
    date_from_visit=False,  # use visit start datetime as the code datetime
    additional_filtering=dict(condition_status_source_value={"DP", "DAS", "DR"}),
)


CONFIGS_DIALYSE = dict(
    codes_ICD10=dict(
        dialyse=dict(
            exact=[
                "Y841",
                "Z49",
                # "Z490",
                "Z491",
                "Z492",
                "Z992",
                "T824",
                "Y602",
                "Y612",
                "Y622",
            ],
        ),
    ),
    codes_CCAM=dict(
        dialyse=dict(
            exact=[
                # "HPLC035",
                # "HPLA005",
                "JVJB001",
                "JVJB002",
                "JVJF002",
                "JVJF003",
                "JVJF004",
                "JVJF005",
                "JVJF006",
                "JVJF007",
                "JVJF008",
                "JVRP004",
                "JVRP007",
                "JVRP008",
                # "HPLB004",
                # "HPLC035",
                # "HPPA004",
                # "HPPP002",
                # "HPKA002",
                # "HPKB001",
                # "HPKC014",
            ],
        ),
    ),
    date_from_visit=True,  # If set to True, uses visit_start_datetime as the code datetime
    additional_filtering=dict(condition_status_source_value={"DP", "DAS", "DR"}),
)


CONFIGS_DIAG_CONCO = dict(
    codes_ICD10=dict(
        acute_kidney_failure=dict(
            exact=[
                "N17",
                "N170",
                "N171",
                "N172",
                "N178",
                "N179",
                "O904",
                # "N990",
                # "O084",
                "T795",
            ],
        ),
        choc=dict(
            exact=[
                "R570",
                "R571",
                "R572",
            ],
        ),
        # volume_depletion=dict(
        #     exact=[
        #         "E86",
        #     ],
        # ),
        sepsis=dict(
            exact=[
                "A227",
                "A267",
                "A40",
                "A41",
                "R651",
                "A427",
                "B377",
                "A548",
                "A327",
            ],
        ),
        acute_kidney_pb=dict(
            exact=["N13"],
        ),
        kidney_disease=dict(
            exact=["N19", "N990", "O084"],
        ),
    ),
    codes_CCAM=dict(
        acute_kidney_failure=dict(
            exact=[
                "JVJF005",
                "JVJF002",
                "JVJB002",
                "JVJF007",
                "JVJF006",
            ],
        ),
    ),
    date_from_visit=False,  # use event start datetime as the code datetime
    additional_filtering=dict(condition_status_source_value={"DP", "DAS", "DR"}),
)


CONFIGS_KD = dict(
    codes_ICD10=dict(
        kidney_disease=dict(
            exact=[
                "N188",
                "N189",
                # "N19",
                "P960",
                "I131",
                "I132",
                "I120",
                "N250",
            ],
        ),
        chronic_kidney_pb=dict(
            exact=[
                "N03",
                # "N04",
                "N07",
                "N08",
                "N11",
                # "N13",
                "N14",
                "N15",
                "N16",
                "N25",
                "N26",
                "N27",
                "N28",
                "N29",
                "N04.9",
                "N139",
            ],
        ),
    ),
    codes_CCAM=dict(
        kidney_disease=dict(
            exact=[
                # "JVJB001",
                # "JVJF004",
                # "JVJF008",
                "HPLB004",
                "HPLC035",
                "HPPA004",
                "HPPP002",
                "HPKA002",
                "HPKB001",
                "HPKC014",
                "HPLA005",
            ],
        ),
    ),
    date_from_visit=True,  # use visit start datetime as the code datetime #If set to True, uses visit_start_datetime as the code datetime
    additional_filtering=dict(condition_status_source_value={"DP", "DAS", "DR"}),
)

# from bio
SERUM_CREATININE = ConceptsSet(
    name="serum_creatinine",
    concept_codes=[
        "2160-0",
        "39955-0",
        "14682-9",
        "59826-8",
        "A0094",
        "A7813",
        "F9409",
        "G1975",
        "J1172",
    ],
)

# GLOMERULAR_FILTRATION_RATE = ConceptsSet(
#     name="glomerular_filtration_rate",
#     concept_codes=[
#         "A7455",
#         "A7456",
#         "B9964",
#         "F8160",
#         "G6921",
#         "F9622",
#         "G7835",
#         "H5609",
#         "F9613",
#         "F9621",
#         "70969-1",
#         "50044-7",
#         "33914-3",
#         "62238-1",
#     ],
# )

GLOMERULAR_FILTRATION_RATE_MDRD = ConceptsSet(
    name="glomerular_filtration_rate_mdrd",
    concept_codes=[
        "F9622",
        "G7835",
        "B9964",
        "A7456",
        "A7455",
        "H5609",
    ],
)


GLOMERULAR_FILTRATION_RATE_COCKROFT = ConceptsSet(
    name="glomerular_filtration_rate_cockroft",
    concept_codes=["A2154", "A0990", "A0992", "A0991", "A0993"],
)
GLOMERULAR_FILTRATION_RATE_EPICKD = ConceptsSet(
    name="glomerular_filtration_rate_epickd",
    concept_codes=["G6921", "F8160", "F9613", "F9621"],
)


DIURESE = ConceptsSet(
    name="diurese",
    concept_codes=["3167-4", "13620-0", "A0291", "B1750", "F5573", "C8445"],
)

URINARY_PROTEINS = ConceptsSet(
    name="P24",
    concept_codes=["2889-4", "42482-0", "A1696", "J7269", "C9991", "D0065"],
)

RATIO_PROT_CREATININE = ConceptsSet(
    name="UPCR",
    concept_codes=["2890-2", "13801-6", "C3941", "E4745", "G4187"],
)

URINARY_ALBUMINE = ConceptsSet(
    name="A24",
    concept_codes=["30003-8", "14956-7", "A0204", "F6542", "F6541", "F6540", "A1506"],
)

RATIO_ALBUMINE_CREATININE = ConceptsSet(
    name="UACR",
    concept_codes=[
        "14958-3",
        "14959-1",
        "30000-4",
        "59159-4",
        "A9311",
        "E4739",
        "F2140",
        "F6061",
    ],
)

ALBUMINURY = ConceptsSet(
    name="albuminury",
    concept_codes=["14957-5", "A0205", "J7398", "B3915", "F6539", "F6538", "F6537"],
)
URINARY_CREATININE = ConceptsSet(
    name="urinary_creatinine",
    concept_codes=["2161-8", "C8222"],
)
PROTEINURY = ConceptsSet(
    name="proteinury",
    concept_codes=["1753-3", "20454-5", "A1684"],
)

urinary_test_concepts = [
    "P24",
    "UPCR",
    "A24",
    "UACR",
]

urinary_raw_measures = [
    "albuminury",
    "urinary_creatinine",
    "proteinury",
]
# urinary tests concept sets
kd_biological_measures = [
    # URINARY_PROTEINS,
    # RATIO_PROT_CREATININE,
    # URINARY_ALBUMINE,
    # RATIO_ALBUMINE_CREATININE,
    # ALBUMINURY,
    # URINARY_CREATININE,
    # PROTEINURY,
    # DIURESE,
    SERUM_CREATININE,
    # GLOMERULAR_FILTRATION_RATE,
    GLOMERULAR_FILTRATION_RATE_MDRD,
    GLOMERULAR_FILTRATION_RATE_COCKROFT,
    GLOMERULAR_FILTRATION_RATE_EPICKD,
]


# NLP params
patterns_kd = dict(
    source="atteinte_renale",
    regex=[
        r"(?i)\b(nephropa?t?h?i?e?\s*diabetiq?u?e?)\b",
        r"(?i)\b(nephropa?t?h?i?e?\s*diabetiq?u?e?)\b",
        r"(?i)\b(nephropa?t?h?i?e?\s*diabetic?)\b",
        r"(?i)\b(nephropa?t?h?y?\s*diabetic?)\b",
        r"(?i)\b(nephropa?t?h?y?\s*diabetiq?u?e?)\b",
        r"(?i)\b(glomerulo\s*pathi?e?)\b",
        r"(?i)\b(syndr?o?m?e?\s*nephritique)\b",
        r"(?i)\b(syndr?o?m?e?\s*nephritic)\b",
        r"(?i)\b(syndr?o?m?e?\s*nephrotique)\b",
        r"(?i)\b(syndr?o?m?e?\s*nephrotic)\b",
        r"(?i)\b(nephropath?i?e?|nephropt|nephropathy|nehpropathy|nehpropath?i?e?)\b",
        r"(?i)\b(glomerulo\s*pathie|glomerulo\s*pathy)\b",
        r"(?i)\b(nephrite?\s*tubulo[\s|\-]*interstitiell?e?)\b",
        r"(?i)\b(nehprite?\s*tubulo[\s|\-]*interstitiell?e?)\b",
        r"(?i)\b(uropath?ie\s*obstructive)\b",
        r"(?i)\b(uropath?ie\s*par\s*reflux?)\b",
        r"(?i)\b(uropath?ie\s*obstructive\s*e?t?\s*par\s*reflux?)\b",
        r"(?i)\b(atteinte?\s*tubulo[\s|\-]*interstitiell?e?)\b",
        r"(?i)\b(tubulopath?ie\s*renale?)\b",
        r"(?i)\b(fibrose\s*renale?)\b",
    ],
    terms=[
        "nephropathie diabetique",
        "glomerulonephrite",
        "GN",
        "syndrome nephritique",
        "syndrome nephrotique",
        "nephropathie",
        "glomerulopathie",
        "nephrite tubulo-interstitielle",
        "uropathie obstructive",
        "uropathie obstructive et par reflux",
        "uropathie par reflux",
        "atteinte tubulo interstitielle",
        "tubulopathie renale",
        "fibrose renale",
    ],
    regex_attr="NORM",
    # exclude=dict(
    #     regex=[
    #          r"(?i)\bulcere\s*cutanee?\b",
    #         r"(?i)\bulcere\s*veineux?\b"
    #     ],
    #     window=3,
    # )
    # assign=[
    #     dict(
    #         name="value",
    #         regex=r"\b(\d+[\.|\,]*\d+)\b",
    #         replace_entity=False,
    #         reduce_mode="keep_first",
    #         window=10,
    #     ),
    # dict(
    #     name="range_val",
    #     regex=r"\b(\d+[\.]*\d+\-\s*\d+\s*[\.]*\s*\d+)\b",
    #     replace_entity=False,
    #     window=15,
    # ),
    # dict(
    #     name="unit",
    #     regex=r"(?i)\b(m?mol*\/l|µmol*\/l|umol*\/l)\b",
    #     replace_entity=False,
    #     window=10,
    # ),
    # dict(
    #     name="kaliemie_hemo",
    #     regex=r"(?i)\b(hemolysee?)\b",
    #     replace_entity=False,
    #     window=(-7, 7),
    # ),
    # dict(
    #     name="value_normality",
    #     regex=r"(?i)\b(normale?|anormale?|hauts?|basses?|normaux|anormaux|absence|absent)\b",
    #     replace_entity=False,
    #     reduce_mode="keep_first",
    #     window=(-20,20),
    # ),
    # ],
)
