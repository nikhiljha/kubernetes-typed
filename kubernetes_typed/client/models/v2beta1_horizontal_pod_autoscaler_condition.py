# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict

V2beta1HorizontalPodAutoscalerConditionDict = TypedDict(
    "V2beta1HorizontalPodAutoscalerConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)