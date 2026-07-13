class ExportError(Exception):
    """Kesalahan dasar untuk modul ekspor."""
    pass

class ExportInitializationError(ExportError):
    """Gagal menginisialisasi pengekspor."""
    pass

class ExportValidationError(ExportError):
    """Data yang akan diekspor tidak valid."""
    pass

class ExportGenerationError(ExportError):
    """Gagal menghasilkan file ekspor."""
    pass

class ExportFormatError(ExportError):
    """Format ekspor tidak didukung."""
    pass

class ExportPermissionError(ExportError):
    """Izin menulis file ditolak."""
    pass

class ExportConfigurationError(ExportError):
    """Konfigurasi ekspor salah."""
    pass

class ExportTimeoutError(ExportError):
    """Proses ekspor melebihi batas waktu."""
    pass