# Code generated by `typeddictgen`. DO NOT EDIT.
from typing import TypedDict

V1AzureFilePersistentVolumeSourceDict = TypedDict(
    "V1AzureFilePersistentVolumeSourceDict",
    {
        "readOnly": bool,
        "secretName": str,
        "secretNamespace": str,
        "shareName": str,
    },
    total=False,
)