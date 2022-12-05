## Presentation

!!! aphp "Care sites"

     This dataset is useful to link AP-HP's care sites of various levels together

To generate it, it uses the `fact_relationship` OMOP table, with the `care_site` domain and the `A is part of B` relation. Thus, it generates a wide-type table, effectively flattening out the hierarchical structure of each care site.

This dataset is useful to find the **parent of a care_site**, e.g.:

- in which hospital is this UDS (*Unité De Soin*) ?
- in which UF (*Unité Fonctionnelle*) is this UMA (*Unité Médico-Administrative*) ?

## Structure and usage

In this dataset **each row** corresponds to a given `care_site` and the **columns** contain
the ids of the parent `care_site` for several hierarchical level. Those columns are thus values contained in `care_site_type_source_value`.

Internally, the dataset is returned by calling the function `get_care_site_hierarchy()`:

```python
from eds_scikit.resources import registry
df = registry.get("data", function_name="get_care_site_hierarchy")()
```

## Use your own data.

It is as simple as registering a new loading function:

```python title="custom_resources.py"
from eds_scikit.resources import registry # (1)

@registry.data("get_care_site_hierarchy") # (2)
def get_care_site_hierarchy():
      """
      Your code here
      """
      return df
```

1. The `registry` instance stores user-defined functions
2. Using this decorator allows to register the function when importing the corresponding file

Then simply import your `custom_resources` module before running eds-scikit's pipelines, and you're good to go.

## Structure and usage

Internally, the dataset is returned by calling the function `get_care_site_hierarchy()`.
It should return a Pandas Dataframe with the following columns:

- `care_site_id` (OMOP column): The identifier of the care site
- `care_site_type_source_value` (OMOP column): The type of care site

Additionally, it can contains an arbitrary number of columns whose name are values from `care_site_type_source_value`, and whose values are `care_site_id` of the corresponding parent structure

## Generation function

You can generate the dataset on your specific data using [this function][eds_scikit.datasets.generation_scripts.care_site_hierarchy.generate_care_site_hierarchy]
