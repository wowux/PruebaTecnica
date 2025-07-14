import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_subscribe_success():
    response = client.post("/subscribe/1?user_id=123")
    assert response.status_code == 200