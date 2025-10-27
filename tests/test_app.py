import pytest
from app.main import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as c:
        yield c

def test_health_ok(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_ping_pong(client):
    r = client.get("/api/v1/ping")
    assert r.status_code == 200
    assert r.get_json()["message"] == "pong"
