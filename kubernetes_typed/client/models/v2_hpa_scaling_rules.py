# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2HPAScalingRulesDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V2HPAScalingPolicyDict

V2HPAScalingRulesDict = TypedDict(
    "V2HPAScalingRulesDict",
    {
        "policies": List[V2HPAScalingPolicyDict],
        "selectPolicy": str,
        "stabilizationWindowSeconds": int,
    },
    total=False,
)