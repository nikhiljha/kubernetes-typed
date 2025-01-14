# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ManagedFieldsEntry:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_version: Optional[Any] = ..., fields_type: Optional[Any] = ..., fields_v1: Optional[Any] = ..., manager: Optional[Any] = ..., operation: Optional[Any] = ..., subresource: Optional[Any] = ..., time: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def fields_type(self): ...
    @fields_type.setter
    def fields_type(self, fields_type: Any) -> None: ...
    @property
    def fields_v1(self): ...
    @fields_v1.setter
    def fields_v1(self, fields_v1: Any) -> None: ...
    @property
    def manager(self): ...
    @manager.setter
    def manager(self, manager: Any) -> None: ...
    @property
    def operation(self): ...
    @operation.setter
    def operation(self, operation: Any) -> None: ...
    @property
    def subresource(self): ...
    @subresource.setter
    def subresource(self, subresource: Any) -> None: ...
    @property
    def time(self): ...
    @time.setter
    def time(self, time: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
