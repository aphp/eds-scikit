import os

import pandas as pd


def define_env(env):

    env.variables["import"] = _concat_lines(
        "```python",
        "import eds_scikit" "```",
    )
    env.variables["load_data"] = _concat_lines(
        "```python",
        "from eds_scikit.io import HiveData",
        "data = HiveData(DBNAME)",
        "```",
    )

    @env.macro
    def link_repo_file(relative_path: str):
        BASE_PATH = "https://github.com/aphp/eds-scikit/blob/main"
        return os.path.join(BASE_PATH, relative_path)

    @env.macro
    def preview_csv(csv_path: str, limit=None):
        HARD_LIMIT = 100
        df = pd.read_csv(csv_path)[:HARD_LIMIT]
        if limit is not None:
            df = df[:limit]
        return df.to_markdown(index=False)

    @env.macro
    def values_from_csv(csv_path: str, col: str, indent: str = ""):
        df = pd.read_csv(csv_path)
        values = df[col].drop_duplicates().sort_values().to_list()

        return "".join(f"\n{indent}- {value}" for value in values)

    @env.macro
    def test_fct(x):
        return x


def _concat_lines(*lines):
    return "\n".join(lines)
