"""
SYNAPSE HELIOS ID - API & Endpoint Unit & Integration Tests
"""
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_health_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "HEALTHY"
        assert "SYNAPSE HELIOS ID" in data["system"]

@pytest.mark.asyncio
async def test_ai_types_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/ai-types")
        assert response.status_code == 200
        data = response.json()
        assert data["total_categories"] == 6
        assert len(data["categories"]) == 6
        
        # Check category structure
        cat_ids = [c["id"] for c in data["categories"]]
        assert "reasoning-test-time" in cat_ids
        assert "omni-modal-frontier" in cat_ids
        assert "autonomous-agentic" in cat_ids
        assert "generative-media-world" in cat_ids
        assert "architectural-foundations" in cat_ids
        assert "narrow-ai-to-agi" in cat_ids

@pytest.mark.asyncio
async def test_languages_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/languages")
        assert response.status_code == 200
        data = response.json()
        assert data["total_languages"] == 7
        lang_ids = [l["id"] for l in data["languages"]]
        
        expected = ["python", "typescript-javascript", "cplusplus-cuda", "rust", "mojo", "golang", "julia"]
        for exp in expected:
            assert exp in lang_ids
            
        # Verify SVG logo presence
        for l in data["languages"]:
            assert "logo_url" in l
            assert l["logo_url"].startswith("http")

@pytest.mark.asyncio
async def test_terminal_modes_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        for mode in ["creative", "code", "analysis"]:
            payload = {
                "query": "Jelaskan arsitektur reasoning models dan penskalaan test-time compute.",
                "mode": mode,
                "client_id": "TEST_SUITE"
            }
            response = await client.post("/api/terminal", json=payload)
            assert response.status_code == 200
            data = response.json()
            assert data["status"] == "SUCCESS"
            assert data["mode"] == mode
            assert len(data["response"]) > 20
            assert data["tokens_estimated"] > 0
