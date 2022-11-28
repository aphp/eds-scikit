from dataclasses import dataclass


@dataclass
class Dataset:
    def __repr__(self):
        df_names = ", ".join([d for d in dir(self) if "__" not in d])
        return f"{self.__class__.__name__}({df_names})"
