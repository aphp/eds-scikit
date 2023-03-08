from pandas import pd

from ..base import Phenotype

ICD10_CODES_DF = pd.read_csv("./codes.csv")


class CancerFromICD10(Phenotype):

    ICD10_CODES = {
        cancer_type: {"prefix": df.ICD10_Code.to_list()}
        for cancer_type, df in ICD10_CODES_DF.groupby("Cancer type")
    }
    ALL_CANCER_TYPES = list(ICD10_CODES.keys())

    def __init__(
        self,
        data,
        cancer_types=None,
        level: str = "patient",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        super().__init__(data)

        if cancer_types is None:
            cancer_types = self.ALL_CANCER_TYPES

        incorrect_cancer_types = set(cancer_types) - set(self.ALL_CANCER_TYPES)

        if incorrect_cancer_types:
            raise ValueError(
                f"Incorrect cancer types ({incorrect_cancer_types}). "
                f"Available cancer types are {self.ALL_CANCER_TYPES}"
            )

        self.icd10_codes = {
            k: v for k, v in self.ICD10_CODES.items() if k in cancer_types
        }

        self.level = level
        self.subphenotype = subphenotype
        self.threshold = threshold

    def get(self):

        self.add_code_feature(
            output_feature="icd10",
            source="icd10",
            codes=self.icd10_codes,
            additional_filtering=dict(condition_status_source_value={"DP", "DR"}),
        )

        self.agg_single_feature(
            input_feature="icd10",
            level=self.level,
            subphenotype=self.subphenotype,
            threshold=self.threshold,
        )
