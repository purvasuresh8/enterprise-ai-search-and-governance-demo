from pathlib import Path

DOCUMENT_FOLDER = (
    Path(__file__)
    .parent.parent
    .joinpath("data", "sample_documents")
)


class SearchEngine:
    def __init__(self):
        self.documents = self._load_documents()

    def _load_documents(self):
        documents = []

        if not DOCUMENT_FOLDER.exists():
            return documents

        for file in DOCUMENT_FOLDER.glob("*.txt"):
            documents.append(
                {
                    "filename": file.name,
                    "content": file.read_text(encoding="utf-8")
                }
            )

        return documents

    def search(self, query):
        query = query.lower()

        matches = []

        for document in self.documents:
            if query in document["content"].lower():
                matches.append(
                    {
                        "filename": document["filename"],
                        "snippet": document["content"][:250]
                    }
                )

        return matches
