"""
SYNAPSE HELIOS ID - Configuration & Architectural System Constants
"""
import os
from pydantic import BaseModel

class SystemSettings(BaseModel):
    app_name: str = "SYNAPSE HELIOS ID"
    app_version: str = "2026.10.4-PROD"
    environment: str = os.getenv("ENVIRONMENT", "production")
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    node_id: str = "NODE_01_JKT_COGNITION"
    default_model: str = "gemini-3-flash-preview"
    latency_target_ms: float = 18.4
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

settings = SystemSettings()
