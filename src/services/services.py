from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from services.document_store import DocumentStore
from services.answer_provider import AnswerProvider


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)

store = DocumentStore(vector_store=vector_store, embedding=embeddings)
llm = AnswerProvider("gpt-4.1-mini")
