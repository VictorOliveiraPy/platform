from sqlalchemy.orm import Session

from src.core.repository.models.publication import Publication
from src.core.repository.sqlalchemy.publications.abstract import \
    AbstractRepository
from src.core.schemas.publications import PublicationCreate


class SqlAlchemyPublicationRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id_publication) -> Publication:
        return (
            self.session.query(Publication)
                .filter(Publication.id == id_publication)
                .first()
        )

    def get(self) -> Publication:
        return self.session.query(Publication).filter(Publication.is_active == True).all()

    def post(self, publication: PublicationCreate, owner_id) -> PublicationCreate:
        publication = Publication(**publication.dict(), owner_id=owner_id)
        self.session.add(publication)
        self.session.commit()
        self.session.refresh(publication)
        return publication


def update_publication_by_id(
        id: int, publication: PublicationCreate, db: Session, owner_id: int
):
    existing_publication = db.query(Publication).filter(Publication.id == id)
    if not existing_publication.first():
        return 0

    publication.__dict__.update(owner_id=owner_id)
    existing_publication.update(publication.__dict__)
    db.commit()
    return 1


def delete_publication_by_id(id: int, db: Session, owner_id: int):
    existing_job = db.query(Publication).filter(Publication.id == id)
    if not existing_job.first():
        return 0

    existing_job.delete(synchronize_session=False)
    db.commit()
    return 1
