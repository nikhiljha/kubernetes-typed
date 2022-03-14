# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PersistentVolumeClaimStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, access_modes: Optional[Any] = ..., allocated_resources: Optional[Any] = ..., capacity: Optional[Any] = ..., conditions: Optional[Any] = ..., phase: Optional[Any] = ..., resize_status: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def access_modes(self): ...
    @access_modes.setter
    def access_modes(self, access_modes: Any) -> None: ...
    @property
    def allocated_resources(self): ...
    @allocated_resources.setter
    def allocated_resources(self, allocated_resources: Any) -> None: ...
    @property
    def capacity(self): ...
    @capacity.setter
    def capacity(self, capacity: Any) -> None: ...
    @property
    def conditions(self): ...
    @conditions.setter
    def conditions(self, conditions: Any) -> None: ...
    @property
    def phase(self): ...
    @phase.setter
    def phase(self, phase: Any) -> None: ...
    @property
    def resize_status(self): ...
    @resize_status.setter
    def resize_status(self, resize_status: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
