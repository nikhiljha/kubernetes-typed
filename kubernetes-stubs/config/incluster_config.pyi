# Code generated by `stubgen`. DO NOT EDIT.
from .config_exception import ConfigException as ConfigException
from kubernetes.client import Configuration as Configuration
from typing import Any

SERVICE_HOST_ENV_NAME: str
SERVICE_PORT_ENV_NAME: str
SERVICE_TOKEN_FILENAME: str
SERVICE_CERT_FILENAME: str

class InClusterConfigLoader:
    def __init__(self, token_filename, cert_filename, try_refresh_token: bool = ..., environ=...) -> None: ...
    def load_and_set(self, client_configuration: Any | None = ...) -> None: ...

def load_incluster_config(client_configuration: Any | None = ..., try_refresh_token: bool = ...) -> None: ...