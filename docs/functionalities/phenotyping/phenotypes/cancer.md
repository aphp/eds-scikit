{% set csv_path = "eds_scikit/phenotype/cancer/codes.csv" %}

# Cancer

## Presentation

We provide the [CancerFromICD10][eds_scikit.phenotype.cancer.cancer.CancerFromICD10] class to extract visits or patients with cancer related ICD10 code

??? note "Available cancer types"
    {{ values_from_csv(csv_path, col="Cancer type", indent="\t") }}

!!! algos "How it works"
    The algorithm works by looking for either DP ou DR ICD10 codes associated with cancer.
    The codes terminology comes from this article[@kempf2022impact] and is available under `CancerFromICD10.ICD10_CODES`

## Usage

By default, all cancer types mentionned above are extracted

{{ load_data }}

```python
from eds_scikit.phenotype import CancerFromICD10

cancer = CancerFromICD10(data)
data = cancer.to_data()
```

To choose a subset of cancer types, use the `cancer_types` argument:

```python
cancer = CancerFromICD10(
    data,
    cancer_types=[
        "Eye",
        "Liver",
        "Leukemia",
    ],
)
```

The final phenotype DataFrame is then available at `data.computed["CancerFromICD10"]`

### Optional parameters

::: eds_scikit.phenotype.cancer.cancer.CancerFromICD10.__init__
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

## Citation

You can get the BibTex of the corresponding article[@kempf2022impact] by calling

```python
cancer.cite()
```

```bibtex
--8<-- "eds_scikit/phenotype/cancer/citation.bib"
```

## Reference

Check the code reference [here][eds_scikit.phenotype.cancer.cancer.CancerFromICD10] for a more detailled look.

\bibliography
