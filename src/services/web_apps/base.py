from fastapi import APIRouter

from src.services.web_apps.auth import route_login
from src.services.web_apps.publication import route_publications
from src.services.web_apps.users import route_users

api_router = APIRouter()

api_router.include_router(route_publications.router, prefix="", tags=["home-page"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(route_login.router, prefix="", tags=["auth"])

