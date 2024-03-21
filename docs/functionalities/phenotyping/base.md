{% set csv_path = "eds_scikit/phenotype/cancer/codes.csv" %}

# How to use and developp phenotyping algorithms in `eds-scikit`

## The [`Phenotype`][eds_scikit.phenotype.base.Phenotype] class

Phenotyping is done via the `Phenotype` class.

Using this class, we can add *`features`* that will be stored in the `features` attribute.
Features are DataFrames containing at least a `person_id` and a `phenotype` column. Additionaly:

- If phenotyping at the **visit** level, features contains a `visit_occurrence_id` column
- If using sub-phenotypes (e.g. types of diabetes, or various cancer localiizations), features contains a `subphenotype` column.

We distinguish 2 main ways of adding features to a `Phenotype` instance:

- By querying the database to extract *raw* features
- By aggregating one or multiple existing features

## Available phenotypes

`eds-scikit` is shipped with various phenotyping algorithms. For instance, the [CancerFromICD10][eds_scikit.phenotype.cancer.cancer.CancerFromICD10] class can be used to extract visits or patients with a cancer-related ICD10 code. All those phenotyping algorithms share the same API. We will demonstrate it using the `CancerFromICD10` class

{{ load_data }}

```python
from eds_scikit.phenotype import CancerFromICD10

cancer = CancerFromICD10(data)
```

To run the phenotyping algorithm, simply run:

```python
data = cancer.to_data()
```

This will put the resulting phenotype DataFrame in `data.computed["CancerFromICD10"]`

Most available phenotypes share the same parameters:

::: eds_scikit.phenotype.cancer.cancer.CancerFromICD10.__init__
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

Please look into each algorithm's documentation for further specific details.

## Implement your own phenotyping algorithm

TO help you implement your own phenotyping algorithm, the `Phenotype` class exposes method to

- Easily featch features based on ICD10 and CCAM codes
- Easily aggregate feature(s) using simple threshold rules


The following paragraph will show how to implement a dummy phenotyping algorithm for moderate to terminal Chronic Kidney Disease (CKD). In short, it will:
- Extract patients with ICD10 code for CKD
- Extract patients with CCAM code for dialysis or kidney transplant
- Aggregate those two feature by keeping patients with both features

We will start by creating an instance of the `Phenotype` class:

```python
from eds_scikit.phenotype import Phenotype

ckd = Phenotype(data, name="DummyCKD")
```

Next we define the ICD10 and CCAM codes

!!! tip "Codes formatting"
    Under the hood, `Phenotype` will use the [conditions_from_icd10][eds_scikit.event.icd10.conditions_from_icd10] and [procedures_from_ccam][eds_scikit.event.procedures_from_ccam] functions. Check their documentation for details on how to format the provided codes

```python
icd10_codes = {
    "CKD": {"regex": ["N18[345]"]},
}

ccam_codes = {
    "dialysis": {"regex": ["JVJB001"]},
    "transplant": {"exact": ["JAEA003"]},
}
```

Finally, we can start designing the phenotyping algorithm:

#### Get ICD10 features
```
ckd = ckd.add_code_feature(
    output_feature="icd10",
    source="icd10",
    codes=icd10_codes,
)
```
#### Get CCAM features
```
ckd = ckd.add_code_feature(
    output_feature="ccam",
    source="ccam",
    codes=ccam_codes,
)
```
#### Aggregate those 2 features
```
ckd = ckd.agg_two_features(
    input_feature_1="icd10",
    input_feature_2="ccam",
    output_feature="CKD",
    how="AND",
    level="patient",
    subphenotype=False,
    thresholds=(1, 1),
)
```


The final phenotype DataFrame can now be added to the `data` object:

```python
data = ckd.to_data()
```

It will be available under `data.computed.CKD`


### Available methods on `Phenotype`:

::: eds_scikit.phenotype.base.Phenotype
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

### Citation

Most available phenotypes implement an algorithm described in an academic paper. When using this algorithm, you can get the BibTex citation of the corrresponding paper by calling the `cite` method. For instance:

```python
cancer.cite()
```

```bibtex
--8<-- "eds_scikit/phenotype/cancer/citation.bib"
```

\bibliography
