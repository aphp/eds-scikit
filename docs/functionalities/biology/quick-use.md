# Quick use

This tutorial demonstrates how the biology module can be quickly used to map measurement codes.

!!! tip "Big volume"
    Measurement table can be large. Do not forget to set proper spark config before loading data.

## Mapping measurement table to ANABIO codes

### Defining Concept-Set

To define a concept-set variable you just need to specify a terminology and a set of codes.

```python

from eds_scikit.biology import prepare_measurement_table, ConceptsSet

custom_leukocytes = ConceptsSet("Custom_Leukocytes")

custom_leukocytes.add_concept_codes(concept_codes=['A0174', 'H6740'], 
                                    terminology='GLIMS_ANABIO') # (1)

custom_leukocytes.add_concept_codes(concept_codes=['6690-2'],
                                    terminology='ITM_LOINC') # (2)

```

1. Codes must be given with terminology. See. [measurement_config](/reference/io/settings/) for details on terminologies relationship.
2. Codes must be given with terminology. See. [measurement_config](/reference/io/settings/) for details on terminologies relationship.

### Preparing measurement table

Then, simply run ```prepare_measurement_table``` to select the measurements from your concept set.

```python

measurement = prepare_measurement_table(data,
                                        start_date="2022-01-01", end_date="2022-05-01",
                                        concept_sets=[custom_leukocytes],
                                        convert_units=False,
                                        get_all_terminologies=True)

```
