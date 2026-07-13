from fastapi import APIRouter, HTTPException, Query
from ..question_generator.models import QuestionRequest
from ..services.question_service import QuestionService
from ..question_generator.exceptions import (
    QuestionParserError,
    QuestionFormatError,
    QuestionGenerationError,
    QuestionValidationError,
)
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
async def generate_questions(request: QuestionRequest, debug: bool = Query(False)):
    question_service = QuestionService()
    try:
        result = await question_service.generate_questions(request)
    except (QuestionParserError, QuestionFormatError, QuestionValidationError) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except QuestionGenerationError as e:
        raise HTTPException(status_code=500, detail=str(e))
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

    response = {
        "success": True,
        "message": "Questions generated successfully.",
        "data": {
            "questions": result.questions,
        },
        "metadata": {
            "provider": result.provider,
            "model": result.model,
            "latency_seconds": result.generation_time,
            "prompt_version": result.metadata.get("prompt_version"),
            "schema_version": result.metadata.get("schema_version"),
            "generation_timestamp": result.metadata.get("generation_timestamp"),
            "token_usage": result.metadata.get("token_usage"),
            "finish_reason": result.metadata.get("finish_reason"),
        },
    }
    if debug and question_service._last_prompt:
        response["prompt"] = question_service._last_prompt

    return response