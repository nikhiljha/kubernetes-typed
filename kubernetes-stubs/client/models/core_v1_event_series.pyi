# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class CoreV1EventSeries:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, count: Optional[Any] = ..., last_observed_time: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def count(self): ...
    @count.setter
    def count(self, count: Any) -> None: ...
    @property
    def last_observed_time(self): ...
    @last_observed_time.setter
    def last_observed_time(self, last_observed_time: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
