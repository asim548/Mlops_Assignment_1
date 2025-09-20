import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # noqa: E402


def test_index():
    """Check if Flask app root (/) runs"""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


@pytest.fixture
def client():
    """Fixture for Flask test client"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to MLOps Assignment Flask API" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_predict_valid(client):
    response = client.post("/predict", json={"features": [1, 2, 3, 4]})
    assert response.status_code == 200
    data = response.get_json()
    assert "prediction" in data


def test_predict_invalid(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
