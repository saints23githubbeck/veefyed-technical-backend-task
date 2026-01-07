from pathlib import Path
from fastapi import UploadFile

from app.config import ALLOWED_EXTENSIONS, MAX_FILE_SIZE
from app.utils.exceptions import InvalidFileTypeError, FileTooLargeError


def validate_image(file: UploadFile) -> None:
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise InvalidFileTypeError()

    file.file.seek(0, 2)           # go to end
    size = file.file.tell()
    file.file.seek(0)              # reset cursor

    if size > MAX_FILE_SIZE:
        raise FileTooLargeError()