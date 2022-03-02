from fastapi import APIRouter

from src.core.apis import route_login

api_router = APIRouter()

api_router.include_router(route_login.router, prefix="/users", tags=["users"])
