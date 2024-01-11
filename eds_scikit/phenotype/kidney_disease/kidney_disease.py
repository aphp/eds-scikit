from pathlib import Path
from typing import List, Optional

import pandas as pd

from ..base import Phenotype

from .codes import *

class KidneyDisease(Phenotype):
    """
    Phenotyping visits or patients using ICD10 codes, CCAM and biology.
    """
    
    def __init__(
        self,
        data,
        level: str = "visit",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        level : str
            On which level to do the aggregation,
            either "patient" or "visit"
        subphenotype : bool
            Whether the threshold should apply to the phenotype
            ("phenotype" column) of the subphenotype ("subphenotype" column)
        threshold : int
            Minimal number of *events* (which definition depends on the `level` value)
        """
        super().__init__(data)

        self.config_CKD_diag = CONFIGS_CKD_DIAG
        self.config_dialysis = CONFIGS_DIALYSE
        self.config_conco_diag = CONFIGS_DIAG_CONCO
        self.config_other_kd_diag = CONFIGS_KD
        self.config_biology = kd_biological_measures

        self.level = level
        self.subphenotype = subphenotype
        self.threshold = threshold

    def compute_is_CKD(self):

        self.add_code_feature(
            output_feature="is_CKD_icd10",
            source="icd10",
            codes=self.config_CKD_diag["codes_ICD10"],
            additional_filtering=self.config_CKD_diag["additional_filtering"],
            date_from_visit=self.config_CKD_diag["date_from_visit"]
        )

    def compute_has_IRA(self):

        self.add_code_feature(
            output_feature="is_CKD_icd10",
            source="icd10",
            codes=self.config_CKD_diag["codes_ICD10"],
            additional_filtering=self.config_CKD_diag["additional_filtering"],
            date_from_visit=self.config_CKD_diag["date_from_visit"]
        )

        
    def compute_has_dialysis(self):

        self.add_code_feature(
            output_feature="has_dialysis_icd10",
            source="icd10",
            codes=self.config_dialysis["codes_ICD10"],
            additional_filtering=self.config_CKD_diag["additional_filtering"],
            date_from_visit=self.config_CKD_diag["date_from_visit"]
        )
        
        self.add_code_feature(
            output_feature="has_dialysis_ccam",
            source="ccam",
            codes=self.config_dialysis["codes_CCAM"],
            additional_filtering=self.config_CKD_diag["additional_filtering"],
            date_from_visit=self.config_CKD_diag["date_from_visit"]
        )
        
        self.agg_two_features(
            "has_dialysis_icd10",
            "has_dialysis_ccam",
            "has_dialysis"
            "OR",
            level=self.level,
            subphenotype=self.subphenotype,
            #threshold=(self.threshold, self.threshold)
        )

    def compute(self):
        """
        Fetch all necessary features and perform aggregation
        """
        self.add_code_feature(
            output_feature="icd10",
            source="icd10",
            codes=self.ICD10_CODES,
            additional_filtering=dict(condition_status_source_value={"DP", "DAS"}),
        )

        self.agg_single_feature(
            input_feature="icd10",
            level=self.level,
            subphenotype=self.subphenotype,
            threshold=self.threshold,
        )
