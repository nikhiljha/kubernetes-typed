# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PriorityLevelConfigurationStatusDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1beta1PriorityLevelConfigurationConditionDict

V1beta1PriorityLevelConfigurationStatusDict = TypedDict(
    "V1beta1PriorityLevelConfigurationStatusDict",
    {
        "conditions": List[V1beta1PriorityLevelConfigurationConditionDict],
    },
    total=False,
)
