import os

from dependency_injector import containers, providers

from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from services.document_processing import DocumentProcessor
from services.document_store import DocumentStore
from services.answer_provider import AnswerProvider


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_yaml(os.path.join("config.yaml"))

    document_processor = providers.Factory(
        DocumentProcessor,
        path_to_documents=config.documents_path,
    )

    embeddings = providers.Singleton(
        HuggingFaceEmbeddings,
        model_name=config.embedding_model_name,
        )

    vector_store = providers.Singleton(
        Chroma,
        collection_name=config.vector_store.index_name,
        embedding_function=embeddings,
        persist_directory=config.vector_store.storage_path
    )

    document_store = providers.Factory(
        DocumentStore,
        vector_store=vector_store,
        embedding=embeddings,
    )

    llm = providers.Factory(
        AnswerProvider,
        language_model=config.language_model_name,
    )

    wiring = containers.WiringConfiguration(modules=[
        "api.rest_api"
    ])
