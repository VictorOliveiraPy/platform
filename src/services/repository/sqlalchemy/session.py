from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from config.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class SessionMakerWrapper(object):
    session: Session = None

    def __init__(self) -> None:
        self.session: Session = SessionLocal()

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
