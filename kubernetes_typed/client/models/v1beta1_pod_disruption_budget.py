# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1PodDisruptionBudgetSpecDict, V1beta1PodDisruptionBudgetStatusDict

V1beta1PodDisruptionBudgetDict = TypedDict(
    "V1beta1PodDisruptionBudgetDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1PodDisruptionBudgetSpecDict,
        "status": V1beta1PodDisruptionBudgetStatusDict,
    },
    total=False,
)