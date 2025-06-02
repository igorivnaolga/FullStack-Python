from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy import text
from starlette import status

from api.dependencies import SessionLocal, get_db
from api.root.schemas import HealthCheckSchema

router = APIRouter(tags=["infrastructure"])


@router.get(
    path="/healthcheck",
    summary="Health check",
    response_model=HealthCheckSchema,
    status_code=status.HTTP_200_OK,
)
async def healthcheck(db: SessionLocal = Depends(get_db)) -> dict:
    """Healthcheck endpoint for infrastructure monitoring."""
    result = db.execute(text("SELECT 1")).fetchone()
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database is not configured correctly",
        )
    return {"result": "success"}
