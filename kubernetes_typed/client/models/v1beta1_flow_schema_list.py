# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1FlowSchemaListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta1FlowSchemaDict

V1beta1FlowSchemaListDict = TypedDict(
    "V1beta1FlowSchemaListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1FlowSchemaDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
