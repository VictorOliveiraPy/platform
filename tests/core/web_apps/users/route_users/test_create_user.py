import pytest
from starlette.testclient import TestClient

from config.config import app


class TestCreateUserForm:
    def test_create_user(self, client):
        payload = {
            "username": "hugo",
            "email": "test@gmail.com",
            "password": "passtest",
        }
        result = client.post("/register/", data=payload)

        assert result.status_code == 201

