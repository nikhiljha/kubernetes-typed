# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1StorageClassDict

V1StorageClassListDict = TypedDict(
    "V1StorageClassListDict",
    {
        "apiVersion": str,
        "items": List[V1StorageClassDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)