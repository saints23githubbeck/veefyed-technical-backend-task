from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    image_id: str = Field(..., min_length=8)


class AnalysisResponse(BaseModel):
    image_id: str
    skin_type: str
    issues: list[str]
    confidence: float = Field(..., ge=0.0, le=1.0)