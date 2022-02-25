from src.core.schemas.users import UserCreate


class TestTypingData:
    def test_typing_users_schemas(self):
        user = UserCreate(
            username="str",
            email="test@email.com",
            password="str"
        )
        assert user.email == "test@email.com"