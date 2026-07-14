#### `docs/export/export-capability.md`

````markdown
# Export Capability System

## Tujuan

Setiap pengekspor mendeskripsikan fiturnya melalui `ExportCapability`. Ini memungkinkan frontend dan backend beradaptasi tanpa mengecek tipe pengekspor secara eksplisit.

## Model Kapabilitas

```python
class ExportCapability(BaseModel):
    supports_rich_text: bool
    supports_pagination: bool
    supports_editable: bool
    supports_images: bool
    supports_tables: bool
    supports_headers: bool
    supports_footers: bool
    supports_page_numbers: bool
    supports_metadata: bool
    supports_unicode: bool
    supports_rtl: bool
    supports_preview: bool
    supports_large_documents: bool
    # ... lebih banyak field
    supported_extensions: List[str]
    preferred_file_extension: str
    display_name: str
    description: str
```
````

## Cara Mendapatkan Kapabilitas

- **Backend**: `registry.get_capabilities("pdf")`
- **API**: `GET /export/capabilities` mengembalikan kapabilitas semua pengekspor.
- **Frontend**: menggunakan data dari API untuk menampilkan opsi yang sesuai.

## Mengapa Tidak Hardcode?

Karena dengan kapabilitas, ketika pengekspor baru ditambahkan (misal DOCX), UI otomatis tahu fitur apa yang tersedia tanpa perubahan kode.

````

#### `docs/export/export-session.md`
```markdown
# Export Session

## Konsep
`ExportSession` adalah objek yang mewakili satu proses ekspor dari awal hingga selesai. Saat ini disimpan di memori (`ExportSessionManager`), siap untuk dipindahkan ke database di masa depan.

## Status Sesi
- `CREATED` – sesi dibuat.
- `PREVIEW_READY` – pratinjau telah dihasilkan.
- `DOWNLOAD_STARTED` – pengguna memulai unduhan.
- `DOWNLOAD_COMPLETED` – file berhasil dihasilkan.
- `FAILED` – terjadi kesalahan.
- `CANCELLED` – dibatalkan.
- `CLOSED` – sesi berakhir.

## Data yang Disimpan
- ID sesi, ID korelasi, format, provider, model, jumlah pertanyaan, bahasa, kesulitan, estimasi ukuran/halaman, timestamp, status, metadata, peringatan, error.

## Manfaat Masa Depan
- **Riwayat Ekspor** – semua sesi dapat ditampilkan kembali.
- **Analitik** – menghitung metrik seperti rata-rata waktu ekspor, format terpopuler.
- **Audit** – melacak siapa mengekspor apa.
- **Resume** – melanjutkan ekspor yang gagal.
````
