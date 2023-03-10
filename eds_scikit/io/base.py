from ..utils.bunch import Bunch


class ComputedTables(Bunch):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        if self:
            return f"Computed tables: {', '.join(self.keys())}"
        return "No computed tables yet"

    def __str__(self):
        return self.__repr__()


class BaseData:
    def __init__(self):
        self.computed = ComputedTables()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}\n"
            "=========\n"
            f"Tables: {self.list_available_tables()}\n"
            f"Computed: {self.computed}"
        )
