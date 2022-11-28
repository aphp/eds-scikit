import pandas as pd
from numpy import NaN

from eds_scikit.datasets import load_hierarchy
from eds_scikit.utils import hierarchy
from eds_scikit.utils.test_utils import assert_equal_no_order, make_df

ds = load_hierarchy()


def test_build_hierarchy():
    expected_result = make_df(
        """
    id, category, lit, chambre, batiment
    batiment1, batiment, None, None, batiment1
    chambre1, chambre, None, chambre1, batiment1
    chambre2, chambre, None, chambre2, batiment1
    lit1, lit, lit1, chambre1, batiment1
    lit2, lit, lit2, chambre1, batiment1
    lit3, lit, lit3, chambre2, batiment1
    """
    ).replace("None", NaN)
    result = hierarchy.build_hierarchy(ds.categories, ds.relationships)
    pd.testing.assert_frame_equal(result, expected_result)


def test_follow_relationships():
    expected_result = make_df(
        """
    child, parent
    chambre1, batiment1
    chambre2, batiment1
    lit1, chambre1
    lit2, chambre1
    lit3, chambre2
    lit1, batiment1
    lit2, batiment1
    lit3, batiment1
    """
    )
    result = hierarchy._follow_relationships(ds.relationships)
    assert_equal_no_order(result, expected_result)


def test_follow_relationships_self_reference():
    # making sure that the self-reference "batiment1, batiment1"
    # does not create a RecursionError
    relationships = make_df(
        """
    child, parent
    batiment1, batiment1
    chambre1, batiment1
    """
    )
    expected_result = make_df(
        """
    child, parent
    chambre1, batiment1
    """
    )
    result = hierarchy._follow_relationships(relationships)
    pd.testing.assert_frame_equal(result, expected_result)


def test_follow_relationships_loops():
    # warning: these relationships create a loop
    # we test that this does not create a RecursionError
    relationships = make_df(
        """
    child, parent
    chambre1, chambre2
    chambre2, chambre3
    chambre3, chambre1
    """
    )
    expected_result = make_df(
        """
    child, parent
    chambre1, chambre2
    chambre1, chambre3
    chambre2, chambre1
    chambre2, chambre3
    chambre3, chambre1
    chambre3, chambre2
    """
    )
    result = hierarchy._follow_relationships(relationships)
    assert_equal_no_order(result, expected_result)
