# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2PodsMetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2MetricIdentifierDict, V2MetricValueStatusDict

V2PodsMetricStatusDict = TypedDict(
    "V2PodsMetricStatusDict",
    {
        "current": V2MetricValueStatusDict,
        "metric": V2MetricIdentifierDict,
    },
    total=False,
)
