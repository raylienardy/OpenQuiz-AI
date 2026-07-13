import time
import logging
from datetime import datetime, timezone
from .ai_service import AIService
from ..question_generator.prompt_builder import PromptBuilder
from ..question_generator.models import QuestionRequest, QuestionResponse
from ..question_generator.json_parser import JSONResponseParser
from ..question_generator.validators import QuestionValidator
from ..ai.models import AIRequest

logger = logging.getLogger(__name__)

PROMPT_VERSION = "v1"
SCHEMA_VERSION = "1.0"

class QuestionService:
    def __init__(self):
        self.ai_service = AIService()
        self.prompt_builder = PromptBuilder()
        self.parser = JSONResponseParser()
        self.validator = QuestionValidator()
        self._last_prompt = None

    async def generate_questions(self, request: QuestionRequest) -> QuestionResponse:
        prompt = self.prompt_builder.build(request)
        self._last_prompt = prompt
        logger.info("Prompt built.")

        await self.ai_service.initialize()
        ai_request = AIRequest(prompt=prompt, temperature=0.7, max_tokens=2048)

        start_time = time.time()
        try:
            ai_response = await self.ai_service.generate(ai_request)
        except Exception as e:
            logger.error(f"AI generation failed: {str(e)}")
            raise
        latency = time.time() - start_time
        logger.info("AI response received.")

        try:
            question_response = self.parser.parse(ai_response.response_text)
        except Exception as e:
            logger.error(f"Parsing failed: {str(e)}")
            raise

        self.validator.validate(question_response)

        # Isi metadata
        question_response.provider = ai_response.provider
        question_response.model = ai_response.metadata.get("model", "unknown")
        question_response.generation_time = latency
        question_response.metadata.update({
            "prompt_version": PROMPT_VERSION,
            "schema_version": SCHEMA_VERSION,
            "generation_timestamp": datetime.now(timezone.utc).isoformat(),
        })
        if "usage" in ai_response.metadata:
            question_response.metadata["token_usage"] = ai_response.metadata["usage"]
        if "finish_reason" in ai_response.metadata:
            question_response.metadata["finish_reason"] = ai_response.metadata["finish_reason"]

        return question_response