# Quick use

This tutorial demonstrates how the biology module can be quickly used to map measurement codes and generate comprehensive statistical summaries.

!!! tip "Big volume"
    Measurement table can be large. Do not forget to set proper spark config before loading data.

## Mapping measurement table to ANABIO codes

### Defining Concept-Set

```python

from eds_scikit.biology import prepare_measurement_table, ConceptsSet

custom_leukocytes = ConceptsSet("Custom_Leukocytes")

custom_leukocytes.add_concept_codes(concept_codes=['xxxxx', 'xxxxx', 'xxxxx'], 
                                    terminology='GLIMS_ANABIO')

custom_leukocytes.add_concept_codes(concept_codes=['6690-2'], 
                                    terminology='ITM_LOINC')

```

### Preparing measurement table

```python

measurement = prepare_measurement_table(data,
                                        start_date="2022-01-01", end_date="2022-05-01",
                                        concept_sets=[custom_leukocytes],
                                        convert_units=False,
                                        get_all_terminologies=True)

```

