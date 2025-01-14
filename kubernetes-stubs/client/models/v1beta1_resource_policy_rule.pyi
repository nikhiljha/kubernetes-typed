# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1beta1ResourcePolicyRule:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, api_groups: Optional[Any] = ..., cluster_scope: Optional[Any] = ..., namespaces: Optional[Any] = ..., resources: Optional[Any] = ..., verbs: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def api_groups(self): ...
    @api_groups.setter
    def api_groups(self, api_groups: Any) -> None: ...
    @property
    def cluster_scope(self): ...
    @cluster_scope.setter
    def cluster_scope(self, cluster_scope: Any) -> None: ...
    @property
    def namespaces(self): ...
    @namespaces.setter
    def namespaces(self, namespaces: Any) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources: Any) -> None: ...
    @property
    def verbs(self): ...
    @verbs.setter
    def verbs(self, verbs: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
