# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PodDisruptionBudgetStatusDict generated type."""
import datetime
from typing import TypedDict, Dict, List

from kubernetes_typed.client import V1ConditionDict

V1beta1PodDisruptionBudgetStatusDict = TypedDict(
    "V1beta1PodDisruptionBudgetStatusDict",
    {
        "conditions": List[V1ConditionDict],
        "currentHealthy": int,
        "desiredHealthy": int,
        "disruptedPods": Dict[str, datetime.datetime],
        "disruptionsAllowed": int,
        "expectedPods": int,
        "observedGeneration": int,
    },
    total=False,
)
