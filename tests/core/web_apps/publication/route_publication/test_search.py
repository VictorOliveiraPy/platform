import pytest
from starlette.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


class TestSearchTitle:
    def test_search(self, client):
        query_result = client.get("/search/?query=Python")

        assert query_result.status_code == 200
