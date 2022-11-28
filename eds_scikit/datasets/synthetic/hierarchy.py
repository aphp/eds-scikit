import pandas as pd

from .base_dataset import Dataset, dataclass


@dataclass(repr=False)
class HierarchyDataset(Dataset):
    categories: pd.DataFrame
    relationships: pd.DataFrame


def load_hierarchy():
    ids = ["batiment1", "chambre1", "chambre2", "lit1", "lit2", "lit3"]
    categories_ = ["batiment", "chambre", "chambre", "lit", "lit", "lit"]
    categories = pd.DataFrame({"id": ids, "category": categories_})

    children = ["chambre1", "chambre2", "lit1", "lit2", "lit3"]
    parents = ["batiment1", "batiment1", "chambre1", "chambre1", "chambre2"]
    relationships = pd.DataFrame(
        {
            "child": children,
            "parent": parents,
        }
    )

    return HierarchyDataset(
        categories=categories,
        relationships=relationships,
    )
