import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    return TestClient(app)


class TestHealthCheck:
    def test_health_check_return_message_ok(self, client):
        response = client.get("/health-check/")

        assert response.json() == {"message": "OK"}

    def test_health_check_status_code_200(self, client):
        response = client.get("/health-check/")

        assert response.status_code == 200
