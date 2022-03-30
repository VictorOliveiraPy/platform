from src.services.schemas.users import UserCreate


class TestTypingData:
    def test_passed_data_types(self):
        user = UserCreate(
            username="str",
            email="test@email.com",
            password="str"
        )
        assert user.email == "test@email.com"