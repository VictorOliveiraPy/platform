class TestRetrievePublicationById:
    def test_when_status_code_return_not_found(self, client):
        id_: int = 100

        result = client.get(f"/detail/{id_}")

        assert result.status_code == 404
