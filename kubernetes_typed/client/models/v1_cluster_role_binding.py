# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ObjectMetaDict, V1RoleRefDict, V1SubjectDict

V1ClusterRoleBindingDict = TypedDict(
    "V1ClusterRoleBindingDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "roleRef": V1RoleRefDict,
        "subjects": List[V1SubjectDict],
    },
    total=False,
)