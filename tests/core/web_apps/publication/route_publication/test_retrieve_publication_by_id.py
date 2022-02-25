import pytest
from starlette.testclient import TestClient

from config.config import app


class TestRetrievePublicationById:
    @pytest.fixture()
    def client(self):
        return TestClient(app)

    def test_retrieve_publication_by_id(self, client):
        id_: int = 2

        result = client.get(f"/detail/{id_}")
        assert result.status_code == 200

    def test_retrieve_return_status_code_not_found(self, client):
        id_: int = 100

        result = client.get(f"/detail/{id_}")

        assert result.status_code == 404
