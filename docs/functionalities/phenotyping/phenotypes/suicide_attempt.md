# Suicide Attempt

## Presentation

We provide the [SuicideAttemptFromICD10][eds_scikit.phenotype.suicide_attempt.suicide_attempt.SuicideAttemptFromICD10] class to extract visits linked to suicide attempt from ICD-10 codes.

## Usage

As mentionned below, two algorithms (`"Haguenoer2008"` (default) and `"X60-X84"`) are available

{{ load_data }}

```python

from eds_scikit.phenotype import SuicideAttemptFromICD10

sa = SuicideAttemptFromICD10(data)
data = sa.to_data()

```

The final phenotype DataFrame is then available at `data.computed["SuicideAttemptFromICD10_Haguenoer2008"]` or `data.computed["SuicideAttemptFromICD10_X60_X84"]` depending on the used algorithm

!!! algos "Availables algorithms (values for `"algo"`)"
    The ICD10 codes are available under `SuicideAttemptFromICD10.ICD10_CODES`

	=== "'X60-X84'"

        Returns the visits that have at least one ICD code that belongs to the range X60 to X84.
    === "'Haguenoer2008'"

        Returns the visits that follow the definiton of Haguenoer2008[@haguenoer_tentatives_2008]. This rule requires at least one Main Diagnostic (DP) belonging to S00 to T98, and at least one Associated Diagnostic (DAS) that belongs to the range X60 to X84.

## Citation

When using `algo="Haguenoer2008"`, you can get the BibTex of the corresponding article[@haguenoer_tentatives_2008] by calling

```python
sa.cite()
```

```bibtex
--8<-- "eds_scikit/phenotype/suicide_attempt/Haguenoer2008.bib"
```

## Reference

Check the code reference [here][eds_scikit.phenotype.suicide_attempt.suicide_attempt.SuicideAttemptFromICD10] for a more detailled look.

\bibliography
