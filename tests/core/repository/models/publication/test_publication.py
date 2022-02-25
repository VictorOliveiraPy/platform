from src.core.repository.models.publication import Publication


class TestPublicationattributes:
    def test_attributes_model(self):
        publication = Publication(
            title="testando title",
            content_url="https://www.youtube.com/watch?v=iDJM3HTdjck&ab_channel=30PRAUM",
            description="testando a descricao"
        )

        assert publication.title == 'testando title'
