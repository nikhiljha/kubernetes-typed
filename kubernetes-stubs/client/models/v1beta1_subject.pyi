# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1Subject:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, group: Optional[Any] = ..., kind: Optional[Any] = ..., service_account: Optional[Any] = ..., user: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def group(self): ...
    @group.setter
    def group(self, group: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def service_account(self): ...
    @service_account.setter
    def service_account(self, service_account: Any) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
