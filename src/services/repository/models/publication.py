from enum import auto

from fastapi_utils.enums import StrEnum
from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String

from src.services.repository.sqlalchemy.base_class import Base


class ContentLevel(StrEnum):
    INICIANTE = auto()
    INTERMEDIARIO = auto()
    AVANCADO = auto()


class Publication(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content_url = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    content_level = Column(Enum(ContentLevel))
    owner_id = Column(Integer, ForeignKey("user.id"))
