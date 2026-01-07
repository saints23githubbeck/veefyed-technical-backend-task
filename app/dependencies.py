from fastapi import Depends, HTTPException

from app.services.storage import image_exists
from app.utils.exceptions import ImageNotFoundError


def valid_image_id(image_id: str) -> str:
    if not image_exists(image_id):
        raise ImageNotFoundError()
    return image_id