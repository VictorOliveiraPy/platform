import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


class TestHomePage:
    def test_return_status_code_200(self, client):
        response = client.get("/")
        assert response.status_code == 200
