import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import rest_api
from services.services import Container


def create_app() -> FastAPI:
    container = Container()
    container.init_resources()
    container.wire(modules=[rest_api])
    container.embeddings()
    container.vector_store()

    app = FastAPI()
    app.container = container
    app.mount("/static", StaticFiles(directory="../static"), name="static")
    app.include_router(rest_api.router)
    return app


api = create_app()

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
