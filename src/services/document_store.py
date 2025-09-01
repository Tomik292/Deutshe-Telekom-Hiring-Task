import uuid

from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class DocumentStore:
    def __init__(self, vector_store: VectorStore, embedding: Embeddings):
        self.vector_store = vector_store
        self.embedding = embedding

    def ingest_documents(self, documents: list[Document]):
        self.vector_store.add_documents(documents, ids=[str(uuid.uuid4()) for _ in documents])

    async def match_relevant_documents(self, user_query: str) -> list[Document]:
        return await self.vector_store.asimilarity_search(user_query, k=5)
