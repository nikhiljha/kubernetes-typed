# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

from kubernetes_typed.client import V1ListMetaDict, V1beta1CronJobDict

V1beta1CronJobListDict = TypedDict(
    "V1beta1CronJobListDict",
    {
        "apiVersion": str,
        "items": List[V1beta1CronJobDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)