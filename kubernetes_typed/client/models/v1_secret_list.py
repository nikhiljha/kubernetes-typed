# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1SecretDict

V1SecretListDict = TypedDict(
    "V1SecretListDict",
    {
        "apiVersion": str,
        "items": List[V1SecretDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)