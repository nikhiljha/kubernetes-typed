# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2ContainerResourceMetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2MetricValueStatusDict

V2ContainerResourceMetricStatusDict = TypedDict(
    "V2ContainerResourceMetricStatusDict",
    {
        "container": str,
        "current": V2MetricValueStatusDict,
        "name": str,
    },
    total=False,
)