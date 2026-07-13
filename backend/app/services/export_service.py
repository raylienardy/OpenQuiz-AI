import logging
from typing import Optional, List, Dict, Any
from ..export.registry import get_export_registry, get_formatter_registry
from ..export.models import (
    ExportRequest,
    ExportResponse,
    ExportResult,
    ExportStatus,
    ExportDocument,
    ExportMetadata,
)
from ..export.exceptions import ExportError

logger = logging.getLogger(__name__)

class ExportService:
    def __init__(self):
        self.export_registry = get_export_registry()
        self.formatter_registry = get_formatter_registry()

    async def export(self, request: ExportRequest) -> ExportResponse:
        """
        Terima ExportRequest yang sudah berisi ExportDocument.
        Jika perlu, pilih formatter berdasarkan format (untuk backward compatibility).
        """
        try:
            exporter = self.export_registry.get(request.format.value)
        except KeyError:
            return ExportResponse(
                success=False,
                message=f"No exporter for format '{request.format.value}'",
            )

        try:
            await exporter.initialize()
        except Exception as e:
            return ExportResponse(
                success=False,
                message=f"Failed to initialize exporter: {str(e)}",
            )

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

    async def format_and_export(
        self,
        questions: List[Dict[str, Any]],
        metadata: ExportMetadata,
        format: str,
        formatter_name: str = "plain",
        title: str = "Generated Questions",
        options: Optional[Dict[str, Any]] = None,
    ) -> ExportResponse:
        """
        Alur lengkap: format pertanyaan -> ExportDocument -> export.
        """
        # 1. Pilih formatter
        try:
            formatter = self.formatter_registry.get(formatter_name)
        except KeyError:
            return ExportResponse(
                success=False,
                message=f"No formatter registered for '{formatter_name}'",
            )

        # 2. Format
        document = await formatter.format(questions, metadata, title)

        # 3. Buat ExportRequest
        export_request = ExportRequest(
            format=format,
            document=document,
            options=options or {},
        )

        # 4. Export
        return await self.export(export_request)