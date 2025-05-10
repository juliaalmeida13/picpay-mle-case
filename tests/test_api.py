from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_load_model_with_invalid_file():
    response = client.post("/model/load/", files={
        "file": ("invalid.txt", b"not a pickle")
    })
    assert response.status_code == 400


def test_predict_without_model():
    payload = {
        "dep_delay": 30.0,
        "distance": 1000.0,
        "air_time": 120.0,
        "origin": 1,
        "destination": 2
    }
    response = client.post("/model/predict/", json=payload)
    assert response.status_code == 400
    assert "Modelo não carregado" in response.text
