from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_wifi_status_valid_key():
    response = client.get("/api/wifi/status", headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
    data = response.json()
    assert "connected" in data or "disconnected" in data

def test_wifi_reset_valid_key():
    response = client.post("/api/wifi/reset", headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
