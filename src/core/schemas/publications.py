from datetime import datetime
from enum import auto
from typing import Optional

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel


class ContentLevel(StrEnum):
    INICIANTE = auto()
    INTERMEDIARIO = auto()
    AVANCADO = auto()


class PublicationBase(BaseModel):
    title: str
    content_url: str
    description: str
    date_posted: Optional[str] = datetime.now().date()
    content_level: ContentLevel


class PublicationCreate(PublicationBase):
    content_level: str
    pass
