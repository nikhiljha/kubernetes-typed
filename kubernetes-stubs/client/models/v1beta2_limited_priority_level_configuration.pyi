# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta2LimitedPriorityLevelConfiguration:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, assured_concurrency_shares: Optional[Any] = ..., limit_response: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def assured_concurrency_shares(self): ...
    @assured_concurrency_shares.setter
    def assured_concurrency_shares(self, assured_concurrency_shares: Any) -> None: ...
    @property
    def limit_response(self): ...
    @limit_response.setter
    def limit_response(self, limit_response: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...