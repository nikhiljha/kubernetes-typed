# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2ContainerResourceMetricSourceDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2MetricTargetDict

V2ContainerResourceMetricSourceDict = TypedDict(
    "V2ContainerResourceMetricSourceDict",
    {
        "container": str,
        "name": str,
        "target": V2MetricTargetDict,
    },
    total=False,
)