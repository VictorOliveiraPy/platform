from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from config.config import templates
from config.hashing import Hasher
from config.security import create_access_token
from src.core.repository.sqlalchemy.session import SessionMakerWrapper
from src.core.repository.sqlalchemy.users.login import \
    SqlAlchemyPublicationRepository

router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
def login(request: OAuth2PasswordRequestForm = Depends()):
    with SessionMakerWrapper() as session:
        user = SqlAlchemyPublicationRepository(session).get_user(request.username)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Invalid credentials'
            )

        if not Hasher.verify_password(user.hashed_password, request.password):
            raise InvalidCredentialsException

        access_token = create_access_token(data={'username': user.username})

