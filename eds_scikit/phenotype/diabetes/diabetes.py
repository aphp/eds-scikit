from pathlib import Path

import pandas as pd

from ..base import Phenotype

ICD10_CODES_DF = pd.read_csv(Path(__file__).parent / "codes.csv")


class DiabetesFromICD10(Phenotype):

    ICD10_CODES = {
        diabetes_type: {"prefix": df.code.to_list()}
        for diabetes_type, df in ICD10_CODES_DF.groupby("Diabetes type")
    }

    def __init__(
        self,
        data,
        level: str = "visit",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        super().__init__(data)

        self.level = level
        self.subphenotype = subphenotype
        self.threshold = threshold

    def get(self):

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
