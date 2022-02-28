class TestGetLogin:
    def test_template_login(self, client):
        templates_result = client.get("/login/")

        assert templates_result.template.filename == "templates/auth/login.html"