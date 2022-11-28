from eds_scikit.structures import attributes
from eds_scikit.utils.test_utils import make_df


def test_parent_UF_attributes_simple_data():
    care_site = make_df(
        """
        care_site_id, care_site_name, care_site_type_source_value, expected_result
        batiment1, batiment un, batiment, False
        secteur1, secteur un urgence, Unité Fonctionnelle (UF), True
        secteur2, secteur deux chirurgie, Unité Fonctionnelle (UF), False
        unité1, unité un, unité, True
        unité2, unité deux, unité, False
        unité3, unité trois, unité, False
        """
    )

    result = attributes.get_parent_attributes(
        care_site,
        version="test",
        only_attributes=["IS_EMERGENCY"],
        parent_type="Unité Fonctionnelle (UF)",
    )

    assert (care_site["care_site_id"] == result["care_site_id"]).all()
    care_site["result"] = result["IS_EMERGENCY"]
    assert (care_site["result"] == care_site["expected_result"]).all()
