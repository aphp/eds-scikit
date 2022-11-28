from typing import Any, Dict, Optional

import pandas as pd
from numpy import NaN


def build_hierarchy(
    categories: pd.DataFrame,
    relationships: pd.DataFrame,
) -> pd.DataFrame:
    """Build a dataframe with parent categories as columns"""
    assert set(categories.columns) == {"id", "category"}
    assert set(relationships.columns) == {"child", "parent"}
    assert not categories["id"].duplicated().any()
    assert not relationships.duplicated().any()

    expanded_relationships = _follow_relationships(relationships)

    expanded_relationships = expanded_relationships.loc[
        expanded_relationships["child"].isin(categories["id"])
    ]

    relationships_with_category = _deduplicate_parent_category(
        expanded_relationships, categories
    )

    categories = _finalize_parent_categories(categories, relationships_with_category)

    return categories


def _finalize_parent_categories(
    categories: pd.DataFrame,
    relationships_with_category: pd.DataFrame,
) -> pd.DataFrame:
    all_categories = categories["category"].value_counts().index.tolist()

    # We pivot the "parent_category" to columns, making sure to keep all original categories
    parent_categories = relationships_with_category.pivot(
        index="child", columns="parent_category", values="parent"
    ).reset_index()
    for category in all_categories:
        if category not in parent_categories.columns:
            parent_categories[category] = NaN

    # We can now add this info to the original dataset.
    new_columns = categories.columns.tolist() + all_categories
    categories = categories.merge(
        parent_categories, how="left", left_on="id", right_on="child"
    ).loc[:, new_columns]

    for category in all_categories:
        selected = categories["category"] == category
        # ex: for a care site of category "Batiment", the column "Batiment"
        # should contain this care_site_id
        categories.loc[selected, category] = categories.loc[selected, "id"]

    return categories


def _deduplicate_parent_category(
    relationships: pd.DataFrame,
    categories: pd.DataFrame,
) -> pd.DataFrame:
    # now we want a dataset where each row is (child, parent, parent_category)
    # In case a child has multiple parents of a given category, we select the
    # "biggest", i.e. the one with the most children.
    n_children = relationships.groupby("parent").size().rename("n_children")
    relationships = (
        relationships.merge(n_children, on="parent")
        .merge(categories, how="left", left_on="parent", right_on="id")
        .rename(columns={"category": "parent_category"})
        .dropna()
    )
    relationships = relationships.sort_values(
        by=["child", "parent_category", "n_children"], ascending=False
    ).drop_duplicates(subset=["child", "parent_category"], keep="first")

    return relationships.loc[:, ["child", "parent", "parent_category"]]


def _follow_relationships(relationships: pd.DataFrame) -> pd.DataFrame:
    """Expand relationships dataframe with grandparents (etc.) as new rows.

    Returns
    -------
    relationships: pd.DataFrame
        same as input dataframe (columns 'child' and 'parent')
        but with additionnal rows containing "grandparent" relationships

    """
    # handle everything in dicts
    relationships = (
        relationships.drop_duplicates()
        .groupby("child")["parent"]
        .apply(lambda s: set(s))
        .to_dict()
    )
    known_parents = dict()
    for child_id in relationships.keys():
        known_parents[child_id] = _get_all_parents_for_child(
            child_id, relationships, known_parents
        )

    # go back to dataframe world
    all_parents = pd.DataFrame(
        [
            (child, parent)
            for child, parents in known_parents.items()
            for parent in parents
        ],
        columns=["child", "parent"],
    )

    return all_parents


def _get_all_parents_for_child(
    child_id: str,
    relationships: pd.DataFrame,
    known_parents: Dict[str, Any],
    allready_visited: Optional[set] = None,
) -> set:
    if allready_visited is None:
        allready_visited = set()

    try:
        return known_parents[child_id]
    except KeyError:
        try:
            first_parents = relationships[child_id]
        except KeyError:
            return set()

        # avoiding loops and self-reference
        allready_visited = allready_visited.union({child_id})
        parents_to_visit = first_parents - allready_visited

        # follow parents to know grandparents
        all_parents = first_parents.union(
            *[
                _get_all_parents_for_child(
                    parent, relationships, known_parents, allready_visited
                )
                for parent in parents_to_visit
            ]
        )
        # avoiding self-reference in output in case of looping
        all_parents = all_parents - {child_id}
        if parents_to_visit == first_parents:
            # We store the result for this child_id only if we fully followed its parents
            # This is usefull in case of looping. This line should never be skipped
            # if the input relationships do not contain loops.
            known_parents[child_id] = all_parents
        return all_parents
