"""
API endpoint untuk mengajukan permintaan generasi pertanyaan.
"""

from fastapi import APIRouter, HTTPException, Query
from ..question_generator.models import QuestionRequest
from ..services.question_service import QuestionService
from ..ai.exceptions import (
    AIAuthenticationError,
    AIConnectionError,
    AIRateLimitError,
    AIResponseError,
    AITimeoutError,
    ProviderNotSupportedError,
)

router = APIRouter(prefix="/questions", tags=["Question Generation"])

@router.post("/generate")
async def generate_questions(
    request: QuestionRequest,
    debug: bool = Query(False, description="Sertakan prompt yang digunakan (hanya untuk pengembangan)"),
):
    """
    Menghasilkan pertanyaan berdasarkan teks yang diberikan.

    Request body mengikuti model QuestionRequest.
    """
    # Inisialisasi service (dependency injection bisa dilakukan di sini)
    question_service = QuestionService()

    try:
        # generate_questions akan mengembalikan AIResponse (raw)
        ai_response = await question_service.generate_questions(request)
    except AIAuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except AIRateLimitError as e:
        raise HTTPException(status_code=429, detail=str(e))
    except AITimeoutError as e:
        raise HTTPException(status_code=504, detail=str(e))
    except AIConnectionError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except AIResponseError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except ProviderNotSupportedError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

    # Bangun respons
    response = {
        "success": True,
        "provider": ai_response.provider,
        "model": ai_response.metadata.get("model", "unknown"),
        "raw_response": ai_response.response_text,
    }
    if debug:
        # Prompt aman untuk debugging, tapi hanya jika diminta
        prompt = question_service._last_prompt  # kita simpan prompt di service
        if prompt:
            response["prompt"] = prompt

    return response