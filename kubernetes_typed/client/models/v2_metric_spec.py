# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2MetricSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2ContainerResourceMetricSourceDict, V2ExternalMetricSourceDict, V2ObjectMetricSourceDict, V2PodsMetricSourceDict, V2ResourceMetricSourceDict

V2MetricSpecDict = TypedDict(
    "V2MetricSpecDict",
    {
        "containerResource": V2ContainerResourceMetricSourceDict,
        "external": V2ExternalMetricSourceDict,
        "object": V2ObjectMetricSourceDict,
        "pods": V2PodsMetricSourceDict,
        "resource": V2ResourceMetricSourceDict,
        "type": str,
    },
    total=False,
)
