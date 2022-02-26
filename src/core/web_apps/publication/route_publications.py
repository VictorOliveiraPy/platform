from fastapi import APIRouter, HTTPException, Request, responses, status
from fastapi.responses import HTMLResponse
from fastapi.security.utils import get_authorization_scheme_param

from config.config import templates
from src.core.apis.route_login import get_current_user_from_token
from src.core.repository.models.users import User
from src.core.repository.sqlalchemy.publications.publication import \
    SqlAlchemyPublicationRepository
from src.core.repository.sqlalchemy.session import SessionMakerWrapper
from src.core.schemas.publications import PublicationCreate
from src.core.web_apps.publication.forms import PublicationCreateForm

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home_page(request: Request, msg: str = None):
    with SessionMakerWrapper() as session:
        repository = SqlAlchemyPublicationRepository(session)
        publication = repository.get()

        return templates.TemplateResponse(
            "frontpage.html", {"request": request, "publications": publication, "msg": msg}
        )


@router.get("/create_publication/")
def create_publication(request: Request):
    return templates.TemplateResponse("publications/create_publication.html", {"request": request})


@router.post("/create_publication/")
async def create_publication(request: Request):
    with SessionMakerWrapper() as session:
        form = PublicationCreateForm(request)
        await form.load_data()

        if form.is_valid():
            publication = PublicationCreate(**form.__dict__)
            repository = SqlAlchemyPublicationRepository(session)

            publication = repository.post(publication=publication)

            return responses.RedirectResponse(
                f"/detail/{publication.id}", status_code=status.HTTP_302_FOUND
            )
        return templates.TemplateResponse("publications/create_publication.html", form.__dict__)


@router.get("/detail/{id_publication}")
def publication_detail(id_publication: int, request: Request):
    with SessionMakerWrapper() as session:
        repository = SqlAlchemyPublicationRepository(session)
        publication = repository.get_by_id(id_publication)

        if not publication:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Publication ID {id_publication} not found.",
            )
    return templates.TemplateResponse(
        "publications/detail.html", {"request": request, "publications": publication}
    )


@router.get("/delete-publication/")
def show_publication_to_delete(request: Request):
    with SessionMakerWrapper() as session:
        repository = SqlAlchemyPublicationRepository(session)
        publication = repository.get()

        return templates.TemplateResponse(
            "publications/show_publications_to_delete.html", {
                "request": request,
                "publications": publication
            }
        )
