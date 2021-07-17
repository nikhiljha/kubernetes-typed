# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1LabelSelectorDict, V1PodTemplateSpecDict, V1beta1DaemonSetUpdateStrategyDict

V1beta1DaemonSetSpecDict = TypedDict(
    "V1beta1DaemonSetSpecDict",
    {
        "minReadySeconds": int,
        "revisionHistoryLimit": int,
        "selector": V1LabelSelectorDict,
        "template": V1PodTemplateSpecDict,
        "templateGeneration": int,
        "updateStrategy": V1beta1DaemonSetUpdateStrategyDict,
    },
    total=False,
)