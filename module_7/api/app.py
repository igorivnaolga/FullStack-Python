from collections.abc import Callable
from datetime import UTC, datetime

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from api.routes import register_routes

fastapi_app = FastAPI(title="Lecture #7", version="0.1.0")
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")


@fastapi_app.middleware("http")
async def add_process_time_header(request: Request, call_next: Callable):
    start_time = datetime.now(tz=UTC)
    response = await call_next(request)
    process_time = datetime.now(tz=UTC) - start_time
    print("Process time: ", process_time)
    response.headers["X-Process-Time"] = str(process_time)
    return response


register_routes(fastapi_app=fastapi_app)


# TODO(Valerii Dyshlevyi): healthcheck endpoint should do requrest to the database
# TODO(Valerii Dyshlevyi): use postgresql as a database
