# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1alpha1LimitResponseDict

V1alpha1LimitedPriorityLevelConfigurationDict = TypedDict(
    "V1alpha1LimitedPriorityLevelConfigurationDict",
    {
        "assuredConcurrencyShares": int,
        "limitResponse": V1alpha1LimitResponseDict,
    },
    total=False,
)