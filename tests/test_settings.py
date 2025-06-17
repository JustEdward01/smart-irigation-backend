from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_export_config_valid_key():
    response = client.get("/api/settings/export-config", headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)

def test_import_config_invalid_key():
    # You would need a test file or JSON here for actual import testing
    # Just test response to invalid key:
    response = client.post("/api/settings/import-config", headers={"x-api-key": "invalid"})
    assert response.status_code == 403
