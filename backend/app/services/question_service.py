import logging
from typing import Optional
from ..ai import AIService  # AIService dari milestone 4 (belum ada generate? Akan dipanggil nanti)
from ..question_generator.base_generator import BaseQuestionGenerator
from ..question_generator.models import QuestionRequest, QuestionResponse

logger = logging.getLogger(__name__)

class QuestionService:
    """
    Orkestrator generasi pertanyaan.
    Menggunakan AIService untuk berkomunikasi dengan provider AI,
    dan generator spesifik untuk parsing/validasi.
    """

    def __init__(self, ai_service: AIService, generator: BaseQuestionGenerator):
        self.ai_service = ai_service
        self.generator = generator

    async def generate_questions(self, request: QuestionRequest) -> QuestionResponse:
        """
        Alur generasi pertanyaan:
        1. Generator membangun request AI (prompt)
        2. AIService mengirim ke provider
        3. Generator mengurai respons mentah
        4. Generator memvalidasi hasil
        5. Mengembalikan QuestionResponse
        """
        # Placeholder: akan diimplementasikan nanti
        raise NotImplementedError("Question generation not yet implemented")