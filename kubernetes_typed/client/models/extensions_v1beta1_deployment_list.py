# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import ExtensionsV1beta1DeploymentDict, V1ListMetaDict

ExtensionsV1beta1DeploymentListDict = TypedDict(
    "ExtensionsV1beta1DeploymentListDict",
    {
        "apiVersion": str,
        "items": List[ExtensionsV1beta1DeploymentDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)