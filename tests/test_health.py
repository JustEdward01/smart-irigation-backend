from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_valid_key():
    response = client.get("/api/health", headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
    data = response.json()
    assert data["api_status"] == "ok"
    assert "database_status" in data

def test_health_invalid_key():
    response = client.get("/api/health", headers={"x-api-key": "invalid"})
    assert response.status_code == 403
