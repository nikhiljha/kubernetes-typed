# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1IngressListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1IngressDict, V1ListMetaDict

V1IngressListDict = TypedDict(
    "V1IngressListDict",
    {
        "apiVersion": str,
        "items": List[V1IngressDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
