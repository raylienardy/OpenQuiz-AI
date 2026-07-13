import logging
from .ai_service import AIService
from ..question_generator.prompt_builder import PromptBuilder
from ..question_generator.models import QuestionRequest, QuestionResponse
from ..question_generator.json_parser import JSONResponseParser
from ..question_generator.validators import QuestionValidator   # <-- tambahan
from ..ai.models import AIRequest

logger = logging.getLogger(__name__)

class QuestionService:
    def __init__(self):
        self.ai_service = AIService()
        self.prompt_builder = PromptBuilder()
        self.parser = JSONResponseParser()
        self.validator = QuestionValidator()   # <-- tambahan
        self._last_prompt = None

    async def generate_questions(self, request: QuestionRequest) -> QuestionResponse:
        """
        Menghasilkan pertanyaan terstruktur dengan validasi.
        """
        # 1. Bangun prompt
        prompt = self.prompt_builder.build(request)
        self._last_prompt = prompt
        logger.info("Prompt built.")

        # 2. Panggil AI
        await self.ai_service.initialize()
        ai_request = AIRequest(prompt=prompt, temperature=0.7, max_tokens=2048)
        ai_response = await self.ai_service.generate(ai_request)
        logger.info("AI response received.")

        # 3. Parse raw text menjadi QuestionResponse
        try:
            question_response = self.parser.parse(ai_response.response_text)
            question_response.provider = ai_response.provider
            question_response.model = ai_response.metadata.get("model", "unknown")
        except Exception as e:
            logger.error(f"Parsing failed: {str(e)}")
            raise

        # 4. Validasi QuestionResponse
        self.validator.validate(question_response)   # <-- tambahan

        return question_response