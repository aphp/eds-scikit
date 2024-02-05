import pytest

from eds_scikit.biology import ConceptsSet, bioclean
from eds_scikit.biology.utils.process_concepts import fetch_all_concepts_set
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
        start_date=data.t_start,
        end_date=data.t_end,
    )
