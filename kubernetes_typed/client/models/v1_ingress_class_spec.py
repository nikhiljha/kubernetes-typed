# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1IngressClassSpecDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1IngressClassParametersReferenceDict

V1IngressClassSpecDict = TypedDict(
    "V1IngressClassSpecDict",
    {
        "controller": str,
        "parameters": V1IngressClassParametersReferenceDict,
    },
    total=False,
)