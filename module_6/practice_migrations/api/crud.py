from sqlalchemy import delete, select

from domain import User
from domain.connection import session
from domain.enums import UserRoles
from domain.users import EmployeeProfile


class EntityCruder:
    VALUE = 456

    def __init__(self):
        self.value = 321

    @staticmethod
    def list_users(**kwargs) -> None:
        print("Listing users kwargs:", kwargs)
        order_by = User.id.desc() if kwargs.get("order_by") == "desc" else User.id.asc()
        query = select(User).order_by(order_by)
        # print("query:", query)
        result = session.execute(query.order_by(order_by))
        scalars = result.scalars()
        all_users = scalars
        for user in all_users:
            print(
                user.id,
                user.email,
                user.role,
                user.first_name,
                user.last_name,
                user.profile.salary if user.role == UserRoles.EMPLOYEE else "",
            )

    @staticmethod
    def create_users(**kwargs) -> None:
        print("Creating user kwargs:", kwargs)
        user = User(email=kwargs["name"])
        session.add(user)
        session.commit()
        print(f"User {user.id} created successfully.")

    @staticmethod
    def update_users(**kwargs) -> None:
        print("Updating user kwargs:", kwargs)
        user_id = kwargs.get("entity_id")
        print(2, user_id)
        get_query = select(User).where(User.id == user_id)
        print("query:", get_query)
        result = session.execute(get_query)
        user = result.scalar()

        if not user:
            raise ValueError(f"User with ID={user_id} not found.")
        print(
            user.id,
            user.email,
            user.role,
            user.first_name,
            user.last_name,
            # user.employeeprofile.salary,
        )
        user.email = kwargs.get("name")
        session.add(user)
        session.commit()
        print(f"User {user.id} updated successfully.")

    @classmethod
    def do_something(cls):
        return cls.VALUE + 122

    @staticmethod
    def delete_users(**kwargs) -> None:
        print("Delete user kwargs:", kwargs)
        user_id = kwargs.get("entity_id")
        delete_query = delete(User).where(User.id == user_id)
        print("query:", delete_query)
        result = session.execute(delete_query)
        session.commit()
        print(f"User {user_id} deleted successfully.")

    @staticmethod
    def create_employee_profiles(**kwargs) -> None:
        print("Creating employee profile kwargs:", kwargs)
        profile = EmployeeProfile(salary=kwargs["name"], user_id=kwargs["entity_id"])
        session.add(profile)
        session.commit()
        print(f"Profile {profile.id} created successfully.")
