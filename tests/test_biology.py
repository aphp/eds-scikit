import pytest

from eds_scikit.biology import ConceptsSet, bioclean, prepare_measurement_table, plot_biology_summary
from eds_scikit.biology.utils.prepare_relationship import prepare_biology_relationship_table
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
def test_units(data):
    units = Units()
    
    units.add_target_unit("g")
    assert units.can_be_converted("g", "mg")
    assert not units.can_be_converted("g", "l")

    
    assert units.convert_unit("L", "ml") == 1000
    assert units.convert_unit("m/s", "m/h") == 3600.
    
    units.add_conversion("mol", "g", 10)
    assert units.convert_unit("g", "mol") == 0.1


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
    try:
        concept_set.add_concept_codes(55)
    except TypeError:
        pass
    concept_set.remove_concept_codes("XXXX", terminology="X")
    concept_set.remove_concept_codes(["XXXX", "YYYYY"], terminology="X")
    try:
        concept_set.remove_concept_codes(55)
    except TypeError:
        pass
    fetch_all_concepts_set()

    assert set(concept_set.concept_codes) == set(concepts_sets[0].concept_codes)

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
        
    concept_set.get_concept_codes_table()
    relationship_table = prepare_biology_relationship_table(data, [concept_set], True)
    concept_set.get_concept_codes_table(relationship_table=relationship_table)
    concept_set.add_target_unit("g")
    concept_set.add_conversion("g", "mol", 10)
        
    try:
        concept_set.add_concept_codes(55)
    except TypeError:
        pass
    concept_set.remove_concept_codes("XXXX", terminology="X")
    concept_set.remove_concept_codes(["XXXX", "YYYYY"], terminology="X")
    try:
        concept_set.remove_concept_codes(55)
    except TypeError:
        pass
    fetch_all_concepts_set()

    assert set(concept_set.concept_codes) == set(concepts_sets[0].concept_codes)
    
    
@pytest.mark.parametrize("standard_terminologies", [["AnaBio", "LOINC"], ["AnaBio"]])
def test_bioclean(data, concepts_sets, standard_terminologies, tmp_biology_dir):

    bioclean(
        data=data,
        concepts_sets=concepts_sets,
        studied_cohort=[0, 1, 2, 3, 4],
        convert_units=True,
        start_date=data.t_start,
        end_date=data.t_end,
    )
    
@pytest.fixture
def test_prepare_measurement(data, concepts_sets, standard_terminologies, tmp_biology_dir):
    
    measurement = prepare_measurement_table(data=data,
                                            concepts_sets=concepts_sets,
                                            convert_units=False,
                                            start_date=data.t_start,
                                            end_date=data.t_end,
                                           )
    try:
        plot_biology_summary(measurement)
    except ValueError:
        pass
     
    plot_biology_summary(measurement, "value_as_number", terminologies=["AnaBio"])
    