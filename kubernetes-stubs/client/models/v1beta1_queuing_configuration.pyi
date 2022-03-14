# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1QueuingConfiguration:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, hand_size: Optional[Any] = ..., queue_length_limit: Optional[Any] = ..., queues: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def hand_size(self): ...
    @hand_size.setter
    def hand_size(self, hand_size: Any) -> None: ...
    @property
    def queue_length_limit(self): ...
    @queue_length_limit.setter
    def queue_length_limit(self, queue_length_limit: Any) -> None: ...
    @property
    def queues(self): ...
    @queues.setter
    def queues(self, queues: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
