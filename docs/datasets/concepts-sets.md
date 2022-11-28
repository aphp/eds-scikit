{% set csv_path = "eds_scikit/datasets/default_concepts_sets.csv" %}

# Concepts-sets

A concepts-set is a generic concept that has been deemed appropriate for most biological analyses. It is a group of several biological concepts representing the same biological entity.

!!! aphp "Concepts-sets"

    This dataset is listing common biological entities in AP-HP's Data Warehouse.

Below, one can see the list of **default concepts-set** provided by the library.

## Preview

{{ preview_csv(csv_path) }}

## Link

You can see the dataset [here]({{ link_repo_file(csv_path) }})

!!!note
    The concept codes are expressed in the **AnaBio** and **LOINC** standard vocabularies (for more information about the vocabularies see the [Vocabulary][vocabulary] page).
