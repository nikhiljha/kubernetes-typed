# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1PersistentVolumeStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, message: Optional[Any] = ..., phase: Optional[Any] = ..., reason: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message: Any) -> None: ...
    @property
    def phase(self): ...
    @phase.setter
    def phase(self, phase: Any) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
