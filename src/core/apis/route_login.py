from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt

from config.config import settings
from config.hashing import Hasher
from config.security import create_access_token
from src.core.apis.utils import OAuth2PasswordBearerWithCookie
from src.core.repository.sqlalchemy.session import SessionMakerWrapper
from src.core.repository.sqlalchemy.users.login import \
    SqlAlchemyPublicationRepository

router = APIRouter()


def authenticate_user(username: str, password: str):
    with SessionMakerWrapper() as session:
        user = SqlAlchemyPublicationRepository(session).get_user(username=username)

        if not user:
            return False
        if not Hasher.verify_password(password, user.hashed_password):
            return False
        return user


@router.post("/token")
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    with SessionMakerWrapper() as session:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )

        access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expire)
        response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)

        return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")


def get_current_user_from_token(token: str = Depends(oauth2_scheme)):
    with SessionMakerWrapper() as session:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = SqlAlchemyPublicationRepository(session).get_user(username=username)
        if user is None:
            raise credentials_exception
        return user
