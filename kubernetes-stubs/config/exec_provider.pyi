# Code generated by `stubgen`. DO NOT EDIT.
from .config_exception import ConfigException as ConfigException
from typing import Any, Optional

class ExecProvider:
    api_version: Any = ...
    args: Any = ...
    env: Any = ...
    cwd: Any = ...
    def __init__(self, exec_config: Any, cwd: Any) -> None: ...
    def run(self, previous_response: Optional[Any] = ...): ...
