import inspect
import re
from pathlib import Path
from typing import Optional, Tuple

from loguru import logger

from eds_scikit.event import conditions_from_icd10, procedures_from_ccam
from eds_scikit.io import BaseData
from eds_scikit.utils.framework import bd
from eds_scikit.utils.typing import DataFrame


class Features:
    """
    Class used to store features (i.e. DataFrames). Features are
    stored in the self._features dictionary.
    """

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
    """
    Base class for phenotyping
    """

    def __init__(
        self,
        data: BaseData,
        name: Optional[str] = None,
        **kwargs,
    ):
        """
        Parameters
        ----------
        data : BaseData
            A BaseData object
        name : Optional[str]
            Name of the phenotype. If left to None,
            the name of the class will be used instead
        """
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
        additional_filtering: Optional[dict] = None,
    ):
        """
        Adds a feature from either ICD10 or CCAM codes

        Parameters
        ----------
        output_feature : str
            Name of the feature
        codes : dict
            Dictionary of codes to provide to the `from_codes` function
        source : str,
            Either 'icd10' or 'ccam', by default 'icd10'
        additional_filtering : Optional[dict]
            Dictionary passed to the `from_codes` functions for filtering

        Returns
        -------
        Phenotype
            The current Phenotype object with an additional feature
            stored in self.features[output_feature]

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
    ) -> "Phenotype":
        """
        Simple aggregation rule on a feature:

        - If level="patient", keeps patients with at least `threshold`
          visits showing the (sub)phenotype
        - If level="visit", keeps visits with at least `threshold` events
          (could be ICD10 codes, NLP features, biology, etc) showing the (sub)phenotype

        Parameters
        ----------
        input_feature : str
            Name of the input feature
        output_feature : Optional[str]
            Name of the input feature. If None, will be set to
            input_feature + "_agg"
        level : str
            On which level to do the aggregation,
            either "patient" or "visit"
        subphenotype : bool
            Whether the threshold should apply to the phenotype
            ("phenotype" column) of the subphenotype ("subphenotype" column)
        threshold : int, optional
            Minimal number of *events* (which definition depends on the `level` value)

        Returns
        -------
        Phenotype
            The current Phenotype object with an additional feature
            stored in self.features[output_feature]

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
        input_feature_1: str,
        input_feature_2: str,
        output_feature: str = None,
        how: str = "AND",
        level: str = "patient",
        subphenotype: bool = True,
        thresholds: Tuple[int, int] = (1, 1),
    ) -> "Phenotype":
        """

        - If level='patient', keeps a specific patient if
            - At least `thresholds[0]` visits are found in feature_1 AND/OR
            - At least `thresholds[1]` visits are found in feature_2

        - If level='visit', keeps a specific visit if
            - At least `thresholds[0]` events are found in feature_1 AND/OR
            - At least `thresholds[1]` events are found in feature_2

        Parameters
        ----------
        input_feature_1 : str
            Name of the first input feature
        input_feature_2 : str
            Name of the second input feature
        output_feature : str
            Name of the input feature. If None, will be set to
            input_feature + "_agg"
        how : str, optional
            Whether to perform a boolean "AND" or "OR" aggregation
        level : str
            On which level to do the aggregation,
            either "patient" or "visit"
        subphenotype : bool
            Whether the threshold should apply to the phenotype
            ("phenotype" column) of the subphenotype ("subphenotype" column)
        thresholds : Tuple[int, int], optional
            Repsective threshold for the first and second feature

        Returns
        -------
        Phenotype
            The current Phenotype object with an additional feature
            stored in self.features[output_feature]
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

    def compute(self, **kwargs):
        """
        Fetch all necessary features and perform aggregation
        """
        raise NotImplementedError()

    def to_data(self, key: Optional[str] = None) -> BaseData:
        """
        Appends the feature found in self.features[key] to the data object.
        If no key is provided, uses the last added feature

        Parameters
        ----------
        key : Optional[str]
            Key of the self.feature dictionary

        Returns
        -------
        BaseData
            The data object with phenotype added to `data.computed`
        """

        if not self.features:
            self.compute()

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
        """
        Set the result DataFrame to the data object

        Parameters
        ----------
        result : DataFrame
            _description_

        Returns
        -------
        _type_
            _description_
        """
        setattr(self.data.computed, self.name, result)
        self.logger.info(
            f"<light-green>Phenotype available under data.computed.{self.name} (N={len(result)})</light-green>"
        )

        return self.data

    def cite(self):

        if self.__class__.__module__ == "__main__":
            base_path = Path.cwd()
        else:
            base_path = Path(inspect.getfile(self.__class__)).parent
        citation_path = list(base_path.glob("*.bib"))

        if not citation_path:
            raise FileNotFoundError(
                f"No .bib file was found for {self.name} in {base_path}"
            )

        algo = getattr(self, "algo", None)

        if algo is None:
            # Only one phenotyping algorithm:
            citation_path = citation_path.pop()

        else:
            expected_citation_path = base_path / f"{algo}.bib"
            if expected_citation_path not in citation_path:
                raise FileNotFoundError(
                    f"Phenotype {self.__class__.__name__} with algo={self.algo} "
                    f"expects a bib file named {expected_citation_path.name}"
                )
            citation_path = expected_citation_path

        with open(citation_path, "r") as f:
            citation = f.read()
        print(citation)


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
