# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CertificateSigningRequestListDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1CertificateSigningRequestDict, V1ListMetaDict

V1CertificateSigningRequestListDict = TypedDict(
    "V1CertificateSigningRequestListDict",
    {
        "apiVersion": str,
        "items": List[V1CertificateSigningRequestDict],
        "kind": str,
        "metadata": V1ListMetaDict,
    },
    total=False,
)
