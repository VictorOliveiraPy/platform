from src.services.schemas.publications import PublicationCreate


class TestTypingData:
    def test_typing_publication_schemas(self):

        publication = PublicationCreate(
            title="test title",
            content_url="https://www.youtube.com/watch?v=NoXp9aNANTc&ab_channel=McPozedoRodo-Topic",
            description="test de description",
            content_level='INICIANTE'
        )

        assert publication.title == 'test title'
        assert publication.content_level == 'INICIANTE'