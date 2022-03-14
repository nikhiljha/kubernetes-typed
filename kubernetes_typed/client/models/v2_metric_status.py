# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2MetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2ContainerResourceMetricStatusDict, V2ExternalMetricStatusDict, V2ObjectMetricStatusDict, V2PodsMetricStatusDict, V2ResourceMetricStatusDict

V2MetricStatusDict = TypedDict(
    "V2MetricStatusDict",
    {
        "containerResource": V2ContainerResourceMetricStatusDict,
        "external": V2ExternalMetricStatusDict,
        "object": V2ObjectMetricStatusDict,
        "pods": V2PodsMetricStatusDict,
        "resource": V2ResourceMetricStatusDict,
        "type": str,
    },
    total=False,
)
