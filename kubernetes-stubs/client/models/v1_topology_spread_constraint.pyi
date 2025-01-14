# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class V1TopologySpreadConstraint:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, label_selector: Optional[Any] = ..., match_label_keys: Optional[Any] = ..., max_skew: Optional[Any] = ..., min_domains: Optional[Any] = ..., node_affinity_policy: Optional[Any] = ..., node_taints_policy: Optional[Any] = ..., topology_key: Optional[Any] = ..., when_unsatisfiable: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def label_selector(self): ...
    @label_selector.setter
    def label_selector(self, label_selector: Any) -> None: ...
    @property
    def match_label_keys(self): ...
    @match_label_keys.setter
    def match_label_keys(self, match_label_keys: Any) -> None: ...
    @property
    def max_skew(self): ...
    @max_skew.setter
    def max_skew(self, max_skew: Any) -> None: ...
    @property
    def min_domains(self): ...
    @min_domains.setter
    def min_domains(self, min_domains: Any) -> None: ...
    @property
    def node_affinity_policy(self): ...
    @node_affinity_policy.setter
    def node_affinity_policy(self, node_affinity_policy: Any) -> None: ...
    @property
    def node_taints_policy(self): ...
    @node_taints_policy.setter
    def node_taints_policy(self, node_taints_policy: Any) -> None: ...
    @property
    def topology_key(self): ...
    @topology_key.setter
    def topology_key(self, topology_key: Any) -> None: ...
    @property
    def when_unsatisfiable(self): ...
    @when_unsatisfiable.setter
    def when_unsatisfiable(self, when_unsatisfiable: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
