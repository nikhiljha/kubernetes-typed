# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict

V1StatefulSetConditionDict = TypedDict(
    "V1StatefulSetConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)