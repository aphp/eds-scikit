from ..base import Phenotype


class SuicideAttempts(Phenotype):

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

    def __init__(
        self,
        data,
        algo: str = "Haguenoer2008",
    ):
        super().__init__(
            data,
            name=f"SuicideAttempts_{algo}",
        )
        self.algo = algo

    def get(self):

        self.add_code_feature(
            output_feature="X60-X84",
            source="icd10",
            codes=self.ICD10_CODES["X60-X84"]["codes"],
        )

        if self.algo == "X60-X84":

            self.agg_single_feature(
                "X60-X84",
                level="visit",
                subphenotype=False,
                threshold=1,
            )

        elif self.algo == "Haguenoer2008":
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
