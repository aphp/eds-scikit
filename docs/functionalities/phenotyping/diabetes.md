# Diabetes

## Presentation

For the moment, we provide a diabetes phenotyping function based solely on ICD-10 codes.

## The `diabetes_from_icd10()` function

{{ load_data }}

```python

from eds_scikit.event import diabetes_from_icd10

visit_occurrence = diabetes_from_icd10(
    data.condition_occurrence,
    data.visit_occurrence,
)

```

The snippet above will run *as is* and add two columns to the `condition_occurrence` DataFrame:

- A `"concept"` column, containing the `"DIABETES_FROM_ICD10"` value
- A `"value"` column, containing the type of diabetes extracted

Please check [the code reference][eds_scikit.event.diabetes.diabetes_from_icd10] for a complete explanation of the function.
