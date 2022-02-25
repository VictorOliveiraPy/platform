from fastapi import APIRouter, HTTPException
from fastapi import Request

from config.config import templates
from src.core.apis.route_login import login_for_access_token
from src.core.repository.sqlalchemy.session import SessionMakerWrapper
from src.core.web_apps.auth.forms import LoginForm

router = APIRouter(include_in_schema=False)


@router.get("/login/")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
async def login(request: Request):
    with SessionMakerWrapper() as session:
        form = LoginForm(request)
        await form.load_data()

        if await form.is_valid():
            try:
                form.__dict__.update(msg="Login Successfull :)")
                response = templates.TemplateResponse("auth/login.html", form.__dict__)

                login_for_access_token(response=response, form_data=form)
                return response
            except HTTPException:
                form.__dict__.update(msg="")
                form.__dict__.get("erros").append("Incorrect email and password")
                return templates.TemplateResponse("auth/login.html", form.__dict__)
        return templates.TemplateResponse("auth/login.html", form.__dict__)