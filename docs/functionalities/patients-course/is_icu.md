EDS-Scikit provides a function to tag care sites as being **Intensive Care Units**.  It also provides a higher-level function to directly tag visits.

{{ load_data }}

### Tagging care sites

Tagging is done using the `tag_icu_care_site` function:

```python
from eds_scikit.icu import tag_icu_care_site
```

::: eds_scikit.icu.tag_icu_care_site
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

Simply call the function by providing the necessary data (see below) and by picking the *algo*

```python
care_site = tag_icu_care_site(
    care_site=data.care_site,
    algo="from_authorisation_type",
)
```

!!! algos "Availables algorithms (values for `"algo"`)"

	=== "'from_authorisation_type'"

        ::: eds_scikit.icu.icu_care_site.from_authorisation_type
	=== "'from_regex_on_care_site_description'"

        ::: eds_scikit.icu.icu_care_site.from_regex_on_care_site_description

### Tagging visits

Tagging is done using the `tag_icu_visit` function:

```python
from eds_scikit.icu import tag_icu_visit
```

::: eds_scikit.icu.tag_icu_visit
    options:
         docstring_section_style: spacy
         show_signature_annotations: true
         show_signature: true
         heading_level: 3
         members_order: source
         show_source: false
         separate_signature: true

Simply call the function by providing the necessary data (see below) and by picking the *algo*

```python
visit_detail = tag_icu_visit(
    visit_detail=data.visit_detail,
    algo="from_mapping",
)
```

!!! algos "Availables algorithms (values for `"algo"`)"

	Those are the same as `tag_icu_care_site`
