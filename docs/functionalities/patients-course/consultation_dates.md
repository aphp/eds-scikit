When a patient comes multiple times for consultations, it is often represented as a single ``visit_occurrence`` in the CDW. If a clear history of a patient's course is needed, it is then necessary to use proxies in order to access this information. An available proxy to get those consultation dates is to check for the existence of consultation reports and use the associated reports dates.

To this extend, two methods are available. They can be combined or used separately:

- Use the `note_datetime` field associated to each consultation report
- Extract the consultation report date by using NLP

!!! aphp "An important remark"

     Be careful when using the `note_datetime` field as it can represent the date of **modification** of a document (i.e. it can be modified if the clinician adds some information in it in the future).


{{ load_data }}

```python
from eds_scikit.event import get_consultation_dates

get_consultation_dates(
    data.visit_occurrence,
    note=data.note,
    note_nlp=note_nlp,
    algo=["nlp"],
)
```

The snippet above required us to generate a `note_nlp` with a `consultation_date` column (see below for more informations).

!!! edsnlp "Consultation pipe"
     A [consultation date](https://aphp.github.io/edsnlp/latest/pipelines/misc/consultation-dates/) pipeline exists and is particulary suited for this task.
     Moreover, [methods are available](https://aphp.github.io/edsnlp/latest/tutorials/multiple-texts/) to run an EDS-NLP pipeline on a Pandas, Spark or even Koalas DataFrame !

We can check the various exposed parameters if needed:

::: eds_scikit.event.consultations.get_consultation_dates
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

!!! algos "Availables algorithms (values for `"algo"`)"

    === "'nlp'"

        ::: eds_scikit.event.consultations.get_consultation_dates_nlp

	=== "'structured'"

        ::: eds_scikit.event.consultations.get_consultation_dates_structured
