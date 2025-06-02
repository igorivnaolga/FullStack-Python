#!venv/bin/python
import uvicorn

# TODO(Valerii Dyshlevyi): use click to parse command line arguments

if __name__ == "__main__":
    # settings = get_settings()
    uvicorn.run(
        app="api.app:fastapi_app",
        # host=self._args.host or settings.host,
        # port=self._args.port or settings.port,
        # reload=settings.debug or self._args.reload,
        reload=True,
    )


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/api/healthchecker")
# def root():
#     return {"message": "Welcome to FastAPI!"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="127.0.0.1", port=8000)
