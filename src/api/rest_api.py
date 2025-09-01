import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, FileResponse
from pydantic import BaseModel

from services.services import store, llm

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")


class Input(BaseModel):
    question: str


@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("..", "static", "index.html"))


@app.post("/ask")
async def ask(user_input: Input) -> StreamingResponse:
    documents = await store.match_relevant_documents(user_input.question)

    return StreamingResponse(llm.provide_streamed_answers(user_input, documents), media_type="text/event-stream")
