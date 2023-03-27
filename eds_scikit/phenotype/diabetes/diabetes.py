from pathlib import Path
from typing import List, Optional

import pandas as pd

from ..base import Phenotype

path_icd10 = Path(__file__).parent / "codes.csv"
ICD10_CODES_DF = pd.read_csv(path_icd10)


class DiabetesFromICD10(Phenotype):
    """
    Phenotyping visits or patients using ICD10 diabetes codes
    """

    ICD10_CODES = {
        diabetes_type: {"prefix": df.code.to_list()}
        for diabetes_type, df in ICD10_CODES_DF.groupby("Diabetes type")
    }

    ALL_DIABETES_TYPES = list(ICD10_CODES.keys())
    """
    Available diabetes types.
    """

    def __init__(
        self,
        data,
        diabetes_types: Optional[List[str]] = None,
        level: str = "visit",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        diabetes_types :  Optional[List[str]]
            Optional list of diabetes types to use for phenotyping
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

        if diabetes_types is None:
            diabetes_types = self.ALL_DIABETES_TYPES

        incorrect_diabetes_types = set(diabetes_types) - set(self.ALL_DIABETES_TYPES)

        if incorrect_diabetes_types:
            raise ValueError(
                f"Incorrect diabetes types ({incorrect_diabetes_types}). "
                f"Available diabetes types are {self.ALL_DIABETES_TYPES}"
            )

        self.icd10_codes = {
            k: v for k, v in self.ICD10_CODES.items() if k in diabetes_types
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
            codes=self.ICD10_CODES,
            additional_filtering=dict(condition_status_source_value={"DP", "DAS"}),
        )

        self.agg_single_feature(
            input_feature="icd10",
            level=self.level,
            subphenotype=self.subphenotype,
            threshold=self.threshold,
        )
