from fastapi import APIRouter, HTTPException
from ..services.export_service import ExportService
from ..export.models import ExportFormat, ExportMetadata
from ..export.preview_builder import ExportPreviewBuilder
from ..export.preview import ExportPreview
from ..export.session_manager import get_session_manager
from ..export.session import SessionStatus

router = APIRouter(prefix="/export", tags=["Export"])

@router.post("/preview")
async def export_preview(request: dict):
    questions = request.get("questions", [])
    if not questions:
        raise HTTPException(status_code=400, detail="No questions provided.")

    fmt_str = request.get("format", "pdf").upper()
    if fmt_str not in ExportFormat.__members__:
        raise HTTPException(status_code=400, detail=f"Unsupported format: {fmt_str}")

    fmt = ExportFormat[fmt_str.upper()]
    metadata_dict = request.get("metadata", {})
    metadata = ExportMetadata(**metadata_dict)

    # Gunakan ExportService untuk membangun ExportDocument
    service = ExportService()
    formatter_name = "rich" if fmt == ExportFormat.PDF else "markdown"

    document = await service.formatter_registry.get(formatter_name).format(
        questions, metadata, title="Generated Questions"
    )

    # Bangun preview
    builder = ExportPreviewBuilder()
    preview = builder.build(document, fmt)

    # Buat sesi ekspor
    session_mgr = get_session_manager()
    session = session_mgr.create_session(
        correlation_id=preview.metadata.request_id,
        export_format=fmt,
        provider=preview.metadata.provider,
        model=preview.metadata.model,
        question_count=preview.question_count,
        language=preview.metadata.language,
        difficulty=preview.metadata.difficulty,
        generated_filename=preview.filename,
        estimated_size=preview.estimated_size,
        estimated_pages=preview.estimated_pages,
        warnings=preview.warnings,
        metadata=preview.metadata,
        preview_available=True,
    )

    # Sesi sekarang PREVIEW_READY
    session_mgr.update_session(session.session_id, status=SessionStatus.PREVIEW_READY)

    # Kembalikan preview dengan session_id
    preview.session_id = session.session_id
    return preview.dict()