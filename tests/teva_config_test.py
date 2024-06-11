teva_config_test = {
    "visit_occurrence": {
        "category_columns": [
            "visit_occurrence_id",
            "care_site_short_name",
            "stay_source_value",
            "visit_source_value",
            "admission_reason_source_value",
            "visit_type_source_value",
            "destination_source_value",
            "cdm_source",
        ],
        "date_column": "visit_start_datetime",
        "mapper": {"visit_occurrence_id": {"not NaN": ".*"}},
    },
    "condition_occurrence": {
        "category_columns": [
            "visit_occurrence_id",
            "care_site_short_name",
            "condition_source_value",
            "stay_source_value",
            "visit_source_value",
            "admission_reason_source_value",
            "visit_type_source_value",
            "destination_source_value",
            "cdm_source",
        ],
        "date_column": "condition_start_datetime",
        "mapper": {
            "visit_occurrence_id": {"not NaN": ".*"},
            "condition_source_value": {"not NaN": ".*"},
        },
    },
    "note": {
        "category_columns": [
            "visit_occurrence_id",
            "care_site_short_name",
            "note_type_source_value",
            "note_class_source_value",
        ],
        "date_column": "visit_start_datetime",
        "mapper": {
            "visit_occurrence_id": {"not NaN": ".*"},
        },
    },
    "fake_table": {
        "category_columns": ["a", "b"],
        "date_column": "visit_start_datetime",
        "mapper": {},
    },
}
