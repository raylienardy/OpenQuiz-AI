from typing import Dict, Type
from .base_exporter import BaseExporter
from .formatters.base_formatter import BaseFormatter

class ExportRegistry:
    def __init__(self):
        self._exporters: Dict[str, BaseExporter] = {}

    def register(self, format: str, exporter: BaseExporter) -> None:
        self._exporters[format.lower()] = exporter

    def get(self, format: str) -> BaseExporter:
        fmt = format.lower()
        if fmt not in self._exporters:
            raise KeyError(f"No exporter registered for format '{fmt}'")
        return self._exporters[fmt]

    def supported_formats(self) -> list:
        return list(self._exporters.keys())

class FormatterRegistry:
    def __init__(self):
        self._formatters: Dict[str, BaseFormatter] = {}

    def register(self, name: str, formatter: BaseFormatter) -> None:
        self._formatters[name.lower()] = formatter

    def get(self, name: str) -> BaseFormatter:
        fmt = name.lower()
        if fmt not in self._formatters:
            raise KeyError(f"No formatter registered for '{fmt}'")
        return self._formatters[fmt]

    def supported_formatters(self) -> list:
        return list(self._formatters.keys())

# Instans global untuk export registry
_export_registry = None
def get_export_registry() -> ExportRegistry:
    global _export_registry
    if _export_registry is None:
        _export_registry = ExportRegistry()
    return _export_registry

# Instans global untuk formatter registry
_formatter_registry = None
def get_formatter_registry() -> FormatterRegistry:
    global _formatter_registry
    if _formatter_registry is None:
        _formatter_registry = FormatterRegistry()
    return _formatter_registry