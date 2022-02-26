import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ContentLevel(str, enum.Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIARY = "INTERMEDIARY"
    ADVANCING = "ADVANCING"


class PublicationBase(BaseModel):
    title: str
    content_url: str
    description: str
    date_posted: Optional[str] = datetime.now().date()
    content_level: ContentLevel


class PublicationCreate(PublicationBase):
    pass
