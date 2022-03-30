from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

from src.config.config import templates
from src.services.apis.route_login import login_for_access_token
from src.services.repository.sqlalchemy.session import SessionMakerWrapper
from src.services.web_apps.auth.forms import LoginForm

router = APIRouter()


@router.get("/login/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login/")
async def login(request: Request):
    with SessionMakerWrapper() as session:
        form = LoginForm(request)
        await form.load_data()

        if await form.is_valid():
            try:
                form.__dict__.update(msg="Login Successful :)")
                response = templates.TemplateResponse("auth/login.html", form.__dict__)
                login_for_access_token(response=response, form_data=form)
                return response

            except HTTPException:
                form.__dict__.update(msg="")
                form.__dict__.get("errors").append("Incorrect email or password")

                return templates.TemplateResponse("auth/login.html", form.__dict__)
        return templates.TemplateResponse("auth/login.html", form.__dict__)
