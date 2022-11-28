import pytest

from eds_scikit.biology import ConceptsSet, bioclean, plot_biology_summary
from eds_scikit.biology.utils.config import create_config_from_stats
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
        concept[concept.vocabulary_id == "LOINC"]
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
        concepts_sets.append(
            ConceptsSet(name="Entity_" + str(i), concept_codes=concept_codes)
        )
    concept_set = concepts_sets[0]
    concept_set.add_concept_codes("XXXX")
    concept_set.add_concept_codes(["XXXX", "YYYYY"])
    try:
        concept_set.add_concept_codes(55)
    except TypeError:
        pass
    concept_set.remove_concept_codes("XXXX")
    concept_set.remove_concept_codes(["XXXX", "YYYYY"])
    try:
        concept_set.remove_concept_codes(55)
    except TypeError:
        pass
    fetch_all_concepts_set()

    assert set(concept_set.concept_codes) == set(concepts_sets[0].concept_codes)
    return concepts_sets


@pytest.mark.parametrize("module", ["pandas", "koalas"])
def test_biology_summary(data, concepts_sets, module, tmp_biology_dir):
    if module == "koalas":
        data.convert_to_koalas()
    elif module == "pandas":
        data.reset_to_pandas()

    plot_biology_summary(
        data=data,
        concepts_sets=concepts_sets,
        start_date=data.t_start,
        end_date=data.t_end,
        number_of_concept=("AnaBio", 2),
        limit_count=("AnaBio", 500),
        stats_only=True,
        save_folder_path=tmp_biology_dir,
    )


def test_create_config(concepts_sets, tmp_biology_dir):
    config_name = "my_custom_config"

    create_config_from_stats(
        concepts_sets=concepts_sets,
        config_name=config_name,
        stats_folder=tmp_biology_dir,
    )


@pytest.mark.parametrize("standard_terminologies", [["AnaBio", "LOINC"], ["AnaBio"]])
def test_bioclean(data, concepts_sets, standard_terminologies, tmp_biology_dir):

    concepts_sets.append(ConceptsSet(name="WRONG_CODE", concept_codes=["XXX", "XYXY"]))
    concepts_sets.append(
        ConceptsSet(name="WRONG_CODE_2", concept_codes=["A1234", "XYXY"])
    )

    bioclean(
        data=data,
        concepts_sets=concepts_sets,
        config_name="my_custom_config",
        studied_cohort=[0, 1, 2, 3, 4],
        clip=True,
        standard_terminologies=standard_terminologies,
        start_date=data.t_start,
        end_date=data.t_end,
    )

    assert hasattr(data, "bioclean")

    plot_biology_summary(
        data=data,
        pd_limit_size=100,
        concepts_sets=concepts_sets,
        start_date=data.t_start,
        end_date=data.t_end,
        save_folder_path=tmp_biology_dir,
    )
