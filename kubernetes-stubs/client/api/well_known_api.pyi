# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class WellKnownApi:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def get_service_account_issuer_open_id_configuration(self, **kwargs: Any): ...
    def get_service_account_issuer_open_id_configuration_with_http_info(self, **kwargs: Any): ...
