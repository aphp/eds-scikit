# Exploring concept codes relationship

Manipulating different code terminologies through OMOP ```concept``` and ```concept_relationship``` tables can be tricky.  This becomes even more pronounced when working with biological measurements that may encompass multiple terminologies, including laboratory, unified, and international terminologies.

Use ```prepare_biology_relationship_table``` to preprocess OMOP ```concept``` and ```concept_relationship``` into a single table and get a better insight on how terminologies are related.

!!! tip "Relationship config"
    Terminologies mapping from AP-HP database are used by default. See ```io.settings.measurement_config``` for mapping details or to modify it.

```python

from eds_scikit.biology import prepare_biology_relationship_table

biology_relationship_table = prepare_biology_relationship_table(data)
biology_relationship_table = biology_relationship_table.to_pandas()
biology_relationship_table.head()
```

|   source_concept_id | source_concept_name   | source_concept_code   |   standard_concept_id     | standard_concept_name     | standard_concept_code       |
|--------------------:|:---------------------:|:---------------------:|:-------------------------:|:-------------------------:|:---------------------------:|
|                   3 | xxxxxxxxxxxx          | CX1                   |                         4 | xxxxxxxxxxxx              | A1                          |
|                   9 | xxxxxxxxxxxx          | ZY2                   |                         5 | xxxxxxxxxxxx              | A2                          |
|                   9 | xxxxxxxxxxxx          | B3F                   |                        47 | xxxxxxxxxxxx              | D3                          |
|                   7 | xxxxxxxxxxxx          | T32                   |                         4 | xxxxxxxxxxxx              | F82                         |
|                   5 | xxxxxxxxxxxx          | S23                   |                         1 | xxxxxxxxxxxx              | A432                        |
