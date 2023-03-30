from pathlib import Path
from typing import List, Optional

import pandas as pd

from ..base import Phenotype

path_icd10 = Path(__file__).parent / "codes.csv"
ICD10_CODES_DF = pd.read_csv(path_icd10)


class PsychiatricDisorderFromICD10(Phenotype):
    """
    Phenotyping visits or patients with psychiatric disorders
    using ICD10 codes
    """

    ICD10_CODES = {
        disorder_group: {"exact": df.ICD10_Code.to_list()}
        for disorder_group, df in ICD10_CODES_DF.groupby("disorder_group")
    }
    """
    ICD10 codes used for phenotyping
    """

    ALL_DISORDER_TYPES = list(ICD10_CODES.keys())
    """
    Available disorder types.
    """

    def __init__(
        self,
        data,
        disorder_types: Optional[List[str]] = None,
        level: str = "patient",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        disorder_types :  Optional[List[str]]
            Optional list of disorder types to use for phenotyping
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

        if disorder_types is None:
            disorder_types = self.ALL_DISORDER_TYPES

        incorrect_disorder_types = set(disorder_types) - set(self.ALL_DISORDER_TYPES)

        if incorrect_disorder_types:
            raise ValueError(
                f"Incorrect cancer types ({incorrect_disorder_types}). "
                f"Available cancer types are {self.ALL_DISORDER_TYPES}"
            )

        self.icd10_codes = {
            k: v for k, v in self.ICD10_CODES.items() if k in disorder_types
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
        )

        self.agg_single_feature(
            input_feature="icd10",
            level=self.level,
            subphenotype=self.subphenotype,
            threshold=self.threshold,
        )
