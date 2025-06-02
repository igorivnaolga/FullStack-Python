from pydantic import BaseModel


class HealthCheckSchema(BaseModel):
    result: str
