# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1HTTPIngressRuleValueDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1HTTPIngressPathDict

V1HTTPIngressRuleValueDict = TypedDict(
    "V1HTTPIngressRuleValueDict",
    {
        "paths": List[V1HTTPIngressPathDict],
    },
    total=False,
)
