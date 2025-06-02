from fastapi import APIRouter, FastAPI

from api.root.views import router as root_router
from api.vehicles.views import router as vehicle_router


def register_routes(fastapi_app: FastAPI):
    """Function to register all API routers in one place."""
    v1_router = APIRouter(prefix="/api/v1")
    v1_router.include_router(vehicle_router)

    # main level
    fastapi_app.include_router(root_router)
    fastapi_app.include_router(v1_router)
