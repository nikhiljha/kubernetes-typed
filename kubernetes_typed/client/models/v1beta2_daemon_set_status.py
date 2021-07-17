# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1beta2DaemonSetConditionDict

V1beta2DaemonSetStatusDict = TypedDict(
    "V1beta2DaemonSetStatusDict",
    {
        "collisionCount": int,
        "conditions": List[V1beta2DaemonSetConditionDict],
        "currentNumberScheduled": int,
        "desiredNumberScheduled": int,
        "numberAvailable": int,
        "numberMisscheduled": int,
        "numberReady": int,
        "numberUnavailable": int,
        "observedGeneration": int,
        "updatedNumberScheduled": int,
    },
    total=False,
)