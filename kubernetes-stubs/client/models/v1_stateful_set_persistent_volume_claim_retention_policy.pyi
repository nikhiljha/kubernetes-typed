# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1StatefulSetPersistentVolumeClaimRetentionPolicy:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, when_deleted: Optional[Any] = ..., when_scaled: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def when_deleted(self): ...
    @when_deleted.setter
    def when_deleted(self, when_deleted: Any) -> None: ...
    @property
    def when_scaled(self): ...
    @when_scaled.setter
    def when_scaled(self, when_scaled: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
