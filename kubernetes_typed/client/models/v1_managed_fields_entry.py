# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1ManagedFieldsEntryDict generated type."""
import datetime
from typing import TypedDict

V1ManagedFieldsEntryDict = TypedDict(
    "V1ManagedFieldsEntryDict",
    {
        "apiVersion": str,
        "fieldsType": str,
        "fieldsV1": object,
        "manager": str,
        "operation": str,
        "subresource": str,
        "time": datetime.datetime,
    },
    total=False,
)
