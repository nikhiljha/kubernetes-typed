# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CronJobListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1CronJobDict, V1ListMetaDict

V1CronJobListDict = TypedDict(
    "V1CronJobListDict",
    {
        "apiVersion": str,
        "items": List[V1CronJobDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
