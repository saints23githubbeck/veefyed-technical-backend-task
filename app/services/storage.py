import uuid
from pathlib import Path

from fastapi import UploadFile

from app.config import UPLOAD_DIR


def generate_image_id() -> str:
    return uuid.uuid4().hex[:12]


def save_image(file: UploadFile, image_id: str) -> Path:
    extension = Path(file.filename).suffix
    file_path = UPLOAD_DIR / f"{image_id}{extension}"

    with file_path.open("wb") as f:
        f.write(file.file.read())

    return file_path


def image_exists(image_id: str) -> bool:
    for ext in [".jpg", ".jpeg", ".png"]:
        if (UPLOAD_DIR / f"{image_id}{ext}").exists():
            return True
    return False