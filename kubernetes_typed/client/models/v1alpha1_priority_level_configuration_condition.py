# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict

V1alpha1PriorityLevelConfigurationConditionDict = TypedDict(
    "V1alpha1PriorityLevelConfigurationConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)