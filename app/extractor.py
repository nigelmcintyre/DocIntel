from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
from pypdf import PdfReader
from docx import Document

class DocumentMetadata(BaseModel):
    path: Path
    name: str
    file_type: str
    size: int
    created_date: datetime
    modified_date: datetime


def extract_metadata(file_path: str | Path) -> DocumentMetadata:
    path = Path(file_path)
    stat = path.stat()
    return DocumentMetadata(
        path = path,
        name = path.name,
        file_type = path.suffix,
        size = stat.st_size,
        created_date = datetime.fromtimestamp(stat.st_ctime),
        modified_date = datetime.fromtimestamp(stat.st_mtime)
    )

def extract_text(file_path: Path) -> str:
    if file_path.suffix == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_path.suffix == ".docx":
        return extract_text_from_docx(file_path)
    elif file_path.suffix == ".txt":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")
    
def extract_text_from_pdf(file_path: Path) -> str:
    reader = PdfReader(file_path)
    pages = [page.extract_text() for page in reader.pages]
    return "\n".join(pages)

def extract_text_from_docx(file_path: Path) -> str:
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    return "\n".join(paragraphs)

def extract_text_from_txt(file_path: Path) -> str:
    with open(file_path, 'r') as f:
        return f.read()
