# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2HorizontalPodAutoscalerListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V2HorizontalPodAutoscalerDict

V2HorizontalPodAutoscalerListDict = TypedDict(
    "V2HorizontalPodAutoscalerListDict",
    {
        "apiVersion": str,
        "items": List[V2HorizontalPodAutoscalerDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
