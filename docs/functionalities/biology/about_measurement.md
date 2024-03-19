## About measurements table

The *BioClean* module focuses on three **OMOP** terms:

- [Measurement](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:measurement) is a record obtained through the standardized testing or examination of a person or person's sample.
- [Concept](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept) is a semantic notion that uniquely identify a clinical event. It can group several measurements.
- [Concept Relationship](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:concept_relationship) is a semantic relation between terminologies, allowing to map codes from different terminologies.


A fourht term was created to ease the use of the two above:

- [concepts-set](../../datasets/concepts-sets.md) is a generic concept that has been deemed appropriate for most biological analyses. It is a group of several biological concepts representing the same biological entity.

**Example:** <br/>
Let's imagine the laboratory X tests the creatinine of Mister A and Mister B in mg/dL and the laboratory Y tests the creatinine of Mister C in µmol/L. In this context, the dataset will contain:

- 3 measurements (one for each conducted test)
- 2 concepts (one concept for the creatinine tested in mg/dL and another one for the creatinine tested in µmol/L)
- 1 concepts-set (it groups the 2 concepts because they are the same biological entity)


## Vocabulary

A vocabulary is a terminology system that associates a code to a specific clinical event. One may distinguish two types of vocabularies:

### Source vocabulary

The source vocabulary is the vocabulary used in the LIMS (Laboratory Information Management System) software. It is specific to the LIMS and may be different in each laboratory.

### Standard vocabulary

The standard vocabulary is a unified vocabulary that allows data analysis on a larger scale.

- It is classified in chapter.
- It has a bigger granularity than the source vocabulary, multiple source codes may be associated to one standard code.

### Vocabulary flowchart in OMOP

![Image title](../../_static/biology/vocabulary_flowchart.svg)
