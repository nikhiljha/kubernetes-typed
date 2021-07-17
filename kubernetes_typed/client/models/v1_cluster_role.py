# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1AggregationRuleDict, V1ObjectMetaDict, V1PolicyRuleDict

V1ClusterRoleDict = TypedDict(
    "V1ClusterRoleDict",
    {
        "aggregationRule": V1AggregationRuleDict,
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "rules": List[V1PolicyRuleDict],
    },
    total=False,
)