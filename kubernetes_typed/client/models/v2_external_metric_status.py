# Code generated by `typeddictgen`. DO NOT EDIT.
"""V2ExternalMetricStatusDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V2MetricIdentifierDict, V2MetricValueStatusDict

V2ExternalMetricStatusDict = TypedDict(
    "V2ExternalMetricStatusDict",
    {
        "current": V2MetricValueStatusDict,
        "metric": V2MetricIdentifierDict,
    },
    total=False,
)