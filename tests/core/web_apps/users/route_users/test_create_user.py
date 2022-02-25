

class TestCreateUserForm:
    def test_create_user(self, client):

        payload = {
            "username": "victor",
            "email": "test@gmail.com",
            "password": "passtest",
        }
        result = client.post("/register/", data=payload)

        assert result.status_code == 200
