from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .base import IDOrmModel
from .enums import UserRoles


class User(IDOrmModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    role: Mapped[UserRoles] = mapped_column(
        SQLAlchemyEnum(UserRoles),
        nullable=False,
        default=UserRoles.ADMIN.value,
        server_default=UserRoles.ADMIN.value,
    )

    profile = relationship("EmployeeProfile", back_populates="user", uselist=False)


class EmployeeProfile(IDOrmModel):
    __tablename__ = "employee_profiles"

    rank: Mapped[str] = mapped_column(String(30), nullable=False)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship("User", back_populates="profile", uselist=False)
