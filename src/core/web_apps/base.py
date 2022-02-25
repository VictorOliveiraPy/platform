from fastapi import APIRouter

from src.core.web_apps.publication import route_publications
from src.core.web_apps.users import route_users
from src.core.web_apps.auth import route_login

api_router = APIRouter()

api_router.include_router(route_publications.router, prefix="", tags=["home-page"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["auth"])

