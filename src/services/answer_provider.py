from collections.abc import AsyncGenerator

from langchain_openai import ChatOpenAI
from langchain_core.documents import Document



class AnswerProvider:
    PROMPT = """
    You are a specialized user assistant. You are an expert on answering questions on information about Deutsche Telecom.

    You will be provided with documents containing information about Deutsche Telecoms press releases and a question from the user.
    To answer the question, you can must only use information provided in the documents, you may not use any other information.
    In case you get no documents, just say you don't have enough information to answer the question.

    Documents:
    {documents}


    User question:
    {user_question}
    """

    def __init__(self, language_model: str):
        self.llm: ChatOpenAI = ChatOpenAI(model=language_model)

    async def _generate_tokens(self, filled_prompt: str) -> AsyncGenerator[str, None]:

        async for chunk in self.llm.astream(filled_prompt):
            yield f"data: {chunk.content}|"
        yield f"data: [DONE]|"

    async def provide_streamed_answers(self, user_question: str,  relevant_documents: list[Document]) -> AsyncGenerator[str, None]:
        filled_prompt = self.PROMPT.format(
            documents="\n".join([document.page_content for document in relevant_documents]),
            user_question=user_question,
        )

        async for token in self._generate_tokens(filled_prompt):
            yield token
