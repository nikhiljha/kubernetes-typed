# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2ResourceMetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2MetricValueStatusDict

V2ResourceMetricStatusDict = TypedDict(
    "V2ResourceMetricStatusDict",
    {
        "current": V2MetricValueStatusDict,
        "name": str,
    },
    total=False,
)
