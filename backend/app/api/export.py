"""
API untuk pratinjau ekspor.
"""

from fastapi import APIRouter, HTTPException
from ..question_generator.models import QuestionRequest  # Anda bisa membuat model terpisah
from ..services.export_service import ExportService
from ..export.models import ExportFormat, ExportMetadata
from ..export.preview_builder import ExportPreviewBuilder
from ..export.preview import ExportPreview

router = APIRouter(prefix="/export", tags=["Export"])

@router.post("/preview")
async def export_preview(request: dict):
    """
    Menerima data pertanyaan dan format, mengembalikan pratinjau ekspor.
    Body diharapkan:
    {
        "questions": [...],
        "format": "pdf",
        "metadata": {...}  # opsional
    }
    """
    questions = request.get("questions", [])
    if not questions:
        raise HTTPException(status_code=400, detail="No questions provided.")

    fmt_str = request.get("format", "pdf")
    if fmt_str not in ExportFormat.__members__:
        raise HTTPException(status_code=400, detail=f"Unsupported format: {fmt_str}")

    fmt = ExportFormat[fmt_str.upper()]
    metadata_dict = request.get("metadata", {})
    metadata = ExportMetadata(**metadata_dict)

    # Gunakan ExportService untuk membangun ExportDocument
    service = ExportService()
    # Pilih formatter default sesuai format (atau rich untuk pdf)
    formatter_name = "rich" if fmt == ExportFormat.PDF else "markdown"

    # Format dokumen
    document = await service.formatter_registry.get(formatter_name).format(
        questions, metadata, title="Generated Questions"
    )

    # Bangun preview
    builder = ExportPreviewBuilder()
    preview = builder.build(document, fmt)

    return preview.dict()