# Code generated by `typeddictgen`. DO NOT EDIT.
import datetime
from typing import TypedDict, List

from kubernetes_typed.client import V1ObjectReferenceDict

V1beta1CronJobStatusDict = TypedDict(
    "V1beta1CronJobStatusDict",
    {
        "active": List[V1ObjectReferenceDict],
        "lastScheduleTime": datetime.datetime,
    },
    total=False,
)