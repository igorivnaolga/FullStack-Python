from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import IDOrmModel


class Make(IDOrmModel):
    __tablename__ = "makes"

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    # Relationship
    models = relationship("Model", back_populates="make")


class Model(IDOrmModel):
    __tablename__ = "models"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float] = mapped_column(Integer)
    make_id = mapped_column(ForeignKey("makes.id"), nullable=False)

    # Relationship
    make = relationship("Make", back_populates="models")
