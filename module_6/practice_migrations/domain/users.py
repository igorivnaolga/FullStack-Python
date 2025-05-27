from typing import Any

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import ForeignKey, Numeric, String, exists, select
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    validates,
)

from .base import IDOrmModel
from .connection import session
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

    salary: Mapped[str] = mapped_column(
        Numeric(10, 2), default=0, server_default="0.00"
    )
    user_id = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)

    user = relationship("User", back_populates="profile", uselist=False)

    @validates("user_id")
    def validate_user_id(self, key, user_id: Any) -> int:
        print("validate_user_id", key, user_id)
        user_id = int(user_id)  # convert to int
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer.")
        profile_exists_query = select(exists().where(EmployeeProfile.id == user_id))
        print(profile_exists_query)
        result = session.execute(profile_exists_query)
        profile_exists = bool(result.scalar())
        if profile_exists:
            raise ValueError(f"EmployeeProfile with ID={user_id} already exists.")
        return user_id


class Post(IDOrmModel):
    __tablename__ = "posts"

    first_name: Mapped[str] = mapped_column(String(150), nullable=False)
