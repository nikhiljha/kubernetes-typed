# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1StorageOSVolumeSource:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, fs_type: Optional[Any] = ..., read_only: Optional[Any] = ..., secret_ref: Optional[Any] = ..., volume_name: Optional[Any] = ..., volume_namespace: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def fs_type(self): ...
    @fs_type.setter
    def fs_type(self, fs_type: Any) -> None: ...
    @property
    def read_only(self): ...
    @read_only.setter
    def read_only(self, read_only: Any) -> None: ...
    @property
    def secret_ref(self): ...
    @secret_ref.setter
    def secret_ref(self, secret_ref: Any) -> None: ...
    @property
    def volume_name(self): ...
    @volume_name.setter
    def volume_name(self, volume_name: Any) -> None: ...
    @property
    def volume_namespace(self): ...
    @volume_namespace.setter
    def volume_namespace(self, volume_namespace: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
