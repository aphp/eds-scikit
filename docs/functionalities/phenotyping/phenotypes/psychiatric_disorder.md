{% set csv_path = "eds_scikit/phenotype/psychiatric_disorder/codes.csv" %}

# Psychiatric disorder

## Presentation

We provide the [PsychiatricDisorderFromICD10][eds_scikit.phenotype.psychiatric_disorder.psychiatric_disorder.PsychiatricDisorderFromICD10] class to extract visits or patients with ICD10 codes related to psychiatric disorders

??? algos "Available disorders"
    {{ values_from_csv(csv_path, col="disorder_group", indent="\t") }}

## Usage

By default, all cancer types mentionned above are extracted

{{ load_data }}

```python

from eds_scikit.phenotype import PsychiatricDisorderFromICD10

psy = PsychiatricDisorderFromICD10(data)
data = psy.to_data()

```

To choose a subset of disorders, use the `disorder_types` argument:

```python
psy = PsychiatricDisorderFromICD10(
    data,
    disorder_types = [
        "Anxiety Disorders",
        "Trauma and Stressor-Related Disorders",
    ],
)
```

The final phenotype DataFrame is then available at `data.computed["PsychiatricDisorderFromICD10"]`

### Optional parameters

::: eds_scikit.phenotype.psychiatric_disorder.psychiatric_disorder.PsychiatricDisorderFromICD10.__init__
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

## Citation

You can get the BibTex of the corresponding article[@2022_covid_4CE] by calling

```python
cancer.cite()
```

```bibtex
--8<-- "eds_scikit/phenotype/psychiatric_disorder/citation.bib"
```

## Reference

Check the code reference [here][eds_scikit.phenotype.psychiatric_disorder.psychiatric_disorder.PsychiatricDisorderFromICD10] for a more detailled look.

\bibliography
