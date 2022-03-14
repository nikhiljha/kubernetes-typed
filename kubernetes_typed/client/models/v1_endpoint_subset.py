# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1EndpointSubsetDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import CoreV1EndpointPortDict, V1EndpointAddressDict

V1EndpointSubsetDict = TypedDict(
    "V1EndpointSubsetDict",
    {
        "addresses": List[V1EndpointAddressDict],
        "notReadyAddresses": List[V1EndpointAddressDict],
        "ports": List[CoreV1EndpointPortDict],
    },
    total=False,
)
