import pytest
from unittest.mock import AsyncMock, patch
from app.services.export_service import ExportService
from app.export.models import ExportRequest, ExportFormat, ExportDocument, ExportMetadata, ExportResult, ExportStatus

class TestExportService:
    @pytest.mark.asyncio
    async def test_export_with_registered_exporter(self, sample_document):
        service = ExportService()
        # Daftarkan dummy exporter
        dummy = AsyncMock()
        dummy.initialize.return_value = None
        dummy.export.return_value = ExportResult(
            status=ExportStatus.COMPLETED,
            format=ExportFormat.PDF,
            content=b"%PDF...",
            content_type="application/pdf",
            filename="test.pdf",
        )
        dummy.close.return_value = None
        service.export_registry.register("pdf", dummy)

        request = ExportRequest(
            format=ExportFormat.PDF,
            document=sample_document,
        )
        response = await service.export(request)
        assert response.success is True
        assert response.result.format == ExportFormat.PDF

    @pytest.mark.asyncio
    async def test_export_unregistered_format(self, sample_document):
        service = ExportService()
        request = ExportRequest(
            format=ExportFormat.PDF,  # PDF belum terdaftar
            document=sample_document,
        )
        response = await service.export(request)
        assert response.success is False
        assert "No exporter" in response.message

    @pytest.mark.asyncio
    async def test_format_and_export(self, sample_questions, sample_metadata):
        service = ExportService()
        # Daftarkan formatter dan dummy exporter
        from app.export.formatters import PlainFormatter
        service.formatter_registry.register("plain", PlainFormatter())

        dummy = AsyncMock()
        dummy.initialize.return_value = None
        dummy.export.return_value = ExportResult(
            status=ExportStatus.COMPLETED,
            format=ExportFormat.PDF,
            content=b"data",
            content_type="text/plain",
            filename="test.txt",
        )
        dummy.close.return_value = None
        service.export_registry.register("pdf", dummy)

        response = await service.format_and_export(
            questions=sample_questions,
            metadata=sample_metadata,
            format="pdf",
            formatter_name="plain",
            title="My Questions",
        )
        assert response.success is True