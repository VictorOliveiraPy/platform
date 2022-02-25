import pytest
from starlette.testclient import TestClient

from config.config import app


class TestCreateUserForm:
    @pytest.fixture()
    def client(self):
        return TestClient(app)

    def test_create_user(self, client):

        payload = {
            "username": "victor",
            "email": "test@gmail.com",
            "password": "passtest",
        }
        result = client.post("/register", data=payload)
