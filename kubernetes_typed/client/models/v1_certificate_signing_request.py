# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CertificateSigningRequestDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1CertificateSigningRequestSpecDict, V1CertificateSigningRequestStatusDict, V1ObjectMetaDict

V1CertificateSigningRequestDict = TypedDict(
    "V1CertificateSigningRequestDict",
    {
        "apiVersion": str,
        "kind": str,
        "metadata": V1ObjectMetaDict,
        "spec": V1CertificateSigningRequestSpecDict,
        "status": V1CertificateSigningRequestStatusDict,
    },
    total=False,
)