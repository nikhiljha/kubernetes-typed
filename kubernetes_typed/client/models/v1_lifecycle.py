# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

from kubernetes_typed.client import V1HandlerDict

V1LifecycleDict = TypedDict(
    "V1LifecycleDict",
    {
        "postStart": V1HandlerDict,
        "preStop": V1HandlerDict,
    },
    total=False,
)