# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1PersistentVolumeClaimTemplateDict generated type."""
from typing import TypedDict

from kubernetes_typed.client import V1ObjectMetaDict, V1PersistentVolumeClaimSpecDict

V1PersistentVolumeClaimTemplateDict = TypedDict(
    "V1PersistentVolumeClaimTemplateDict",
    {
        "metadata": V1ObjectMetaDict,
        "spec": V1PersistentVolumeClaimSpecDict,
    },
    total=False,
)
