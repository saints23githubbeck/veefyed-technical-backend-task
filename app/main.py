from fastapi import FastAPI

from app.routers.upload import router as upload_router
from app.routers.analyze import router as analyze_router

app = FastAPI(
    title="Skin Analysis API - Technical Assessment",
    description="Simple backend for image upload & mocked skin analysis",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

app.include_router(upload_router, prefix="/api")
app.include_router(analyze_router, prefix="/api")