# Suicide attempt

## Presentation

We provide the [`tag_suicide_attempt()`][eds_scikit.event.tag_suicide_attempt] function to extract suicide attempt from ICD-10 codes.

## The `tag_suicide_attempt()` function

{{ load_data }}

```python

from eds_scikit.event import tag_suicide_attempt

visit_occurrence = tag_suicide_attempt(
    data.visit_occurrence,
    data.condition_occurrence,
    algo = "X60-X84",
)

```

!!! algos "Availables algorithms (values for `"algo"`)"

	=== "'X60-X84'"

        Returns the visits that have at least one ICD code that belongs to the range X60 to X84.
    === "'Haguenoer2008'"

        Returns the visits that follow the definiton of "Haguenoer, Ken, Agnès Caille, Marc Fillatre, Anne Isabelle Lecuyer, et Emmanuel Rusch. « Tentatives de Suicide », 2008, 4.". This rule requires at least one Main Diagnostic (DP) belonging to S00 to T98, and at least one Associated Diagnostic (DAS) that belongs to the range X60 to X84.

You can check the documentation of the function for additional parameters:

::: eds_scikit.event.tag_suicide_attempt
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true
