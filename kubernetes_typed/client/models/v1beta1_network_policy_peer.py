# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LabelSelectorDict, V1beta1IPBlockDict

V1beta1NetworkPolicyPeerDict = TypedDict(
    "V1beta1NetworkPolicyPeerDict",
    {
        "ipBlock": V1beta1IPBlockDict,
        "namespaceSelector": V1LabelSelectorDict,
        "podSelector": V1LabelSelectorDict,
    },
    total=False,
)