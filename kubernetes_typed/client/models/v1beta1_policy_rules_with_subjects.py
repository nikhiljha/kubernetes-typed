# Code generated by `typeddictgen`. DO NOT EDIT.
"""V1beta1PolicyRulesWithSubjectsDict generated type."""
from typing import TypedDict, List

from kubernetes_typed.client import V1beta1NonResourcePolicyRuleDict, V1beta1ResourcePolicyRuleDict, V1beta1SubjectDict

V1beta1PolicyRulesWithSubjectsDict = TypedDict(
    "V1beta1PolicyRulesWithSubjectsDict",
    {
        "nonResourceRules": List[V1beta1NonResourcePolicyRuleDict],
        "resourceRules": List[V1beta1ResourcePolicyRuleDict],
        "subjects": List[V1beta1SubjectDict],
    },
    total=False,
)