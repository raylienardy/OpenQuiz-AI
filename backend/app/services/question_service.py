import logging
from ..ai import AIService
from ..question_generator.prompt_builder import PromptBuilder
from ..question_generator.models import QuestionRequest
from ..ai.models import AIRequest

logger = logging.getLogger(__name__)

class QuestionService:
    """
    Orkestrator generasi pertanyaan.
    Menggunakan PromptBuilder untuk membuat prompt,
    lalu AIService untuk mengirim ke provider AI.
    """

    def __init__(self):
        # AIService akan membaca provider dari settings secara otomatis
        self.ai_service = AIService()
        self.prompt_builder = PromptBuilder()
        self._last_prompt = None   # untuk keperluan debugging

    async def generate_questions(self, request: QuestionRequest):
        """
        Alur:
        1. Bangun prompt dari request.
        2. Kirim prompt ke AI melalui AIService.
        3. Kembalikan AIResponse mentah.
        """
        # 1. Bangun prompt
        prompt = self.prompt_builder.build(request)
        self._last_prompt = prompt
        logger.info("Prompt built for question generation.")

        # 2. Buat AIRequest
        ai_request = AIRequest(
            prompt=prompt,
            temperature=0.7,
            max_tokens=2048,
        )

        # 3. Panggil AIService (pastikan sudah diinisialisasi)
        await self.ai_service.initialize()
        logger.info("Calling AI provider for question generation...")
        ai_response = await self.ai_service.generate(ai_request)
        logger.info("AI response received.")

        return ai_response