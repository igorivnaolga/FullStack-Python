from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.config import get_settings

settings = get_settings()
Base: type = declarative_base()
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(settings.database_uri),  # type: ignore
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
