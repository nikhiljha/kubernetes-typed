# Code generated by `stubgen`. DO NOT EDIT.
from typing import Any, Optional

class Resource:
    prefix: Any = ...
    group: Any = ...
    api_version: Any = ...
    kind: Any = ...
    namespaced: Any = ...
    verbs: Any = ...
    name: Any = ...
    preferred: Any = ...
    client: Any = ...
    singular_name: Any = ...
    short_names: Any = ...
    categories: Any = ...
    subresources: Any = ...
    extra_args: Any = ...
    def __init__(self, prefix: Optional[Any] = ..., group: Optional[Any] = ..., api_version: Optional[Any] = ..., kind: Optional[Any] = ..., namespaced: bool = ..., verbs: Optional[Any] = ..., name: Optional[Any] = ..., preferred: bool = ..., client: Optional[Any] = ..., singularName: Optional[Any] = ..., shortNames: Optional[Any] = ..., categories: Optional[Any] = ..., subresources: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def to_dict(self): ...
    @property
    def group_version(self): ...
    @property
    def urls(self): ...
    def path(self, name: Optional[Any] = ..., namespace: Optional[Any] = ...): ...
    def __getattr__(self, name: Any): ...

class ResourceList(Resource):
    client: Any = ...
    group: Any = ...
    api_version: Any = ...
    kind: Any = ...
    base_kind: Any = ...
    base_resource_lookup: Any = ...
    def __init__(self, client: Any, group: str = ..., api_version: str = ..., base_kind: str = ..., kind: Optional[Any] = ..., base_resource_lookup: Optional[Any] = ...) -> None: ...
    def base_resource(self): ...
    def get(self, body: Any, name: Optional[Any] = ..., namespace: Optional[Any] = ..., **kwargs: Any): ...
    def delete(self, body: Any, name: Optional[Any] = ..., namespace: Optional[Any] = ..., **kwargs: Any): ...
    def verb_mapper(self, verb: Any, body: Any, **kwargs: Any): ...
    def create(self, *args: Any, **kwargs: Any): ...
    def replace(self, *args: Any, **kwargs: Any): ...
    def patch(self, *args: Any, **kwargs: Any): ...
    def to_dict(self): ...
    def __getattr__(self, name: Any): ...

class Subresource(Resource):
    parent: Any = ...
    prefix: Any = ...
    group: Any = ...
    api_version: Any = ...
    kind: Any = ...
    name: Any = ...
    subresource: Any = ...
    namespaced: Any = ...
    verbs: Any = ...
    extra_args: Any = ...
    def __init__(self, parent: Any, **kwargs: Any) -> None: ...
    def create(self, body: Optional[Any] = ..., name: Optional[Any] = ..., namespace: Optional[Any] = ..., **kwargs: Any): ...
    @property
    def urls(self): ...
    def __getattr__(self, name: Any): ...
    def to_dict(self): ...

class ResourceInstance:
    client: Any = ...
    attributes: Any = ...
    def __init__(self, client: Any, instance: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any): ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def __dir__(self): ...

class ResourceField:
    def __init__(self, params: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __getitem__(self, name: Any): ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def __dir__(self): ...
    def __iter__(self) -> Any: ...
