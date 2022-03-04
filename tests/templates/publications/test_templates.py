class TestPublicationGetTemplates:

    def test_get_front_page(self, client):
        templates_result = client.get("/")

        assert templates_result.template.filename == 'templates/frontpage.html'

    def test_get_create_publication(self, client):
        templates_result = client.get("/create_publication/")

        assert templates_result.template.filename == "templates/publications/create_publication.html"

    def test_get_detail_publication(self, client):
        templates_result = client.get("/detail/1/")

        assert templates_result.template.filename == "templates/publications/detail.html"

    def test_get_show_publications_to_delete(self, client):
        templates_result = client.get("/delete-publication/")

        assert templates_result.template.filename == "templates/publications/show_publications_to_delete.html"
