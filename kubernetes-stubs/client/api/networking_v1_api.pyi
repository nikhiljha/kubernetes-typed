# Code generated by `stubgen`. DO NOT EDIT.
from kubernetes.client.api_client import ApiClient as ApiClient
from kubernetes.client.exceptions import ApiTypeError as ApiTypeError, ApiValueError as ApiValueError
from typing import Any, Optional

class NetworkingV1Api:
    api_client: Any = ...
    def __init__(self, api_client: Optional[Any] = ...) -> None: ...
    def create_ingress_class(self, body: Any, **kwargs: Any): ...
    def create_ingress_class_with_http_info(self, body: Any, **kwargs: Any): ...
    def create_namespaced_ingress(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_ingress_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_network_policy(self, namespace: Any, body: Any, **kwargs: Any): ...
    def create_namespaced_network_policy_with_http_info(self, namespace: Any, body: Any, **kwargs: Any): ...
    def delete_collection_ingress_class(self, **kwargs: Any): ...
    def delete_collection_ingress_class_with_http_info(self, **kwargs: Any): ...
    def delete_collection_namespaced_ingress(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_ingress_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_network_policy(self, namespace: Any, **kwargs: Any): ...
    def delete_collection_namespaced_network_policy_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def delete_ingress_class(self, name: Any, **kwargs: Any): ...
    def delete_ingress_class_with_http_info(self, name: Any, **kwargs: Any): ...
    def delete_namespaced_ingress(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_ingress_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_network_policy(self, name: Any, namespace: Any, **kwargs: Any): ...
    def delete_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def get_api_resources(self, **kwargs: Any): ...
    def get_api_resources_with_http_info(self, **kwargs: Any): ...
    def list_ingress_class(self, **kwargs: Any): ...
    def list_ingress_class_with_http_info(self, **kwargs: Any): ...
    def list_ingress_for_all_namespaces(self, **kwargs: Any): ...
    def list_ingress_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def list_namespaced_ingress(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_ingress_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_network_policy(self, namespace: Any, **kwargs: Any): ...
    def list_namespaced_network_policy_with_http_info(self, namespace: Any, **kwargs: Any): ...
    def list_network_policy_for_all_namespaces(self, **kwargs: Any): ...
    def list_network_policy_for_all_namespaces_with_http_info(self, **kwargs: Any): ...
    def patch_ingress_class(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_ingress_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_ingress(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_ingress_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_ingress_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_ingress_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_network_policy(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_network_policy_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def patch_namespaced_network_policy_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def read_ingress_class(self, name: Any, **kwargs: Any): ...
    def read_ingress_class_with_http_info(self, name: Any, **kwargs: Any): ...
    def read_namespaced_ingress(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_ingress_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_ingress_status(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_ingress_status_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_network_policy(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_network_policy_status(self, name: Any, namespace: Any, **kwargs: Any): ...
    def read_namespaced_network_policy_status_with_http_info(self, name: Any, namespace: Any, **kwargs: Any): ...
    def replace_ingress_class(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_ingress_class_with_http_info(self, name: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_ingress(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_ingress_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_ingress_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_ingress_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy_status(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
    def replace_namespaced_network_policy_status_with_http_info(self, name: Any, namespace: Any, body: Any, **kwargs: Any): ...
