# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1CronJobStatus:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, active: Optional[Any] = ..., last_schedule_time: Optional[Any] = ..., last_successful_time: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def active(self): ...
    @active.setter
    def active(self, active: Any) -> None: ...
    @property
    def last_schedule_time(self): ...
    @last_schedule_time.setter
    def last_schedule_time(self, last_schedule_time: Any) -> None: ...
    @property
    def last_successful_time(self): ...
    @last_successful_time.setter
    def last_successful_time(self, last_successful_time: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
