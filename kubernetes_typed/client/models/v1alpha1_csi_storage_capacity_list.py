# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1CSIStorageCapacityListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1alpha1CSIStorageCapacityDict

V1alpha1CSIStorageCapacityListDict = TypedDict(
    "V1alpha1CSIStorageCapacityListDict",
    {
        "apiVersion": str,
        "items": List[V1alpha1CSIStorageCapacityDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
