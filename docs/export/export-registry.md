#### `docs/export/export-registry.md`

```markdown
# Export Registry

## Pola

`ExportRegistry` adalah penyimpanan terpusat untuk instance pengekspor. Mirip dengan `AIProviderRegistry`.

## API

- `register(format, exporter)` – mendaftarkan pengekspor.
- `get_exporter(format)` – mendapatkan pengekspor.
- `unregister(format)` – menghapus pengekspor.
- `list_exporters()` – daftar format yang didukung.
- `get_capabilities(format)` – kapabilitas pengekspor.
- `list_capabilities()` – kapabilitas semua pengekspor.

## Cara Menambah Pengekspor Baru

1. Buat kelas turunan `BaseExporter`.
2. Panggil `registry.register("format", instance)`.
3. Tidak ada perubahan di `ExportService` atau komponen lain.

## Inisialisasi

PDFExporter otomatis didaftarkan saat modul `export` diimpor (`__init__.py`). Pengekspor lain dapat ditambahkan dengan cara yang sama.
```
