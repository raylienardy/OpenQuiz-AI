from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.api.upload import router as upload_router
from app.api.ai import router as ai_router   # <-- tambahan
from app.api.questions import router as questions_router   # tambahan

settings = get_settings()

app = FastAPI(
    title="OpenQuiz AI",
    version="1.0.0",
    description="AI-powered question generation platform",
)

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

app.include_router(upload_router)
app.include_router(ai_router)   # <-- tambahan
app.include_router(questions_router)
