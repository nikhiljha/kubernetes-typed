# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta2PriorityLevelConfigurationSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1beta2LimitedPriorityLevelConfigurationDict

V1beta2PriorityLevelConfigurationSpecDict = TypedDict(
    "V1beta2PriorityLevelConfigurationSpecDict",
    {
        "limited": V1beta2LimitedPriorityLevelConfigurationDict,
        "type": str,
    },
    total=False,
)
