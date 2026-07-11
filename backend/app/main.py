from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.config import get_settings
from app.api.upload import router as upload_router   # <-- baru

settings = get_settings()

app = FastAPI(
    title="OpenQuiz AI",
    version="1.0.0",
    description="AI-powered question generation platform",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "Backend is running",
    }

# Register additional routers
app.include_router(upload_router)   # <-- baru