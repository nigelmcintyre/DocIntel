from app.extractor import DocumentMetadata

class DocumentIndex():
    def __init__(self):
        self.index: dict[str, set[str]] = {}
        self.documents: dict[str, DocumentMetadata] = {}

    def add_document(self, metadata: DocumentMetadata, text: str):
        if str(metadata.path) not in self.documents:
            self.documents[str(metadata.path)] = metadata
        for word in text.split():
            word = word.lower()
            self.index.setdefault(word, set()).add(str(metadata.path))

    def search(self, query:str) -> list[DocumentMetadata]:
        if not query:
            return []
        words = query.lower().split()
        result_paths = self.index.get(words[0], set())
        for word in words[1:]:
            result_paths = result_paths.intersection(self.index.get(word, set()))
        return sorted([self.documents[path] for path in result_paths], key=lambda x: x.name)