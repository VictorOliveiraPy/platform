import random
import string

from _pytest.tmpdir import get_user
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.services.repository.sqlalchemy.users.users import \
    SqlAlchemyPublicationRepositoryUsers
from src.services.schemas.users import UserCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_owner(db: Session):
    email: str = f"{random_lower_string()}@{random_lower_string()}.com"
    password: str = random_lower_string()
    user_schema: UserCreate = UserCreate(username=email, email=email, password=password)
    user = SqlAlchemyPublicationRepositoryUsers().post(user=user_schema, db=db)
    return user


def user_authentication_headers(client: TestClient, email: str, password: str):
    data = {"username": email, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers


def authentication_token_from_email(client: TestClient, email: str, db: Session):
    """
    Return a valid token for the user with given email.
    If the user doesn't exist it is created first.
    """
    password = "random-passW0rd"
    user = get_user(username=email, db=db)
    if not user:
        user_in_create = UserCreate(username=email, email=email, password=password)
        user = create_new_user(user=user_in_create, db=db)
    return user_authentication_headers(client=client, email=email, password=password)
