class TestGetTemplates:
    def test_get_register(self, client):
        templates_result = client.get("/register/")

        assert templates_result.template.filename == "templates/users/register.html"