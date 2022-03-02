class TestRetrievePublicationById:

    def test_retrieve_publication_by_id(self, client):
        id_: int = 1

        payload = {
                "title": "testando isso aqui",
                "content_url": "https://www.youtube.com/watch?v=qS1nP5oDjQY&list=RDhKQVzVdvq2E&index=6&ab_channel=L7NNON",
                "description": "testando essa description",
                "content_level": "INICIANTE"
            }

        result_post = client.post("/create_publication/", data=payload)
        result = client.get(f"/detail/1")
        assert result.status_code == 200

    def test_retrieve_return_status_code_not_found(self, client):
        id_: int = 100

        result = client.get(f"/detail/{id_}")

        assert result.status_code == 404
