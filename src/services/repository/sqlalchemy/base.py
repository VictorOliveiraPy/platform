from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config.config import settings

engine = create_engine(
    settings.DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)

Base = declarative_base()

