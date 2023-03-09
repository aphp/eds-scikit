from eds_scikit.io import BaseData

from ..base import Phenotype


class SuicideAttemptFromICD10(Phenotype):

    """
    Phenotyping visits related to a suicide attempt.
    Two algorithms are available:

    - "X60-X84": The visit needs to have at least one ICD10 code in the range
    X60 to X84
    - "Haguenoer2008": The visit needs to have at least one ICD10 DAS code in the range
    X60 to X84, and a ICD10 DP code in the range S to T
    """

    ICD10_CODES = {
        "X60-X84": dict(
            codes={
                "X60-X84": dict(
                    regex=["X[67]", "X8[0-4]"],
                ),
            },
        ),
        "Haguenoer2008": dict(
            codes={
                "Haguenoer2008": dict(
                    regex=["S", "T[0-9]"],
                ),
            },
            additional_filtering=dict(condition_status_source_value="DP"),
        ),
    }
    """
    ICD10 codes used by both algorithms
    """

    def __init__(
        self,
        data: BaseData,
        algo: str = "Haguenoer2008",
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        algo : str, optional
            The name of the algorithm.
            Should be either "Haguenoer2008" or "X60-X84"
        """
        super().__init__(
            data,
            name=f"SuicideAttemptFromICD10_{algo}",
        )
        self.algo = algo

    def compute(self):
        """
        Fetch and aggregate features
        """

        if self.algo == "X60-X84":

            self.add_code_feature(
                output_feature="X60-X84",
                source="icd10",
                codes=self.ICD10_CODES["X60-X84"]["codes"],
            )

            self.agg_single_feature(
                "X60-X84",
                level="visit",
                subphenotype=False,
                threshold=1,
            )

        elif self.algo == "Haguenoer2008":

            self.add_code_feature(
                output_feature="X60-X84",
                source="icd10",
                codes=self.ICD10_CODES["X60-X84"]["codes"],
                additional_filtering=dict(condition_status_source_value="DAS"),
            )

            self.add_code_feature(
                output_feature="DP",
                source="icd10",
                codes=self.ICD10_CODES["Haguenoer2008"]["codes"],
                additional_filtering=self.ICD10_CODES["Haguenoer2008"][
                    "additional_filtering"
                ],
            )

            self.agg_two_features(
                "X60-X84",
                "DP",
                output_feature="Haguenoer2008",
                how="AND",
                level="visit",
                subphenotype=False,
                thresholds=(1, 1),
            )
