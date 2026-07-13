from typing import Dict, Type
from .base_exporter import BaseExporter

class ExportRegistry:
    """Registry untuk pengekspor, mirip dengan AIProviderRegistry."""

    def __init__(self):
        self._exporters: Dict[str, BaseExporter] = {}

    def register(self, format: str, exporter: BaseExporter) -> None:
        """Daftarkan pengekspor untuk format tertentu."""
        self._exporters[format.lower()] = exporter

    def get(self, format: str) -> BaseExporter:
        """Ambil pengekspor berdasarkan format."""
        fmt = format.lower()
        if fmt not in self._exporters:
            raise KeyError(f"No exporter registered for format '{fmt}'")
        return self._exporters[fmt]

    def supported_formats(self) -> list:
        """Kembalikan daftar format yang didukung."""
        return list(self._exporters.keys())

# Instans global (atau bisa dikelola lewat dependency injection)
_export_registry = None

def get_export_registry() -> ExportRegistry:
    global _export_registry
    if _export_registry is None:
        _export_registry = ExportRegistry()
    return _export_registry