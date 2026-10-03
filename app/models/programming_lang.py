"""
SYNAPSE HELIOS ID - Programming Languages Schemas
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class LanguageMetric(BaseModel):
    label: str
    value: str
    rating: int  # 1 to 5 scale

class ProgrammingLanguage(BaseModel):
    id: str
    name: str
    version_standard: str
    logo_url: str
    role_indonesian: str
    primary_ecosystem: str
    performance_tier: str  # e.g. "Level 1 - Bare Metal CUDA / Kernel", "Level 2 - High Concurrency Native"
    specific_use_cases: List[str]
    architectural_role: str
    strengths: List[str]
    code_example_title: str
    code_example: str
    runtime_environment: str
    metrics: Dict[str, str]

class LanguagesResponse(BaseModel):
    system: str = "SYNAPSE HELIOS ID"
    status: str = "SYNCHRONIZED"
    total_languages: int
    languages: List[ProgrammingLanguage]
