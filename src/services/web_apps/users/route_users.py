from fastapi import APIRouter, Request, responses, status
from sqlalchemy.exc import IntegrityError

from config.config import templates
from src.services.repository.sqlalchemy.session import SessionMakerWrapper
from src.services.repository.sqlalchemy.users.users import \
    SqlAlchemyPublicationRepositoryUsers
from src.services.schemas.users import UserCreate
from src.services.web_apps.users.forms import UserCreateForm

router = APIRouter(include_in_schema=False)


@router.get("/register/")
def register(request: Request):
    return templates.TemplateResponse("users/register.html", {"request": request})


@router.post("/register/")
async def register(request: Request):
    with SessionMakerWrapper() as session:
        form = UserCreateForm(request)
        await form.load_data()

        if await form.is_valid():
            user = UserCreate(username=form.username, email=form.email, password=form.password)
            try:
                user = SqlAlchemyPublicationRepositoryUsers(session).post(user=user)
                return responses.RedirectResponse("/?msg=Succesfully-Registered", status_code=status.HTTP_302_FOUND)
            except IntegrityError:
                form.__dict__.get("errors").append("Duplicate username or email")
                return templates.TemplateResponse("users/register.html", form.__dict__)
        return templates.TemplateResponse("users/register.html", form.__dict__, status_code=201)

