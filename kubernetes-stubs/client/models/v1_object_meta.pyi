# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1ObjectMeta:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, annotations: Optional[Any] = ..., creation_timestamp: Optional[Any] = ..., deletion_grace_period_seconds: Optional[Any] = ..., deletion_timestamp: Optional[Any] = ..., finalizers: Optional[Any] = ..., generate_name: Optional[Any] = ..., generation: Optional[Any] = ..., labels: Optional[Any] = ..., managed_fields: Optional[Any] = ..., name: Optional[Any] = ..., namespace: Optional[Any] = ..., owner_references: Optional[Any] = ..., resource_version: Optional[Any] = ..., self_link: Optional[Any] = ..., uid: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def annotations(self): ...
    @annotations.setter
    def annotations(self, annotations: Any) -> None: ...
    @property
    def creation_timestamp(self): ...
    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp: Any) -> None: ...
    @property
    def deletion_grace_period_seconds(self): ...
    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, deletion_grace_period_seconds: Any) -> None: ...
    @property
    def deletion_timestamp(self): ...
    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp: Any) -> None: ...
    @property
    def finalizers(self): ...
    @finalizers.setter
    def finalizers(self, finalizers: Any) -> None: ...
    @property
    def generate_name(self): ...
    @generate_name.setter
    def generate_name(self, generate_name: Any) -> None: ...
    @property
    def generation(self): ...
    @generation.setter
    def generation(self, generation: Any) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels: Any) -> None: ...
    @property
    def managed_fields(self): ...
    @managed_fields.setter
    def managed_fields(self, managed_fields: Any) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name: Any) -> None: ...
    @property
    def namespace(self): ...
    @namespace.setter
    def namespace(self, namespace: Any) -> None: ...
    @property
    def owner_references(self): ...
    @owner_references.setter
    def owner_references(self, owner_references: Any) -> None: ...
    @property
    def resource_version(self): ...
    @resource_version.setter
    def resource_version(self, resource_version: Any) -> None: ...
    @property
    def self_link(self): ...
    @self_link.setter
    def self_link(self, self_link: Any) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
