# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ConditionDict generated type."""
import datetime
from typing import TypedDict

V1ConditionDict = TypedDict(
    "V1ConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "message": str,
        "observedGeneration": int,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)
