default_tables_to_save = [
    "person",
    "visit_occurrence",
    "visit_detail",
    "condition_occurrence",
    "procedure_occurrence",
    "care_site",
    "concept",
]
"""
The default tables loaded when instanciating a [HiveData][eds_scikit.io.hive.HiveData]
or a [PostgresData][eds_scikit.io.postgres.PostgresData]
"""

tables_to_load = {
    "person": [
        # "key",
        "person_id",
        # "person_source_value",
        "location_id",
        # "provider_id",
        # "care_site_id",
        "year_of_birth",
        "month_of_birth",
        "day_of_birth",
        "birth_datetime",
        "death_datetime",
        # "race_concept_id",
        # "race_source_value",
        # "race_source_concept_id",
        # "ethnicity_concept_id",
        # "ethnicity_source_value",
        # "ethnicity_source_concept_id",
        # "gender_concept_id",
        "gender_source_value",
        "gender_source_concept_id",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "visit_occurrence": [
        # "key",
        "visit_occurrence_id",
        "person_id",
        "visit_occurrence_source_value",
        "preceding_visit_occurrence_id",
        # "provider_id",
        "care_site_id",
        # "visit_start_date",
        "visit_start_datetime",
        # "visit_end_date",
        "visit_end_datetime",
        # "visit_concept_id",
        "visit_source_value",
        "visit_source_concept_id",
        # "visit_type_concept_id",
        "visit_type_source_value",
        "visit_type_source_concept_id",
        # "admitted_from_concept_id",
        "admitted_from_source_value",
        "admitted_from_source_concept_id",
        # "discharge_to_concept_id",
        "discharge_to_source_value",
        "discharge_to_source_concept_id",
        # "row_status_concept_id",
        "row_status_source_value",
        # "row_status_source_concept_id",
        # "stay_concept_id",
        "stay_source_value",
        "stay_source_concept_id",
        "cdm_source",
    ],
    "care_site": [
        # "key",
        "care_site_id",
        "care_site_source_value",
        # "location_id",
        "care_site_name",
        "care_site_short_name",
        # "place_of_service_concept_id",
        "place_of_service_source_value",
        # "place_of_service_source_concept_id",
        # "care_site_type_concept_id",
        "care_site_type_source_value",
        # "care_site_type_source_concept_id",
        "valid_start_date",
        "valid_end_date",
        # "cdm_source",
    ],
    "visit_detail": [
        # "key",
        "visit_detail_id",
        "visit_occurrence_id",
        "person_id",
        "preceding_visit_detail_id",
        "visit_detail_parent_id",
        # "provider_id",
        "care_site_id",
        "visit_detail_start_date",
        "visit_detail_start_datetime",
        "visit_detail_end_date",
        "visit_detail_end_datetime",
        # "visit_detail_concept_id",
        "visit_detail_source_value",
        "visit_detail_source_concept_id",
        # "visit_detail_type_concept_id",
        "visit_detail_type_source_value",
        "visit_detail_type_source_concept_id",
        # "admitted_from_concept_id",
        "admitted_from_source_value",
        "admitted_from_source_concept_id",
        # "discharge_to_concept_id",
        "discharge_to_source_value",
        "discharge_to_source_concept_id",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "condition_occurrence": [
        # "key",
        "condition_occurrence_id",
        "person_id",
        "visit_occurrence_id",
        "visit_detail_id",
        # "provider_id",
        # "condition_start_date",
        "condition_start_datetime",
        # "condition_end_date",
        # "condition_end_datetime",
        # "condition_concept_id",
        "condition_source_value",
        "condition_source_concept_id",
        # "condition_type_concept_id",
        # "condition_type_source_value",
        # "condition_type_source_concept_id",
        # "condition_status_concept_id",
        "condition_status_source_value",
        "condition_status_source_concept_id",
        # "stop_reason",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    "procedure_occurrence": [
        # "key",
        "procedure_occurrence_id",
        "person_id",
        "visit_occurrence_id",
        "visit_detail_id",
        # "provider_id",
        # "procedure_date",
        "procedure_datetime",
        # "procedure_concept_id",
        "procedure_source_value",
        "procedure_source_concept_id",
        # "procedure_type_concept_id",
        # "procedure_type_source_value",
        # "procedure_type_source_concept_id",
        # "modifier_concept_id",
        # "modifier_source_value",
        # "quantity",
        # "row_status_concept_id",
        # "row_status_source_value",
        # "row_status_source_concept_id",
        "cdm_source",
    ],
    # "note": [],
    # "location": [],
    # location_history
    # measurement
    # drug_exposure
    # note_nlp
    # observation
    "concept": [
        "concept_id",
        "concept_name",
        "domain_id",
        "vocabulary_id",
        "concept_class_id",
        "standard_concept",
        "concept_code",
        "valid_start_date",
        "valid_end_date",
        "invalid_reason",
        # "hash",
    ],
    # concept_relationship
    # concept_synonym
    # fact_relationship
    # vocabulary
}
"""
The default columns loaded when instanciating a [HiveData][eds_scikit.io.hive.HiveData]
or a [PostgresData][eds_scikit.io.postgres.PostgresData]
"""

biology_codes_settings = {
    "ANABIO" :  {
        "concept_regex" : "[A-Z][0-9]{4}",
        "source_terminologies" : {
            "GLIMS_ANABIO": r"GLIMS.{0,20}Anabio",
            "ITM_ANABIO": r"ITM - ANABIO",
        }
    },
    
    "LOINC" : {
        "concept_regex" : "[0-9]{2,5}[-][0-9]",
        "source_terminologies" : {
            "GLIMS_LOINC": r"GLIMS.{0,20}Anabio",
            "ITM_LOINC": r"ITM - ANABIO",
        }
    }
}

standard_terminologies = ["LOINC", "AnaBio", "ANABIO", "ANALYSES_LABORATOIRE"]

standard_concept_regex = {
    "LOINC": "[0-9]{2,5}[-][0-9]",
    "AnaBio": "[A-Z][0-9]{4}",
    "ANABIO": "[A-Z][0-9]{4}",
}

source_terminologies = {
    "ANALYSES_LABORATOIRE": r"Analyses Laboratoire",
    "GLIMS_ANABIO": r"GLIMS.{0,20}Anabio",
    "GLIMS_LOINC": r"GLIMS.{0,20}LOINC",
    "ITM_ANABIO": r"ITM - ANABIO",
    "ITM_LOINC": r"ITM - LOINC",
}
mapping = [
    ("ANALYSES_LABORATOIRE", "GLIMS_ANABIO", "Maps to"),
    ("ANALYSES_LABORATOIRE", "GLIMS_LOINC", "Maps to"),
    ("GLIMS_ANABIO", "ITM_ANABIO", "Mapped from"),
    ("ITM_ANABIO", "ITM_LOINC", "Maps to"),
]

# make sure we know how to load the tables we want to save
assert all(table in tables_to_load.keys() for table in default_tables_to_save)


# Tables for each base
i2b2_tables = {
    "edsprod": {
        "visit_occurrence": "i2b2_orbis_visit_dim",
        "note_deid": "i2b2_observation_fact_document",
        "person": "i2b2_patient_dim",
        "condition_occurrence": "i2b2_arem_observation_fact_cim10",
        "procedure_occurrence": "i2b2_arem_observation_fact_ccam",
        "care_site": "i2b2_observation_fact_ufr",
        "visit_detail": "i2b2_observation_fact_ufr",
        "measurement": "i2b2_observation_fact_lab",
        "fact_relationship": "i2b2_observation_fact_ufr",
        "concept": "orbis_form_ref_concept_list",
    },
    "cse": {
        "visit_occurrence": "i2b2_visit",
        "note_deid": "i2b2_observation_doc",
        "person": "i2b2_patient",
        "condition_occurrence": "i2b2_observation_cim10",
        "procedure_occurrence": "i2b2_observation_ccam",
        "care_site": "i2b2_observation_ufr",
        "visit_detail": "i2b2_observation_ufr",
        "measurement": "i2b2_observation_lab",
        "fact_relationship": "i2b2_observation_ufr",
        "concept": "i2b2_concept",
        "concept_relationship": None,
    },
}


# Mapping between i2b2 and OMOP
i2b2_renaming = {
    "care_site": {
        "care_site_source_value": "location_cd",
        "care_site_short_name": "care_site_name",
    },
    "concept": {
        "concept_id": "concept_cd",
        "concept_name": "name_char",
        "concept_source_value": "concept_cd",
    },
    "condition_occurrence": {
        "cdm_source": "sourcesystem_cd",
        "condition_occurrence_id": "instance_num",
        "condition_source_value": "concept_cd",
        "condition_start_datetime": "start_date",
        "condition_status_source_value": "tval_char",
        "person_id": "patient_num",
        "visit_occurrence_id": "encounter_num",
    },
    "fact_relationship": {
        "care_site_source_value": "location_cd",
        "cdm_source": "sourcesystem_cd",
    },
    "measurement": {
        "cdm_source": "sourcesystem_cd",
        "measurement_date": "start_date",
        "measurement_datetime": "start_date",
        "measurement_id": "instance_num",
        "measurement_source_concept_id": "concept_cd",
        "person_id": "patient_num",
        "unit_source_value": "units_cd",
        "value_as_number": "nval_num",
        "visit_occurrence_id": "encounter_num",
    },
    "note_deid": {
        "cdm_source": "sourcesystem_cd",
        "note_class_source_value": "concept_cd",
        "note_datetime": "start_date",
        "note_id": "instance_num",
        "note_text": "observation_blob",
        "person_id": "patient_num",
        "row_status_source_value": "i2b2_action",
        "visit_occurrence_id": "encounter_num",
    },
    "person": {
        "birth_datetime": "birth_date",
        "cdm_source": "sourcesystem_cd",
        "death_datetime": "death_date",
        "gender_source_value": "sex_cd",
        "person_id": "patient_num",
    },
    "procedure_occurrence": {
        "cdm_source": "sourcesystem_cd",
        "person_id": "patient_num",
        "procedure_occurrence_id": "instance_num",
        "procedure_source_value": "concept_cd",
        "procedure_datetime": "start_date",
        "visit_occurrence_id": "encounter_num",
    },
    "visit_detail": {
        "care_site_id": "location_cd",
        "cdm_source": "sourcesystem_cd",
        "person_id": "patient_num",
        "row_status_source_value": "i2b2_action",
        "visit_detail_end_datetime": "end_date",
        "visit_detail_id": "instance_num",
        "visit_detail_start_datetime": "start_date",
        "visit_occurrence_id": "encounter_num",
    },
    "visit_occurrence": {
        "admitted_from_source_value": "mode_entree",
        "cdm_source": "sourcesystem_cd",
        "discharge_to_source_value": "mode_sortie",
        "person_id": "patient_num",
        "row_status_source_value": "i2b2_action",
        "visit_end_datetime": "end_date",
        "visit_occurrence_id": "encounter_num",
        "visit_occurrence_source_value": "visit_blob",
        "visit_source_value": "type_visite",
        "visit_start_datetime": "start_date",
    },
}

sex_cd_mapping = {"W": "f", "M": "m"}


dict_code_UFR = {
    "014": "APR",
    "028": "ABC",
    "095": "AVC",
    "005": "BJN",
    "009": "BRK",
    "010": "BCT",
    "011": "BCH",
    "033": "BRT",
    "016": "BRC",
    "042": "CFX",
    "019": "CRC",
    "021": "CCH",
    "022": "CCL",
    "029": "ERX",
    "036": "GCL",
    "075": "EGP",
    "038": "HND",
    "026": "HMN",
    "099": "HAD",
    "041": "HTD",
    "032": "JVR",
    "044": "JFR",
    "047": "LRB",
    "049": "LRG",
    "053": "LMR",
    "061": "NCK",
    "096": "PBR",
    "066": "PSL",
    "068": "RPC",
    "069": "RMB",
    "070": "RDB",
    "072": "RTH",
    "073": "SAT",
    "079": "SPR",
    "076": "SLS",
    "084": "SSL",
    "087": "TNN",
    "088": "TRS",
    "090": "VGR",
    "064": "VPD",
    "INC": "INCONNU",
}


visit_type_mapping = {
    "I": "hospitalisés",
    "II": "hospitalisation incomplète",
    "U": "urgence",
    "O": "consultation externe",
}
