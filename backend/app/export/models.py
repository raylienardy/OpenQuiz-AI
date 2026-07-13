from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from enum import Enum

class ExportFormat(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    MARKDOWN = "markdown"
    HTML = "html"
    CSV = "csv"
    MOODLE_XML = "moodle_xml"
    JSON = "json"
    ZIP = "zip"

class ExportStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class ExportMetadata(BaseModel):
    """Metadata yang akan disertakan dalam setiap ekspor."""
    generated_at: Optional[str] = None
    provider: Optional[str] = None
    model: Optional[str] = None
    generation_time: Optional[float] = None
    prompt_version: Optional[str] = None
    schema_version: Optional[str] = None
    question_count: Optional[int] = None
    language: Optional[str] = None
    difficulty: Optional[str] = None
    session_id: Optional[str] = None
    request_id: Optional[str] = None
    export_format: Optional[str] = None
    additional: Dict[str, Any] = Field(default_factory=dict)

class ExportDocument(BaseModel):
    """Dokumen standar yang akan diekspor oleh pengekspor."""
    title: str = ""
    content: str = ""          # Konten yang sudah diformat (misal, Markdown)
    questions: List[Dict[str, Any]] = Field(default_factory=list)
    metadata: ExportMetadata = Field(default_factory=ExportMetadata)
    raw_data: Optional[Dict[str, Any]] = None  # Data asli jika diperlukan

class ExportRequest(BaseModel):
    """Permintaan ekspor dari klien."""
    format: ExportFormat
    document: ExportDocument
    options: Dict[str, Any] = Field(default_factory=dict)  # Opsi khusus format

class ExportResult(BaseModel):
    """Hasil ekspor."""
    status: ExportStatus = ExportStatus.COMPLETED
    format: ExportFormat
    content: Optional[bytes] = None       # Konten biner (PDF, DOCX, dll.)
    content_type: Optional[str] = None    # MIME type
    filename: Optional[str] = None
    errors: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ExportResponse(BaseModel):
    """Respons yang dikirim ke klien."""
    success: bool
    message: str
    result: Optional[ExportResult] = None