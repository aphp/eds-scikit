import os
from typing import List

from eds_scikit import BASE_DIR
from eds_scikit.utils import framework, hierarchy

DATASET_FOLDER = BASE_DIR / "resources" / "generated"
CARE_SITE_CATEGORIES = [
    "Unité d’hébergement (UH)",
    "Unité de consultation (UC)",
    "Unité Fonctionnelle (UF)",
    "UM (UMA PMSI)",
    "Service/Département",
    "Hôpital",
]


def generate_care_site_hierarchy(
    care_site: framework.DataFrame,
    fact_relationship: framework.DataFrame,
    care_site_categories: List[str],
) -> None:  # pragma: no cover
    """
    Generate the care site hierarchy dataset.

    Parameters
    ----------
    care_site : framework.DataFrame
        The `care_site` DataFrame
    fact_relationship : framework.DataFrame
        The `fact_relationship` DataFrame
    care_site_categories : List[str]
        A list of `care_site_type_source_value` to use as categories
    """

    care_site = _load_care_site_categories(care_site, care_site_categories)
    relationships = _load_care_site_relationships(fact_relationship)

    care_site = _simplify_care_site_categories(care_site, relationships)
    care_site_hierarchy = hierarchy.build_hierarchy(care_site, relationships)
    care_site_hierarchy = _simplify_care_site_hierarchy(care_site_hierarchy)
    _save_care_site_hierarchy(care_site_hierarchy, DATASET_FOLDER)


def _load_care_site_categories(care_site, care_site_categories):  # pragma: no cover
    selected_cs = care_site[["care_site_id", "care_site_type_source_value"]].rename(
        columns=dict(
            care_site_id="id",
            care_site_type_source_value="category",
        )
    )

    selected_cs = framework.to(
        "pandas",
        selected_cs[selected_cs.category.isin(set(care_site_categories))],
    ).drop_duplicates()
    print(
        f"Loaded {len(selected_cs)} care_site with categories: {care_site_categories}"
    )

    return selected_cs


def _load_care_site_relationships(fact_relationship):  # pragma: no cover

    selected_domain = 57  # care site domain
    selected_relationship = 46233688  # care site is part of care site

    selected_fr = fact_relationship[
        ["fact_id_1", "fact_id_2", "domain_concept_id_1", "relationship_concept_id"]
    ].rename(
        columns=dict(
            fact_id_1="child",
            fact_id_2="parent",
        )
    )

    selected_fr = framework.to(
        "pandas",
        selected_fr[
            (selected_fr.domain_concept_id_1 == selected_domain)
            & (selected_fr.relationship_concept_id == selected_relationship)
        ][["child", "parent"]],
    ).drop_duplicates()

    print(
        f"Loaded {len(selected_fr)} relationships for {selected_fr['child'].nunique()} children"
    )
    return selected_fr


def _simplify_care_site_categories(care_site, relationships):  # pragma: no cover
    n_before = len(care_site)
    care_site_with_relation = set(relationships["child"]).union(relationships["parent"])
    care_site = care_site.loc[care_site["id"].isin(care_site_with_relation)]
    print(
        "Keeping only care_site with at least one relationship."
        f" {len(care_site)} rows remain ({len(care_site)/n_before:.1%})"
    )
    return care_site


def _simplify_care_site_hierarchy(care_site_hierarchy):  # pragma: no cover
    # Create "UMA" category to sumarize three columns.
    # uma_columns = ["UMA consultation", "UMA plateau technique", "UMA PMSI"]
    # assert all(col in care_site_hierarchy.columns for col in uma_columns)
    # care_site_hierarchy["UMA"] = (
    #     care_site_hierarchy.loc[:, uma_columns]
    #     .fillna(method="bfill", axis="columns")
    #     .iloc[:, 0]
    # )
    first_columns = ["id", "category"]
    all_columns = first_columns + [
        col for col in care_site_hierarchy.columns if col not in first_columns
    ]
    care_site_hierarchy = care_site_hierarchy.loc[:, all_columns]

    # Remove columns that contain no infos, ie there is no child of a different category
    parent_columns = [
        col for col in care_site_hierarchy.columns if col not in ["id", "category"]
    ]
    parent_columns_with_children = []
    for col in parent_columns:
        other_categories = care_site_hierarchy.loc[
            care_site_hierarchy["category"] != col
        ]
        if other_categories[col].notnull().any():
            # there is at least a child of another category
            parent_columns_with_children.append(col)
    care_site_hierarchy = care_site_hierarchy.loc[
        :, ["id", "category"] + parent_columns_with_children
    ]
    dropped = [col for col in parent_columns if col not in parent_columns_with_children]
    print(f"Dropping columns {dropped} as they contain no information for children")

    # Rename to match the column names in OMOP
    care_site_hierarchy = care_site_hierarchy.rename(
        columns={
            "id": "care_site_id",
            "category": "care_site_type_source_value",
        }
    )

    # Print some infos
    print("Distribution of <care_site_type_source_value>: ")
    print(care_site_hierarchy["care_site_type_source_value"].value_counts())
    print("Fraction of non-nulls: ")
    print(care_site_hierarchy.notnull().mean())
    return care_site_hierarchy


def _save_care_site_hierarchy(care_site_hierarchy, folder):  # pragma: no cover
    full_path = os.path.abspath(os.path.join(folder, "care_site_hierarchy.csv"))
    # float_format="%.0f" because otherwise the columns which contain care_site_ids with NaNs are
    # represented as "87738383.0" instead of "8278728"
    care_site_hierarchy.to_csv(full_path, index=False, float_format="%.0f")
    print(f"Saved {len(care_site_hierarchy)} rows to file {full_path}")


if __name__ == "__main__":  # pragma: no cover
    generate_care_site_hierarchy()
