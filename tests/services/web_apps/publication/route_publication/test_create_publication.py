class TestCreatePublication:
    def status_code_when_creating_a_post(self, client):
        payload = {
            "title": "testando isso aqui",
            "content_url": "https://www.youtube.com/watch?v=qS1nP5oDjQY&list=RDhKQVzVdvq2E&index=6&ab_channel=L7NNON",
            "description": "testando essa description",
            "content_level": "INICIANTE"
        }

        result = client.post("/create_publication/", data=payload)

        assert result.status_code == 201
