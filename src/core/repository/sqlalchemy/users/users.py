from abc import ABC

from config.hashing import Hasher
from src.core.repository.models.users import User
from src.core.repository.sqlalchemy.users.abstract import AbstractRepositoryUser
from src.core.schemas.users import UserCreate


class SqlAlchemyPublicationRepositoryUsers(AbstractRepositoryUser, ABC):
    def __init__(self, session):
        self.session = session

    def post(self, user: UserCreate) -> UserCreate:
        user = User(
            username=user.username,
            email=user.email,
            hashed_password=Hasher.get_password_hash(user.password),
            is_active=True,
            is_superuser=False,
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
