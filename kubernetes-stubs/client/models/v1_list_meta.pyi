# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ListMeta:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, _continue: Optional[Any] = ..., remaining_item_count: Optional[Any] = ..., resource_version: Optional[Any] = ..., self_link: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def remaining_item_count(self): ...
    @remaining_item_count.setter
    def remaining_item_count(self, remaining_item_count: Any) -> None: ...
    @property
    def resource_version(self): ...
    @resource_version.setter
    def resource_version(self, resource_version: Any) -> None: ...
    @property
    def self_link(self): ...
    @self_link.setter
    def self_link(self, self_link: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...