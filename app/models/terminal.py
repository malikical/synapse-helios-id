"""
SYNAPSE HELIOS ID - Interactive Terminal Query & Response Schemas
"""
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field

class TerminalQueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=4000, description="User prompt or technical inquiry")
    mode: str = Field("creative", description="Mode: 'creative' | 'code' | 'analysis'")
    client_id: Optional[str] = "SYNAPSE_WEB_CLIENT"
    context: Optional[Dict[str, Any]] = None

class TerminalQueryResponse(BaseModel):
    status: str = "SUCCESS"
    mode: str
    query: str
    response: str
    tokens_estimated: int
    latency_ms: float
    model_used: str
    timestamp: str
    source: str = "SYNAPSE_COGNITIVE_MATRIX"
    telemetry: Dict[str, Any] = {}
