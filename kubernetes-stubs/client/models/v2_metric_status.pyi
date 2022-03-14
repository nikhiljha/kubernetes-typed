# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2MetricStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, container_resource: Optional[Any] = ..., external: Optional[Any] = ..., object: Optional[Any] = ..., pods: Optional[Any] = ..., resource: Optional[Any] = ..., type: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def container_resource(self): ...
    @container_resource.setter
    def container_resource(self, container_resource: Any) -> None: ...
    @property
    def external(self): ...
    @external.setter
    def external(self, external: Any) -> None: ...
    @property
    def object(self): ...
    @object.setter
    def object(self, object: Any) -> None: ...
    @property
    def pods(self): ...
    @pods.setter
    def pods(self, pods: Any) -> None: ...
    @property
    def resource(self): ...
    @resource.setter
    def resource(self, resource: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
