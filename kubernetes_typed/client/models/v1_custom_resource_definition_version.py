# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CustomResourceDefinitionVersionDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1CustomResourceColumnDefinitionDict, V1CustomResourceSubresourcesDict, V1CustomResourceValidationDict

V1CustomResourceDefinitionVersionDict = TypedDict(
    "V1CustomResourceDefinitionVersionDict",
    {
        "additionalPrinterColumns": List[V1CustomResourceColumnDefinitionDict],
        "deprecated": bool,
        "deprecationWarning": str,
        "name": str,
        "schema": V1CustomResourceValidationDict,
        "served": bool,
        "storage": bool,
        "subresources": V1CustomResourceSubresourcesDict,
    },
    total=False,
)
