# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2HorizontalPodAutoscalerStatusDict generated type."""
import datetime
from typing import TypedDict, List

from kubernetes_typed.client import V2HorizontalPodAutoscalerConditionDict, V2MetricStatusDict

V2HorizontalPodAutoscalerStatusDict = TypedDict(
    "V2HorizontalPodAutoscalerStatusDict",
    {
        "conditions": List[V2HorizontalPodAutoscalerConditionDict],
        "currentMetrics": List[V2MetricStatusDict],
        "currentReplicas": int,
        "desiredReplicas": int,
        "lastScaleTime": datetime.datetime,
        "observedGeneration": int,
    },
    total=False,
)
