import logging
from ..ai import AIService
from ..question_generator.prompt_builder import PromptBuilder
from ..question_generator.models import QuestionRequest, QuestionResponse
from ..question_generator.json_parser import JSONResponseParser
from ..ai.models import AIRequest

logger = logging.getLogger(__name__)

class QuestionService:
    def __init__(self):
        self.ai_service = AIService()
        self.prompt_builder = PromptBuilder()
        self.parser = JSONResponseParser()
        self._last_prompt = None

    async def generate_questions(self, request: QuestionRequest) -> QuestionResponse:
        """
        Menghasilkan pertanyaan terstruktur.
        Alur: prompt -> AI -> raw response -> parse -> QuestionResponse.
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
            # Isi metadata provider/model
            question_response.provider = ai_response.provider
            question_response.model = ai_response.metadata.get("model", "unknown")
            # generation_time bisa dihitung dari awal, tapi untuk sekarang diabaikan
            return question_response
        except Exception as e:
            # Jika parsing gagal, kita lempar exception yang akan ditangani endpoint
            logger.error(f"Parsing failed: {str(e)}")
            raise