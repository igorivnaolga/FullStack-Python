from domain.users import User
from domain.users import Post

print("I am in __init__.py")
__all__ = ["User", "Post"]

print("__all__ was defined")
