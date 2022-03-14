# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2beta2MetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import (
    V2beta2ContainerResourceMetricStatusDict,
    V2beta2ExternalMetricStatusDict,
    V2beta2ObjectMetricStatusDict,
    V2beta2PodsMetricStatusDict,
    V2beta2ResourceMetricStatusDict,
)

V2beta2MetricStatusDict = TypedDict(
    "V2beta2MetricStatusDict",
    {
        "containerResource": V2beta2ContainerResourceMetricStatusDict,
        "external": V2beta2ExternalMetricStatusDict,
        "object": V2beta2ObjectMetricStatusDict,
        "pods": V2beta2PodsMetricStatusDict,
        "resource": V2beta2ResourceMetricStatusDict,
        "type": str,
    },
    total=False,
)
