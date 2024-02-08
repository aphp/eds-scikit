import numpy as np
import pandas as pd

from eds_scikit import datasets


class Units:
    def __init__(self, concept_sets=None, element=None):
        self.units_file = getattr(datasets, "units").set_index("unit_source_value")
        self.element_file = getattr(datasets, "elements").set_index(
            ["unit_a", "unit_b"]
        )
        self.element = element
        # on part de l'idée que les unités sont des bases, qu'il est symétrique, qu'il est complété. NB : globalement c'est essentiellement pour la masse molaire, non ? Cuillère à soupe en g peut-être ?
        self.outer_conversion = (
            self.element_file[self.element_file.element == self.element]
            if self.element
            else pd.DataFrame()
        )
        self.target_unit = ""
        self.concept_sets = concept_sets

    def add_target_unit(self, unit):
        self.target_unit = unit

    def add_conversion(self, unit_a, unit_b, conversion):
        df = pd.DataFrame(
            {
                "unit_a": [unit_a, unit_b],
                "unit_b": [
                    unit_b,
                    unit_a,
                ],
                "conversion": [conversion, 1 / conversion],
                "element": self.element,
            }
        ).set_index(["unit_a", "unit_b"])
        self.outer_conversion = pd.concat(
            (self.outer_conversion, df), axis=0
        ).drop_duplicates()

    def get_category(self, unit):  # remplacer category par base ??
        unit_tokens = unit.split("/")
        category = []
        for unit_token in unit_tokens:
            unit_token = unit_token.lower()
            if unit_token in self.units_file.index:
                unit_token_category = self.units_file.loc[unit_token].category
                category += [unit_token_category]
            else:
                category += ["Unkown"]
        return category

    def get_unit_base(self, unit) -> str:  # remplacer category par base ??
        unit_tokens = unit.lower().split("/")
        unit_base = ""
        for unit_token in unit_tokens:
            unit_base += f"/{self.base(unit_token)}"
        return unit_base[1:]

    def base(self, token):
        if token in self.units_file.index:
            return self.units_file.loc[token].unit_source_base
        else:
            return "Unkown"

    def to_base(self, token):
        if token in self.units_file.index:
            return self.units_file.loc[token].conversion
        else:
            return np.NaN

    def can_be_converted(self, unit_1, unit_2):
        unit_tokens_1 = unit_1.split("/")
        unit_tokens_2 = unit_2.split("/")

        if len(unit_tokens_1) == len(unit_tokens_2):
            can_be_converted = True
            for token_1, token_2 in zip(unit_tokens_1, unit_tokens_2):
                base_1, base_2 = self.base(token_1), self.base(token_2)
                token_1, token_2 = token_1.lower(), token_2.lower()
                can_be_converted = (
                    can_be_converted
                    and (self.base(token_1) == self.base(token_2) != "Unkown")
                    or ((base_1, base_2) in self.outer_conversion.index)
                )
            return can_be_converted
        else:
            return False

    def convert_token(self, token_1, token_2):
        token_1, token_2 = token_1.lower(), token_2.lower()
        if self.base(token_1) == self.base(token_2) != "Unkown":
            f1 = self.to_base(token_1)
            f2 = self.to_base(token_2)
            return f1 / f2

        base_1, base_2 = self.base(token_1), self.base(token_2)
        if (base_1, base_2) in self.outer_conversion.index:
            f1 = self.to_base(token_1)
            f2 = self.to_base(token_2)
            f3 = self.outer_conversion.loc[(base_1, base_2)].conversion
            return f1 * f3 / f2
        else:
            return np.NaN

    def convert_unit(self, unit_1, unit_2) -> float:
        unit_1, unit_2 = unit_1.lower(), unit_2.lower()
        tokens_1, tokens_2 = unit_1.split("/"), unit_2.split("/")
        f = self.convert_token(tokens_1[0], tokens_2[0])
        for token_1, token_2 in zip(tokens_1[1:], tokens_2[1:]):
            f = f / self.convert_token(token_1, token_2)
        return f
