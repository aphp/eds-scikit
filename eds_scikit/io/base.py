from box import Box


class ComputedTables(Box):
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
