# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta2LimitedPriorityLevelConfigurationDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1beta2LimitResponseDict

V1beta2LimitedPriorityLevelConfigurationDict = TypedDict(
    "V1beta2LimitedPriorityLevelConfigurationDict",
    {
        "assuredConcurrencyShares": int,
        "limitResponse": V1beta2LimitResponseDict,
    },
    total=False,
)