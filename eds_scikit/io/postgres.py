from typing import Optional, Tuple

import pandas as pd
import pgpasslib
import psycopg2 as pg


class PostgresData:  # pragma: no cover
    """PostgreSQL interface to run SQL queries.

    This uses the file `~/.pgpass` to find the password and extra connection infos.

    Parameters
    ----------
    dbname : str
    schema : str
    user : str
    host : str
    port : str

    Examples
    --------
    >>> data = PostgresData(dbname="YOUR_DBNAME", schema="omop", user="YOUR_USERNAME")
    >>> data.read_sql("select count(*) from person")

    """

    def __init__(
        self,
        dbname: Optional[str] = None,
        schema: Optional[str] = None,
        user: Optional[str] = None,
        host: Optional[str] = None,
        port: Optional[int] = None,
    ):
        (
            self.host,
            self.port,
            self.dbname,
            self.user,
        ) = self._find_matching_pgpass_params(host, port, dbname, user)
        self.schema = schema

    @staticmethod
    def _find_matching_pgpass_params(
        host: str,
        port: int,
        dbname: str,
        user: str,
    ) -> Tuple:
        entries = pgpasslib._get_entries()
        consolidated_params = [
            (
                host or entry.host,
                port or entry.port,
                dbname or entry.dbname,
                user or entry.user,
            )
            for entry in entries
        ]
        matching_params = [
            params
            for entry, params in zip(entries, consolidated_params)
            if entry.match(*params)
        ]

        if len(matching_params) == 0:
            raise ValueError("Could not find matching entry in .pgpass file.")
        if len(matching_params) > 1:
            message = "\n".join(
                [
                    "Several entries found in .pgpass file. Be more specific.",
                    "The following entries match what you specified :",
                    *[str(params) for params in matching_params],
                ]
            )
            raise ValueError(message)

        return matching_params[0]

    def read_sql(self, sql_query: str, **kwargs) -> pd.DataFrame:
        """Execute pandas.read_sql() on the database.

        Parameters
        ----------
        sql_query : str
            SQL query (postgres flavor)
        **kwargs
            additional arguments passed to pandas.read_sql()

        Returns
        -------
        df : pandas.DataFrame

        """
        connection_infos = {
            param: getattr(self, param) for param in ["host", "port", "dbname", "user"]
        }
        connection_infos["password"] = pgpasslib.getpass(**connection_infos)
        connection = pg.connect(**connection_infos)
        if self.schema:
            connection.cursor().execute(f"SET SCHEMA '{self.schema}'")

        df = pd.read_sql(sql_query, con=connection, **kwargs)

        connection.close()
        return df
