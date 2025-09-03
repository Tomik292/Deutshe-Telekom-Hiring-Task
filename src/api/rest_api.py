import os
from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter
from fastapi.responses import StreamingResponse, FileResponse
from pydantic import BaseModel

from services.answer_provider import AnswerProvider
from services.document_store import DocumentStore
from services.services import Container

router = APIRouter()


class Input(BaseModel):
    question: str


@router.get("/")
async def serve_index() -> FileResponse:
    return FileResponse(os.path.join("..", "static", "index.html"))


@router.post("/ask")
@inject
async def ask(
        store: Annotated[DocumentStore, Depends(Provide[Container.document_store])],
        llm: Annotated[AnswerProvider, Depends(Provide[Container.llm])],
        user_input: Input,
) -> StreamingResponse:
    documents = await store.match_relevant_documents(user_input.question)

    return StreamingResponse(llm.provide_streamed_answers(user_input.question, documents), media_type="text/event-stream")
