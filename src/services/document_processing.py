import os

from langchain_core.documents import Document


class DocumentProcessor:
    documents = []

    def __init__(self, path_to_documents: str):
        self.documents_path: str = path_to_documents

    def process_documents(self,) -> list[Document]:
        for file in os.listdir(self.documents_path):
            if file.endswith(".txt"):
                with open(os.path.join(self.documents_path, file), "r") as f:
                    file_text = f.read()
                    self.documents.append(Document(file_text))

        return self.documents

