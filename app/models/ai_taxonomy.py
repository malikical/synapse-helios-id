"""
SYNAPSE HELIOS ID - AI Taxonomy Pydantic Schemas
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class BenchmarkMetric(BaseModel):
    name: str
    score: str
    baseline: Optional[str] = None
    description: str

class ArchitecturalFeature(BaseModel):
    title: str
    detail: str
    code_or_formula: Optional[str] = None

class AITypeItem(BaseModel):
    id: str
    category_id: str
    title: str
    tagline: str
    badge: str
    description: str
    deep_dive: str
    key_mechanisms: List[str]
    pioneer_models: List[str]
    architectural_features: List[ArchitecturalFeature]
    benchmarks: List[BenchmarkMetric]
    computational_complexity: str
    hardware_affinity: str
    use_cases: List[str]
    risk_and_alignment: str

class AICategory(BaseModel):
    id: str
    numeral: str
    name: str
    english_name: str
    tagline: str
    overview: str
    paradigm_shift: str
    items: List[AITypeItem]

class TaxonomyResponse(BaseModel):
    system: str = "SYNAPSE HELIOS ID"
    status: str = "OPERATIONAL"
    total_categories: int
    total_types: int
    categories: List[AICategory]
