import pytest
from unittest.mock import MagicMock, AsyncMock
from app.export.models import (
    ExportDocument, ExportMetadata, ExportFormat,
    ExportRequest, ExportResult, ExportStatus,
)
from app.export.session import ExportSession, SessionStatus
from app.export.session_manager import ExportSessionManager, get_session_manager

# Sample questions yang bisa digunakan di banyak pengujian
@pytest.fixture
def sample_questions():
    return [
        {
            "id": 1,
            "question": "Apa ibu kota Indonesia?",
            "type": "multiple_choice",
            "choices": [
                {"label": "A", "text": "Jakarta"},
                {"label": "B", "text": "Surabaya"},
                {"label": "C", "text": "Bandung"},
                {"label": "D", "text": "Medan"}
            ],
            "answer": "A",
            "explanation": "Jakarta adalah ibu kota Indonesia."
        },
        {
            "id": 2,
            "question": "2 + 2 = ?",
            "type": "multiple_choice",
            "choices": [
                {"label": "A", "text": "3"},
                {"label": "B", "text": "4"},
                {"label": "C", "text": "5"},
                {"label": "D", "text": "6"}
            ],
            "answer": "B",
            "explanation": "2 + 2 = 4."
        }
    ]

@pytest.fixture
def sample_metadata():
    return ExportMetadata(
        generated_at="2026-07-14T10:00:00Z",
        provider="groq",
        model="llama-3.1-8b-instant",
        generation_time=1.23,
        prompt_version="v1",
        schema_version="1.0",
        question_count=2,
        language="id",
        difficulty="medium",
        session_id="sess-123",
        request_id="req-456"
    )

@pytest.fixture
def sample_document(sample_questions, sample_metadata):
    return ExportDocument(
        title="Test Document",
        content="Test content",
        questions=sample_questions,
        metadata=sample_metadata,
    )

@pytest.fixture
def empty_document():
    return ExportDocument(
        title="Empty",
        content="",
        questions=[],
        metadata=ExportMetadata()
    )

@pytest.fixture
def clean_session_manager():
    """Reset session manager sebelum setiap pengujian."""
    from app.export.session_manager import _session_manager
    global _session_manager
    _session_manager = None
    return get_session_manager()