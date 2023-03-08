from pandas import pd

from ..base import Phenotype

ICD10_CODES_DF = pd.read_csv("./codes.csv")


class PsychiatricDisorder(Phenotype):

    ICD10_CODES = {
        disorder_group: {"exact": df.ICD10_Code.to_list()}
        for disorder_group, df in ICD10_CODES_DF.groupby("disorder_group")
    }

    def __init__(
        self,
        data,
        level: str = "patient",
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
        )

        self.agg_single_feature(
            input_feature="icd10",
            level=self.level,
            subphenotype=self.subphenotype,
            threshold=self.threshold,
        )
