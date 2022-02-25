from src.core.repository.models.users import User


class TestUserAttributes:
    def test_attributes_model(self):

        user = User(
            username='test de user',
            email='victor@test.com.br',
            hashed_password='234234234'
        )

        assert user.username == "test de user"