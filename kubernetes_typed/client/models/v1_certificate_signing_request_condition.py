# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1CertificateSigningRequestConditionDict generated type."""
import datetime
from typing import TypedDict

V1CertificateSigningRequestConditionDict = TypedDict(
    "V1CertificateSigningRequestConditionDict",
    {
        "lastTransitionTime": datetime.datetime,
        "lastUpdateTime": datetime.datetime,
        "message": str,
        "reason": str,
        "status": str,
        "type": str,
    },
    total=False,
)