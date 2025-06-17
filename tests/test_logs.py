from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_export_logs_valid_key():
    response = client.get("/api/logs/export", headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
