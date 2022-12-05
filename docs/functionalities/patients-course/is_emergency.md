eds-scikit provides a function to tag care sites as being **medical emergency units**.  It also provides a higher-level function to directly tag visits.

{{ load_data }}

### Tagging care sites

Tagging is done using the `tag_emergency_care_site` function:

```python
from eds_scikit.emergency import tag_emergency_care_site
```

::: eds_scikit.emergency.tag_emergency_care_site
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
care_site = tag_emergency_care_site(
    care_site=data.care_site,
    algo="from_mapping",
)
```

!!! algos "Availables algorithms (values for `"algo"`)"

	=== "'from_mapping'"

        ::: eds_scikit.emergency.emergency_care_site.from_mapping
    === "'from_regex_on_parent_UF'"

        ::: eds_scikit.emergency.emergency_care_site.from_regex_on_parent_UF
	=== "'from_regex_on_care_site_description'"

        ::: eds_scikit.emergency.emergency_care_site.from_regex_on_care_site_description

### Tagging visits

Tagging is done using the `tag_emergency_visit` function:

```python
from eds_scikit.emergency import tag_emergency_visit
```

::: eds_scikit.emergency.tag_emergency_visit
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
visit_detail = tag_emergency_visit(
    visit_detail=data.visit_detail,
    algo="from_mapping",
)
```

!!! algos "Availables algorithms (values for `"algo"`)"

	=== "'from_mapping'"

        ::: eds_scikit.emergency.emergency_care_site.from_mapping
    === "'from_regex_on_parent_UF'"

        ::: eds_scikit.emergency.emergency_care_site.from_regex_on_parent_UF
	=== "'from_regex_on_care_site_description'"

        ::: eds_scikit.emergency.emergency_care_site.from_regex_on_care_site_description
	=== "'from_vo_visit_source_value'"

        ::: eds_scikit.emergency.emergency_visit.from_vo_visit_source_value
