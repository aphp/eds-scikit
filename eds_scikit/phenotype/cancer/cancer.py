from pathlib import Path
from typing import List, Optional

import pandas as pd

from eds_scikit.io import BaseData

from ..base import Phenotype

path_icd10 = Path(__file__).parent / "codes.csv"
ICD10_CODES_DF = pd.read_csv(path_icd10)


class CancerFromICD10(Phenotype):
    """
    Phenotyping visits or patients using ICD10 cancer codes
    """

    ICD10_CODES = {
        cancer_type: {"prefix": df.code.to_list()}
        for cancer_type, df in ICD10_CODES_DF.groupby("Cancer type")
    }
    """
    For each cancer type, contains a set of corresponding ICD10 codes.
    """

    ALL_CANCER_TYPES = list(ICD10_CODES.keys())
    """
    Available cancer types.
    """

    def __init__(
        self,
        data: BaseData,
        cancer_types: Optional[List[str]] = None,
        level: str = "patient",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        cancer_types :  Optional[List[str]]
            Optional list of cancer types to use for phenotyping
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

    def compute(self):
        """
        Fetch all necessary features and perform aggregation
        """
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
