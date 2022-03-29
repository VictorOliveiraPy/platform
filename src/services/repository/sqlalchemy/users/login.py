from src.services.repository.models.users import User
from src.services.repository.sqlalchemy.users.abstract import AbstractRepository


class SqlAlchemyPublicationRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def get_user(self, username: str):
        return self.session.query(User).filter(User.email == username).first()
