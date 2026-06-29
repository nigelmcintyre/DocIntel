from pathlib import Path

SUPPORTED_FILE_TYPES = {".pdf", ".docx", ".txt"}

def scan_files_in_directory(dir_path: str | Path) -> list[Path]:
    dir_path = Path(dir_path)
    files = [f for f in dir_path.rglob("*") if f.suffix in SUPPORTED_FILE_TYPES]
    return files

