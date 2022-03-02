from config.config import app
from src.core.apis.base import api_router as api
from src.core.repository.sqlalchemy.base_class import Base
from src.core.repository.sqlalchemy.session import engine
from src.core.web_apps.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api)
    app.include_router(api_router)


def start_application():
    create_tables()
    include_router(app)
    return app


test = start_application()


@app.get("/health-check/")
def health_check():
    return {"message": "OK"}
