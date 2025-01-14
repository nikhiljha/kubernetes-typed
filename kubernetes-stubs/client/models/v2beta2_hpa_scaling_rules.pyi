# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V2beta2HPAScalingRules:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, policies: Optional[Any] = ..., select_policy: Optional[Any] = ..., stabilization_window_seconds: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def policies(self): ...
    @policies.setter
    def policies(self, policies: Any) -> None: ...
    @property
    def select_policy(self): ...
    @select_policy.setter
    def select_policy(self, select_policy: Any) -> None: ...
    @property
    def stabilization_window_seconds(self): ...
    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, stabilization_window_seconds: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
