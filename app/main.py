from pathlib import Path
from app.scanner import scan_files_in_directory
from app.extractor import extract_metadata, extract_text
from app.index import DocumentIndex
from sys import argv

def main():
    doc_index = DocumentIndex()

    files = scan_files_in_directory(Path(__file__).parent.parent / "data")

    for file_path in files:
        try:
            metadata = extract_metadata(file_path)
            text = extract_text(file_path)
            doc_index.add_document(metadata, text)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    query = argv[1] if len(argv) > 1 else "example"
    results = doc_index.search(query)

    print(f"Found {len(files)} files")

    print(f"Search results for '{query}':")
    for result in results:
        print(f"- {result.name} ({result.file_type}) at {result.path}")

if __name__ == "__main__":
    main()