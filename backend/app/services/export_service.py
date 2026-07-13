import logging
from typing import Optional
from ..export.registry import get_export_registry
from ..export.models import (
    ExportRequest,
    ExportResponse,
    ExportResult,
    ExportStatus,
    ExportDocument,
)
from ..export.formatter import QuestionToDocumentFormatter
from ..export.exceptions import ExportError

logger = logging.getLogger(__name__)

class ExportService:
    """Layanan orkestrasi ekspor."""

    def __init__(self):
        self.registry = get_export_registry()
        self.formatter = QuestionToDocumentFormatter()

    async def export(self, request: ExportRequest) -> ExportResponse:
        """
        Terima ExportRequest, format dokumen, pilih pengekspor, dan kembalikan ExportResponse.
        Saat ini hanya kerangka, karena belum ada pengekspor yang terdaftar.
        """
        try:
            # 1. Dapatkan pengekspor
            exporter = self.registry.get(request.format.value)
        except KeyError:
            return ExportResponse(
                success=False,
                message=f"No exporter for format '{request.format.value}'",
            )

        # 2. Inisialisasi pengekspor (placeholder)
        try:
            await exporter.initialize()
        except Exception as e:
            return ExportResponse(
                success=False,
                message=f"Failed to initialize exporter: {str(e)}",
            )

        # 3. Ekspor dokumen (jika dokumen sudah ada di request; jika tidak, buat kosong)
        try:
            result = await exporter.export(request.document)
            return ExportResponse(
                success=True,
                message="Export completed successfully.",
                result=result,
            )
        except Exception as e:
            return ExportResponse(
                success=False,
                message=f"Export failed: {str(e)}",
            )
        finally:
            await exporter.close()