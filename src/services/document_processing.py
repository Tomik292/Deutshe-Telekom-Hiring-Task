import os

from langchain_core.documents import Document


class DocumentProcessor:
    documents = []

    def process_documents(self, document_path: str) -> list[Document]:
        for file in os.listdir(document_path):
            if file.endswith(".txt"):
                with open(os.path.join(document_path, file), "r") as f:
                    file_text = f.read()
                    self.documents.append(Document(file_text))

        return self.documents

