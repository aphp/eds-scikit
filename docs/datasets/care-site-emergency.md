## Presentation

!!! aphp "Emergency"

     This dataset is useful to extract **emergency** care sites from AP-HP's CDW

This dataset contains care sites labelled as emergency.

Those care sites were extracted and verified by  Ariel COHEN,
Judith LEBLANC, and an ER doctor validated them.

Those emergency care sites are further divised into different categories,
as defined in the concept `"EMERGENCY_TYPE"`.

The different categories are:

- Urgences spécialisées
- UHCD + Post-urgences
- Urgences pédiatriques
- Urgences générales adulte
- Consultation urgences
- SAMU / SMUR

!!! warning
      This dataset was built in 2021.


## Structure and usage

Internally, the dataset is returned by calling the function `get_care_site_emergency_mapping()`:

```python
from eds_scikit.resources import registry
df = registry.get("data", function_name="get_care_site_emergency_mapping")()
```

It should return a Pandas Dataframe with 2 columns:

- `care_site_source_value` (OMOP column)
- `EMERGENCY_TYPE` (see above)

## Use your own data.

It is as simple as registering a new loading function:

```python title="custom_resources.py"
from eds_scikit.resources import registry

@registry.data("get_care_site_emergency_mapping")
def get_care_site_emergency_mapping():
      """
      Your code here
      """
      return df
```

Then simply import your `custom_resources` module before running EDS-Scikit's pipelines, and you're good to go.
