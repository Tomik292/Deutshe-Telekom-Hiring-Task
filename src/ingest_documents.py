from dependency_injector.wiring import inject, Provide

from services.document_processing import DocumentProcessor
from services.document_store import DocumentStore
from services.services import Container


@inject
def ingest_documents(
        processor: DocumentProcessor = Provide[Container.document_processor],
        store: DocumentStore = Provide[Container.document_store],
):
    documents = processor.process_documents()
    store.ingest_documents(documents)


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    ingest_documents()
