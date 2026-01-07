import random
from fastapi import APIRouter, Depends

from app.schemas.responses import AnalysisResponse
from app.dependencies import valid_image_id

router = APIRouter(tags=["analysis"])


SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal", "Sensitive"]
POSSIBLE_ISSUES = [
    "Acne", "Hyperpigmentation", "Redness", "Dry patches",
    "Blackheads", "Large pores", "Wrinkles", "Uneven tone"
]


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_image(image_id: str = Depends(valid_image_id)):
    # Mock analysis - in real project would call ML service
    return AnalysisResponse(
        image_id=image_id,
        skin_type=random.choice(SKIN_TYPES),
        issues=random.sample(POSSIBLE_ISSUES, k=random.randint(0, 3)),
        confidence=round(random.uniform(0.68, 0.96), 3)
    )