import asyncio
import logging
from .ai_service import AIService
from ..question_generator.prompt_builder import PromptBuilder
from ..question_generator.models import QuestionRequest, QuestionResponse
from ..question_generator.json_parser import JSONResponseParser
from ..question_generator.validators import QuestionValidator
from ..ai.models import AIRequest

logger = logging.getLogger(__name__)

# Timeout untuk permintaan AI (detik)
AI_TIMEOUT = 60

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

        try:
            await self.ai_service.initialize()
        except Exception as e:
            logger.error(f"AI initialization failed: {str(e)}")
            raise

        ai_request = AIRequest(prompt=prompt, temperature=0.7, max_tokens=2048)

        try:
            ai_response = await asyncio.wait_for(
                self.ai_service.generate(ai_request),
                timeout=AI_TIMEOUT
            )
            logger.info("AI response received.")
        except asyncio.TimeoutError:
            logger.error("AI request timed out.")
            raise AITimeoutError("AI provider timed out. Please try again.")
        except Exception as e:
            logger.error(f"AI generation failed: {str(e)}")
            raise

        try:
            question_response = self.parser.parse(ai_response.response_text)
            question_response.provider = ai_response.provider
            question_response.model = ai_response.metadata.get("model", "unknown")
        except Exception as e:
            logger.error(f"Parsing failed: {str(e)}")
            raise

        self.validator.validate(question_response)
        return question_response