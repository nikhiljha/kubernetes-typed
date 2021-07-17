# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V2alpha1JobTemplateSpecDict

V2alpha1CronJobSpecDict = TypedDict(
    "V2alpha1CronJobSpecDict",
    {
        "concurrencyPolicy": str,
        "failedJobsHistoryLimit": int,
        "jobTemplate": V2alpha1JobTemplateSpecDict,
        "schedule": str,
        "startingDeadlineSeconds": int,
        "successfulJobsHistoryLimit": int,
        "suspend": bool,
    },
    total=False,
)