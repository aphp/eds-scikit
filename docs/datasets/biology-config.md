# Presentation

This dataset is the default configuration used in the [``bioclean()``][eds_scikit.biology.cleaning.main.bioclean] function. Each row corresponds to a given biological ``concept`` and a given ``unit`` and the columns contain various informations.

!!! aphp "Configuration"

    This default configuration is based on statistical summaries of AP-HP's biological measurements.

It can be generated from the [create_config_from_stats][eds_scikit.biology.utils.config.create_config_from_stats] function.

To list all available configurations, use [list_all_configs()][eds_scikit.biology.utils.config.list_all_configs].


## Structure and usage

Internally, the dataset is returned by calling the function `get_biology_config()`:

```python
from eds_scikit.resources import registry
df = registry.get("data", function_name="get_biology_config")()
```

## Use your own data.

The simplest way to generate your own configuration file is to use the [create_config_from_stats][eds_scikit.biology.utils.config.create_config_from_stats] function. Simply provide a name via the `config_name` parameter:

```python
from eds_scikit.biology.utils.config import create_config_from_stats
...
create_config_from_stats(..., config_name="my_custom_config", ...)
```

You can now provide this `config_name` to every function that accepts it, especially the [`bioclean()`][eds_scikit.biology.cleaning.main.bioclean] function.
