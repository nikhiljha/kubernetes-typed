# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PodDisruptionBudgetListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1PodDisruptionBudgetDict

V1PodDisruptionBudgetListDict = TypedDict(
    "V1PodDisruptionBudgetListDict",
    {
        "apiVersion": str,
        "items": List[V1PodDisruptionBudgetDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
