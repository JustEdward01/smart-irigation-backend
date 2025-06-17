from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_valid():
    payload = {
        "plant_type": "rosie",
        "soil_moisture": 50,
        "temperature": 25,
        "air_humidity": 60,
        "light": 5000,
        "last_watered_days": 1,
        "ml_prediction_prev": 0.5
    }
    response = client.post("/api/predict", json=payload, headers={"x-api-key": "supersecret123"})
    assert response.status_code == 200
    data = response.json()
    assert "water_given_ml" in data
    assert "next_watering_days" in data

def test_predict_invalid_soil_moisture():
    payload = {
        "plant_type": "rosie",
        "soil_moisture": 150,  # invalid > 100
        "temperature": 25,
        "air_humidity": 60,
        "light": 5000,
        "last_watered_days": 1,
        "ml_prediction_prev": 0.5
    }
    response = client.post("/api/predict", json=payload, headers={"x-api-key": "supersecret123"})
    assert response.status_code == 422  # validation error
