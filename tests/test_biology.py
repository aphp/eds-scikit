import numpy as np
import pytest

from eds_scikit.biology import (
    ConceptsSet,
    bioclean,
    measurement_values_summary,
    plot_biology_summary,
    prepare_measurement_table,
)
from eds_scikit.biology.utils.prepare_relationship import (
    prepare_biology_relationship_table,
)
from eds_scikit.biology.utils.process_concepts import fetch_all_concepts_set
from eds_scikit.biology.utils.process_units import Units
from eds_scikit.datasets import load_biology_data


@pytest.fixture(scope="session")
def tmp_biology_dir(tmp_path_factory):
    template_dir = tmp_path_factory.mktemp("Biology_summary")
    return template_dir


@pytest.fixture
def data():
    return load_biology_data(seed=42)


@pytest.fixture
def concepts_sets(data):

    concept = data.concept
    concepts_sets = []
    nb_entity = (
        concept[concept.vocabulary_id == "GLIMS_LOINC"]
        .concept_id.str.split("-")
        .str[0]
        .str[:-1]
        .nunique()
    )
    for i in range(nb_entity):
        concept_codes = concept[(concept.concept_code.str.startswith("A" + str(i)))]
        if len(str(i)) == 1:
            concept_codes = concept_codes[concept_codes.concept_code.str.endswith("9")]
        else:
            concept_codes = concept_codes[~concept_codes.concept_code.str.endswith("9")]
        concept_codes = concept_codes.concept_code.to_list()

        concept_set = ConceptsSet(name="Entity_" + str(i))
        concept_set.add_concept_codes(concept_codes, terminology="GLIMS_ANABIO")

        concepts_sets.append(concept_set)
        concept_set = concepts_sets[0]
        concept_set.add_concept_codes("XXXX", terminology="X")
        concept_set.add_concept_codes(["XXXX", "YYYYY"], terminology="X")

    concept_set.remove_concept_codes("XXXX", terminology="X")
    concept_set.remove_concept_codes(["XXXX", "YYYYY"], terminology="X")
    fetch_all_concepts_set()

    assert set(concept_set.concept_codes) == set(concepts_sets[0].concept_codes)

    relationship_table = prepare_biology_relationship_table(
        data, [concept_set], get_all_terminologies=True
    )
    concept_set.get_concept_codes_table(relationship_table=relationship_table)

    concept_set.add_target_unit("g")
    concept_set.add_conversion("g", "mol", 180)

    return concepts_sets


@pytest.mark.parametrize("standard_terminologies", [["ANABIO", "LOINC"], ["ANABIO"]])
def test_bioclean(data, concepts_sets, standard_terminologies, tmp_biology_dir):

    bioclean(
        data=data,
        concepts_sets=concepts_sets,
        studied_cohort=[0, 1, 2, 3, 4],
        convert_units=True,
        start_date=data.t_start,
        end_date=data.t_end,
    )

    bioclean(
        data=data,
        concepts_sets=None,
        studied_cohort=[0, 1, 2, 3, 4],
        convert_units=True,
        start_date=data.t_start,
        end_date=data.t_end,
    )


def test_units(data):
    units = Units()

    units.add_target_unit("g")

    assert units.can_be_converted("g", "mg")
    assert not units.can_be_converted("g", "l")

    assert units.get_category("m/h/xxxx") == ["m", "Time", "Unkown"]
    assert units.to_base("mm") == 0.001
    assert np.isnan(units.to_base("xxxx"))

    assert abs(units.convert_unit("L", "ml") - 1000) < 1e-6
    assert abs(units.convert_unit("m/s", "m/h") - 3600.0) < 1e-6
    assert np.isnan(units.convert_unit("m/s/xxxx", "m/h/s"))
    units.add_conversion("mol", "g", 10)
    assert abs(units.convert_unit("g", "mol") - 0.1) < 1e-6


@pytest.fixture
def measurement(data, concepts_sets):

    data.convert_to_koalas()

    measurement = prepare_measurement_table(
        data=data,
        concept_sets=concepts_sets,
        convert_units=False,
        start_date=data.t_start,
        end_date=data.t_end,
    )

    measurement = prepare_measurement_table(
        data=data,
        concept_sets=concepts_sets,
        convert_units=True,
        start_date=data.t_start,
        end_date=data.t_end,
        get_all_terminologies=False,
    )

    visit_occurrence = data.visit_occurrence[
        ["visit_occurrence_id", "care_site_id"]
    ].merge(data.care_site[["care_site_id", "care_site_short_name"]], on="care_site_id")
    measurement = measurement.merge(
        visit_occurrence[["visit_occurrence_id", "care_site_short_name"]],
        on="visit_occurrence_id",
    )

    plot_biology_summary(
        measurement,
        value_column="value_as_number",
        unit_column="unit_source_value",
        terminologies=["GLIMS_ANABIO"],
    )

    measurement_values_summary(
        measurement, ["concept_set"], "value_as_number", "unit_source_value"
    )

    return measurement


def test_concept_set_error(data, concepts_sets, measurement):

    concept_set = concepts_sets[0]

    try:
        concept_set.add_concept_codes(55)
    except TypeError:
        pass
    try:
        concept_set.add_concept_codes(55, terminology="GLIMS_ANABIO")
    except TypeError:
        pass
    try:
        ConceptsSet(name="Entity_xxx").add_concept_codes(
            [55], terminology="GLIMS_ANABIO"
        )
    except TypeError:
        pass
    try:
        concept_set.remove_concept_codes(["55"], terminology="xxxxx")
    except TypeError:
        pass
    try:
        concept_set.remove_concept_codes(55, terminology="GLIMS_ANABIO")
    except TypeError:
        pass

    try:
        prepare_biology_relationship_table(data, None, get_all_terminologies=False)
    except Exception:
        pass
    try:
        plot_biology_summary(measurement, value_column=None)
    except ValueError:
        pass
    try:
        plot_biology_summary(measurement, unit_column=None)
    except ValueError:
        pass
