# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.configuration import Configuration as Configuration
from typing import Any, Optional

class EventsV1Event:
    openapi_types: Any = ...
    attribute_map: Any = ...
    local_vars_configuration: Any = ...
    discriminator: Any = ...
    def __init__(self, action: Optional[Any] = ..., api_version: Optional[Any] = ..., deprecated_count: Optional[Any] = ..., deprecated_first_timestamp: Optional[Any] = ..., deprecated_last_timestamp: Optional[Any] = ..., deprecated_source: Optional[Any] = ..., event_time: Optional[Any] = ..., kind: Optional[Any] = ..., metadata: Optional[Any] = ..., note: Optional[Any] = ..., reason: Optional[Any] = ..., regarding: Optional[Any] = ..., related: Optional[Any] = ..., reporting_controller: Optional[Any] = ..., reporting_instance: Optional[Any] = ..., series: Optional[Any] = ..., type: Optional[Any] = ..., local_vars_configuration: Optional[Any] = ...) -> None: ...
    @property
    def action(self): ...
    @action.setter
    def action(self, action: Any) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version: Any) -> None: ...
    @property
    def deprecated_count(self): ...
    @deprecated_count.setter
    def deprecated_count(self, deprecated_count: Any) -> None: ...
    @property
    def deprecated_first_timestamp(self): ...
    @deprecated_first_timestamp.setter
    def deprecated_first_timestamp(self, deprecated_first_timestamp: Any) -> None: ...
    @property
    def deprecated_last_timestamp(self): ...
    @deprecated_last_timestamp.setter
    def deprecated_last_timestamp(self, deprecated_last_timestamp: Any) -> None: ...
    @property
    def deprecated_source(self): ...
    @deprecated_source.setter
    def deprecated_source(self, deprecated_source: Any) -> None: ...
    @property
    def event_time(self): ...
    @event_time.setter
    def event_time(self, event_time: Any) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind: Any) -> None: ...
    @property
    def metadata(self): ...
    @metadata.setter
    def metadata(self, metadata: Any) -> None: ...
    @property
    def note(self): ...
    @note.setter
    def note(self, note: Any) -> None: ...
    @property
    def reason(self): ...
    @reason.setter
    def reason(self, reason: Any) -> None: ...
    @property
    def regarding(self): ...
    @regarding.setter
    def regarding(self, regarding: Any) -> None: ...
    @property
    def related(self): ...
    @related.setter
    def related(self, related: Any) -> None: ...
    @property
    def reporting_controller(self): ...
    @reporting_controller.setter
    def reporting_controller(self, reporting_controller: Any) -> None: ...
    @property
    def reporting_instance(self): ...
    @reporting_instance.setter
    def reporting_instance(self, reporting_instance: Any) -> None: ...
    @property
    def series(self): ...
    @series.setter
    def series(self, series: Any) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
