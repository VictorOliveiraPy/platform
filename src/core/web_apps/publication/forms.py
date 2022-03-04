from typing import List, Optional

from fastapi import Request
from fastapi_utils.enums import StrEnum


class PublicationCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.content_url: Optional[str] = None
        self.content_level: StrEnum = None

        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.content_url = form.get("content_url")
        self.content_level = form.get("content_level")
        self.description = form.get("description")

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.content_url or not (self.content_url.__contains__("http")):
            self.errors.append("Valid Url is required e.g. https://example.com")
        if not self.description or not len(self.description) >= 15:
            self.errors.append("Description too short")
        if not self.content_level:
            self.errors.append("choose content level")

        if not self.errors:
            return True
        return False
