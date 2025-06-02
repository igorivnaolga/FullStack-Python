from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from starlette import status

from api.dependencies import SessionLocal, get_db
from api.domain import Make, Model
from api.vehicles.schemas import (
    CreateUpdateMakeSchema,
    MakeSchema,
    MakesListSchema,
    ModelsListSchema,
)

router = APIRouter(tags=["vehicles"], prefix="/vehicles")


@router.get(
    path="/makes",
    summary="List of makes",
    response_model=MakesListSchema,
    status_code=status.HTTP_200_OK,
)
async def list_of_makes(
    limit: int = Query(default=2, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: SessionLocal = Depends(get_db),
) -> dict:
    """Return list of vehicle makes."""
    query = select(Make).limit(limit).offset(offset)
    result = db.execute(query)
    makes = result.scalars().all()
    return {"items": makes}


@router.get(
    path="/makes/{make_id}",
    summary="Retrieve a make",
    response_model=MakeSchema,
    status_code=status.HTTP_200_OK,
)
async def retrieve_make(
    make_id: int,
    db: SessionLocal = Depends(get_db),
) -> Make:
    """Retrieve a vehicle make."""
    query = select(Make).filter(Make.id == make_id)
    result = db.execute(query)
    make = result.scalar()
    if not make:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Make was not found",
        )
    return make


@router.post(
    path="/makes",
    summary="Create a new make",
    response_model=MakeSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_make(
    new_make_schema: CreateUpdateMakeSchema,
    db: SessionLocal = Depends(get_db),
) -> Make:
    """Create a vehicle make."""
    data = new_make_schema.model_dump()
    db_make = Make(**data)
    db.add(db_make)
    db.commit()
    db.refresh(db_make)
    return db_make


@router.patch(
    path="/makes/{make_id}",
    summary="Retrieve a make",
    response_model=MakeSchema,
    status_code=status.HTTP_200_OK,
)
async def partial_update_make(
    update_make_schema: CreateUpdateMakeSchema,
    make_id: int,
    db: SessionLocal = Depends(get_db),
) -> Make:
    """Retrieve a vehicle make."""
    query = select(Make).filter(Make.id == make_id)
    result = db.execute(query)
    db_make = result.scalar()
    if not db_make:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Make was not found",
        )

    # Update the fields
    # for key, value in update_make_schema.model_dump(exclude_unset=True).items():
    #     setattr(db_makemake, key, value)

    # Or just
    db_make.name = update_make_schema.name

    db.add(db_make)
    db.commit()
    db.refresh(db_make)
    return db_make


@router.get(
    path="/models",
    summary="List of models",
    response_model=ModelsListSchema,
    status_code=status.HTTP_200_OK,
)
async def list_of_models(
    limit: int = Query(default=2, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: SessionLocal = Depends(get_db),
) -> dict:
    """Return list of vehicle models."""
    query = (
        select(Model).join(Make, Make.id == Model.make_id).limit(limit).offset(offset)
    )
    result = db.execute(query)
    models = result.scalars().all()
    return {"items": models}
