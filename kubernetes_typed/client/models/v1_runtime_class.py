# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1RuntimeClassDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1OverheadDict, V1SchedulingDict

V1RuntimeClassDict = TypedDict(
    "V1RuntimeClassDict",
    {
        "apiVersion": str,
        "handler": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "overhead": V1OverheadDict,
        "scheduling": V1SchedulingDict,
    },
    total=False,
)