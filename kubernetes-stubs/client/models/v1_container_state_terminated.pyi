# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ContainerStateTerminated:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, container_id: Optional[Any] = ..., exit_code: Optional[Any] = ..., finished_at: Optional[Any] = ..., message: Optional[Any] = ..., reason: Optional[Any] = ..., signal: Optional[Any] = ..., started_at: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def container_id(self): ...
    @container_id.setter
    def container_id(self, container_id: Any) -> None: ...
    @property
    def exit_code(self): ...
    @exit_code.setter
    def exit_code(self, exit_code: Any) -> None: ...
    @property
    def finished_at(self): ...
    @finished_at.setter
    def finished_at(self, finished_at: Any) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message: Any) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason: Any) -> None: ...
    @property
    def signal(self): ...
    @signal.setter
    def signal(self, signal: Any) -> None: ...
    @property
    def started_at(self): ...
    @started_at.setter
    def started_at(self, started_at: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
