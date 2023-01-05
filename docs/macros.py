import os
from functools import lru_cache

import pandas as pd
from markdown.core import Markdown


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
    @lru_cache(maxsize=32)
    def get_rendered():
        config = env.variables["config"]
        plugin = config["plugins"]["mkdocstrings"]
        plugin.md = Markdown(
            extensions=config["markdown_extensions"],
            extension_configs=config["mdx_configs"],
        )
        handler = plugin.handlers.get_handler("python")
        handler.renderer._update_env(plugin.md, plugin.handlers._config)  # noqa: WPS437
        data = handler.collector.collect("eds_scikit.event", {})
        # handler.renderer.render(data, {}).to_pickle("./HANDLER.pkl")
        return handler.renderer.render(data, {})

    @env.macro
    def test_fct(x):
        return x


def _concat_lines(*lines):
    return "\n".join(lines)
