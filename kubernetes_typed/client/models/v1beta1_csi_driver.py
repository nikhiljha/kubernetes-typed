# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1beta1CSIDriverSpecDict

V1beta1CSIDriverDict = TypedDict(
    "V1beta1CSIDriverDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1beta1CSIDriverSpecDict,
    },
    total=False,
)