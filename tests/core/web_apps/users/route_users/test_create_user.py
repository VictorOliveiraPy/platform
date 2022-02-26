import pytest
from starlette.testclient import TestClient

from config.config import app


class TestCreateUserForm:
    def test_create_user(self, client):
        payload = {
            "username": "victor",
            "email": "test@gmail.com",
            "password": "passtest",
        }
        result = client.post("/register/", data=payload)

        assert result.status_code == 200


class TestCreateUserDuplicate:
    @pytest.fixture()
    def client(self):
        return TestClient(app)

    def test_create_user_duplicate(self, client):
        payload = None
        result = client.post("/register/", data=payload)
