from services.document_processing import DocumentProcessor
from services import store

if __name__ == "__main__":
    processor = DocumentProcessor()
    documents = processor.process_documents("../data")

    store.ingest_documents(documents)
