# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1alpha1ServerStorageVersionDict generated type."""
from typing import TypedDict, List

V1alpha1ServerStorageVersionDict = TypedDict(
    "V1alpha1ServerStorageVersionDict",
    {
        "apiServerID": str,
        "decodableVersions": List[str],
        "encodingVersion": str,
    },
    total=False,
)
