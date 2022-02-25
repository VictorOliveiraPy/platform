import enum

from sqlalchemy import Boolean, Column, Date, Enum, ForeignKey, Integer, String

from src.core.repository.sqlalchemy.base_class import Base


class ContentLevel(str, enum.Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIARY = "INTERMEDIARY"
    ADVANCING = "ADVANCING"


class Publication(Base):

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content_url = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    content_level = Column(Enum(ContentLevel))
    owner_id = Column(Integer, ForeignKey("user.id"))
