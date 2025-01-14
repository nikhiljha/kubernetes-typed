# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1JobStatusDict generated type."""
import datetime
from typing import TypedDict, List

from kubernetes_typed.client import V1JobConditionDict, V1UncountedTerminatedPodsDict

V1JobStatusDict = TypedDict(
    "V1JobStatusDict",
    {
        "active": int,
        "completedIndexes": str,
        "completionTime": datetime.datetime,
        "conditions": List[V1JobConditionDict],
        "failed": int,
        "ready": int,
        "startTime": datetime.datetime,
        "succeeded": int,
        "uncountedTerminatedPods": V1UncountedTerminatedPodsDict,
    },
    total=False,
)
