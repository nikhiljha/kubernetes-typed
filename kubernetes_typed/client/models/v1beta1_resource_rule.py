# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict, List

V1beta1ResourceRuleDict = TypedDict(
    "V1beta1ResourceRuleDict",
    {
        "apiGroups": List[str],
        "resourceNames": List[str],
        "resources": List[str],
        "verbs": List[str],
    },
    total=False,
)