# Using ICD-10 and CCAM

eds-scikit provides two functions to ease the extraction of occurrrences of

- [ICD-10 codes][eds_scikit.event.conditions_from_icd10] : `eds_scikit.event.icd10.conditions_from_icd10`
- [CCAM codes][eds_scikit.event.procedures_from_ccam] : `eds_scikit.event.ccam.procedures_from_ccam`

These two functions are by design similar. In fact, they call under the hood the same [base function][eds_scikit.event.from_code.event_from_code].

Let us see a minimal  working example that would allow us to select patients with Deep Vein Thrombosis based on the presence of specific ICD-10 codes.

{{ load_data }}

```python

codes = dict(
    DVT = dict(
        exact = ["I81", "O223", "O082", "O871"], # (1)
        regex = ["I82[02389]", "I80[12]"]
    )
)

from eds_scikit.event.icd10 import conditions_from_icd10

DVTs = conditions_from_icd10(
    condition_occurrence=data.condition_occurrence,
    visit_occurrence=data.visit_occurrence,
    codes=codes,
    date_from_visit=True,
    additional_filtering=dict(
        condition_status_source_value={"DP", "DAS"}, # (1)
    )
)
```

1. Here you can provide either `exact`, `regex` or `prefix` codes
2. With this syntax we will keep only DP (*Diagnostic Principal*) or DAS (*Diagnostic Associé*) diagnoses

Of course, you are encouraged to check the documentation of those functions as they provide additional parameters that might be useful depending on your needs.
