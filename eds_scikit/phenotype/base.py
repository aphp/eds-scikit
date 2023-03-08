import re
from typing import Optional

from loguru import logger

from eds_scikit.event import conditions_from_icd10, procedures_from_ccam
from eds_scikit.io import BaseData
from eds_scikit.utils.framework import bd
from eds_scikit.utils.typing import DataFrame


class Features:

    REQUIRED_COLUMNS: set = {"person_id", "phenotype"}

    def __init__(self):
        self._features = {}
        self.last_feature = None

    def __bool__(self):
        return bool(self._features)

    def __repr__(self):
        return "Features: " + ", ".join(self._features.keys())

    def __contains__(self, feature_name: str):
        return feature_name in self._features

    def __getitem__(self, feature_name: str):
        if feature_name not in self._features:
            raise KeyError(f"No feature named {feature_name}")
        return self._features[feature_name]

    def __setitem__(self, feature_name: str, feature: DataFrame):
        missing_columns = self.REQUIRED_COLUMNS - set(feature.columns)
        if missing_columns:
            raise ValueError(
                f"Cannot add feature {feature_name}: Columns {missing_columns} are missing"
            )

        self._features[feature_name] = feature
        self.last_feature = feature_name

    def last(self):
        logger.info(f"Returning last added feature '{self.last_feature}'")
        return self._features[self.last_feature]


class Phenotype:
    def __init__(
        self,
        data: BaseData,
        name: Optional[str] = None,
        **kwargs,
    ):
        self.data = data
        self.features = Features()
        self.name = (
            to_valid_variable_name(name)
            if name is not None
            else self.__class__.__name__
        )
        self.logger = logger.bind(classname=self.name, sep=".")

    def __repr__(self):
        return f"{self.name} : " + self.features.__repr__()

    def add_code_feature(
        self,
        output_feature: str,
        codes: dict,
        source: str = "icd10",
        additional_filtering: dict = None,
    ):
        """
        Adds a feature from either ICD10 or CCAM codes

        Parameters
        ----------
        output_feature: str
            Name of the feature

        codes: dict
            Dictionary of codes to provide to the `from_codes` function

        source: str, default='icd10'
            Either 'icd10' or 'ccam'

        additional_filtering: dict, default=None
            Dictionary passed to the `from_codes` functions for filtering
        """
        additional_filtering = additional_filtering or dict()

        if source not in ["icd10", "ccam"]:
            raise ValueError(f"source should be either 'icd10' or 'ccam', got {source}")

        self.logger.info(f"Getting {source.upper()} features...")

        from_code_func = (
            conditions_from_icd10 if (source == "icd10") else procedures_from_ccam
        )
        codes_df = (
            self.data.condition_occurrence
            if (source == "icd10")
            else self.data.procedure_occurrence
        )

        df = from_code_func(
            codes_df,
            codes=codes,
            additional_filtering=additional_filtering,
            date_from_visit=False,
        )
        df["phenotype"] = self.name
        df = df.rename(columns={"concept": "subphenotype"})

        bd.cache(df)

        self.features[output_feature] = df

        self.logger.info(
            f"{source.upper()} features stored in self.features['{output_feature}'] (N = {len(df)})"
        )

        return self

    def agg_single_feature(
        self,
        input_feature: str,
        output_feature: Optional[str] = None,
        level: str = "patient",
        subphenotype: bool = True,
        threshold: int = 1,
    ):
        """
        Simple aggregation rule on a feature
        - If level="patient", keeps patients with at least `threshold`
          visits showing the (sub)phenotype
        - If level="visit", keeps visits with at least `threshold` events
          (could be ICD10 codes, NLP features, biology, etc) showing the (sub)phenotype
        """

        assert level in {"patient", "visit"}

        output_feature = output_feature or f"{input_feature}_agg"

        if input_feature not in self.features:
            raise ValueError(
                f"Input feature {input_feature} not found in self.features. "
                "Maybe you forgot to call self.get_features() ?"
            )

        # We use `size` below for two reasons
        # 1) to use it with the `threshold` parameter directly if level == 'visit'
        # 2) to drop duplicates on the group_cols + ["visit_occurrence_id"] subset

        phenotype_type = "subphenotype" if subphenotype else "phenotype"
        group_cols = ["person_id", phenotype_type]

        group_visit = (
            self.features[input_feature]
            .groupby(group_cols + ["visit_occurrence_id"])
            .size()
            .rename("N")  # number of events per visit_occurrence
            .reset_index()
        )

        if level == "patient":
            group_visit = (
                group_visit.groupby(group_cols)
                .size()
                .rename("N")  # number of visits per person
                .reset_index()
            )

        group_visit = group_visit[group_visit["N"] >= threshold].drop(columns="N")
        group_visit["phenotype"] = self.name

        bd.cache(group_visit)

        self.features[output_feature] = group_visit

        self.logger.info(
            f"Aggregation from {input_feature} stored in self.features['{output_feature}'] "
            f"(N = {len(group_visit)})"
        )

        return self

    def agg_two_features(
        self,
        input_feature_1,
        input_feature_2,
        output_feature: str = None,
        how="AND",
        level="patient",
        subphenotype: bool = True,
        thresholds=(1, 1),
    ):
        """
        With level='patient', keeps a specific patient if
        - At least thresholds[0] visits are found in feature_1 AND/OR
        - At least thresholds[1] visits are found in feature_2

        With level='visit', keeps a specific visit if
        - At least thresholds[0] events are found in feature_1 AND/OR
        - At least thresholds[1] events are found in feature_2
        """

        self.agg_single_feature(
            input_feature=input_feature_1,
            level=level,
            subphenotype=subphenotype,
            threshold=thresholds[0],
        )

        self.agg_single_feature(
            input_feature=input_feature_2,
            level=level,
            subphenotype=subphenotype,
            threshold=thresholds[1],
        )

        results_1 = self.features[f"{input_feature_1}_agg"]
        results_2 = self.features[f"{input_feature_2}_agg"]

        assert set(results_1.columns) == set(results_2.columns)

        if how == "AND":
            result = results_1.merge(results_2, on=list(results_1.columns), how="inner")
        elif how == "OR":
            result = bd.concat(
                [
                    results_1,
                    results_2,
                ]
            ).drop_duplicates()
        else:
            raise ValueError(f"'how' options are ('AND', 'OR'), got {how}.")

        bd.cache(result)

        output_feature = output_feature or f"{input_feature_1}_{how}_{input_feature_2}"
        self.features[output_feature] = result

        self.logger.info(
            f"Aggregation from {input_feature_1} {how} {input_feature_1} stored in self.features['{output_feature}'] "
            f"(N = {len(result)})"
        )
        return self

    def get(self, **kwargs):
        raise NotImplementedError()

    def to_data(self, key: Optional[str] = None):

        if not self.features:
            self.get()

        if key is None:
            self.logger.info("No key provided: Using last added feature.")
            return self._set(self.features.last())

        else:
            assert (
                key in self.features
            ), f"Key {key} not found in features. Available {self.features}"
            self.logger.info("Using feature {key}")
            return self._set(self.features[key])

    def _set(self, result: DataFrame):
        setattr(self.data.computed, self.name, result)
        self.logger.info(
            f"<light-green>Phenotype available under data.computed.{self.name} (N={len(result)})</light-green>"
        )

        return self.data


def to_valid_variable_name(s: str):
    """
    Converts a string to a valid variable name
    """
    # Replace non-alphanumeric characters with underscores
    s = re.sub(r"\W+", "_", s)
    # Remove leading underscores
    s = re.sub(r"^_+", "", s)
    # If the string is empty or starts with a number, prepend an underscore
    if not s or s[0].isdigit():
        s = "_" + s
    return s
