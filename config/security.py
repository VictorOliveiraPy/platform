from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form

from config.config import settings
from config.hashing import Hasher
from src.core.apis.route_login import router
from src.core.repository.sqlalchemy.session import SessionMakerWrapper
from src.core.repository.sqlalchemy.users.login import SqlAlchemyPublicationRepository


@router.post("/token")
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    with SessionMakerWrapper() as session:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            return False
        token_expires = timedelta(minutes=60)
        token = create_access_token(
            user.username,
            user.id,
            expires_delta=token_expires
        )

        response.set_cookie(key="access_token", value=token, httponly=True)

        return True


def authenticate_user(username: str, password: str):
    with SessionMakerWrapper() as session:
        user = SqlAlchemyPublicationRepository(session).get_user(username)

        if not user:
            return False
        if not Hasher.verify_password(password, user.hashed_password):
            return False
        return user


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    encode.update({"exp": expire})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
