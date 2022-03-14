# Code generated by `stubgen`. DO NOT EDIT.
import unittest
from kubernetes import client as client, utils as utils
from kubernetes.client.rest import ApiException as ApiException
from kubernetes.e2e_test import base as base

class TestUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def test_create_apps_deployment_from_yaml(self) -> None: ...
    def test_create_apps_deployment_from_yaml_object(self) -> None: ...
    def test_create_apps_deployment_from_yaml_obj(self) -> None: ...
    def test_create_pod_from_yaml(self) -> None: ...
    def test_create_service_from_yaml(self) -> None: ...
    def test_create_namespace_from_yaml(self) -> None: ...
    def test_create_rbac_role_from_yaml(self) -> None: ...
    def test_create_rbac_role_from_yaml_with_verbose_enabled(self) -> None: ...
    def test_create_deployment_non_default_namespace_from_yaml(self) -> None: ...
    def test_create_apiservice_from_yaml_with_conflict(self) -> None: ...
    def test_create_general_list_from_yaml(self) -> None: ...
    def test_create_namespace_list_from_yaml(self) -> None: ...
    def test_create_implicit_service_list_from_yaml_with_conflict(self) -> None: ...
    def test_create_multi_resource_from_directory(self) -> None: ...
    def test_create_from_multi_resource_yaml(self) -> None: ...
    def test_create_from_list_in_multi_resource_yaml(self) -> None: ...
    def test_create_from_multi_resource_yaml_with_conflict(self) -> None: ...
    def test_create_from_multi_resource_yaml_with_multi_conflicts(self) -> None: ...
    def test_create_namespaced_apps_deployment_from_yaml(self) -> None: ...
    def test_create_from_list_in_multi_resource_yaml_namespaced(self) -> None: ...
