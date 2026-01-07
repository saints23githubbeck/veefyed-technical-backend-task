from fastapi import APIRouter, UploadFile, File

from app.schemas.responses import UploadResponse
from app.services.storage import generate_image_id, save_image
from app.utils.validators import validate_image

router = APIRouter(tags=["upload"])


@router.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
    validate_image(file)
    image_id = generate_image_id()
    save_image(file, image_id)
    return UploadResponse(image_id=image_id)