from eds_scikit.utils.typing import DataFrame


class CustomImplem:
    @classmethod
    def add_unique_id(
        cls, obj: DataFrame, col_name: str = "id", use_pd=True
    ) -> DataFrame:
        if use_pd:
            obj[col_name] = range(obj.shape[0])
            return obj
        else:
            return obj.koalas.attach_id_column(id_type="distributed", column=col_name)
