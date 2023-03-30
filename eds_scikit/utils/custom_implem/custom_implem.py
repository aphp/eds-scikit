from typing import Any

import pandas as pd
from databricks import koalas as ks

from .cut import cut


class CustomImplem:
    """
    A collection of custom pandas and koalas methods.

    All public facing methods must be stateless and defined as classmethods.
    """

    @classmethod
    def add_unique_id(
        cls,
        obj: Any,
        col_name: str = "id",
        backend=None,
    ) -> Any:
        """Add an ID column for koalas or pandas."""
        if backend is pd:
            obj[col_name] = range(obj.shape[0])
            return obj
        elif backend is ks:
            return obj.koalas.attach_id_column(id_type="distributed", column=col_name)
        else:
            raise NotImplementedError(
                f"No method 'add_unique_id' is available for backend '{backend}'."
            )

    @classmethod
    def cut(
        cls,
        x,
        bins,
        right: bool = True,
        labels=None,
        retbins: bool = False,
        precision: int = 3,
        include_lowest: bool = False,
        duplicates: str = "raise",
        ordered: bool = True,
        backend=None,  # unused because koalas only
    ):
        """koalas version of pd.cut

        Notes
        -----
        Simplified vendoring from:
        https://github.com/pandas-dev/pandas/blob/v1.5.2/pandas/core/reshape/tile.py#L50-L305
        """
        return cut(
            x,
            bins,
            right,
            labels,
            retbins,
            precision,
            include_lowest,
            duplicates,
            ordered,
        )

    @classmethod
    def cache(cls, df, backend=None):
        if backend is pd:
            # no-op
            return
        elif backend is ks:
            # Cache using count(), a simple action that trigger the
            # eager mode and effectively cache the dataframe.
            # See this link for more details about the count trick:
            # https://stackoverflow.com/a/44002485
            df.spark.cache().count()
            return
        else:
            raise NotImplementedError(
                f"No method 'cache' is available for backend '{backend}'."
            )
