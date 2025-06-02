from pydantic import BaseModel


class CreateUpdateMakeSchema(BaseModel):
    name: str


class MakeSchema(BaseModel):
    id: int
    name: str


class MakesListSchema(BaseModel):
    items: list[MakeSchema]


class ModelSchema(BaseModel):
    id: int
    name: str
    rating: int
    make_id: int
    make: MakeSchema


class ModelsListSchema(BaseModel):
    items: list[ModelSchema]
