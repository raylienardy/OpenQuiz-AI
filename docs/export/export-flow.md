#### `docs/export/export-flow.md`

```markdown
# Export Flow

## Alur Lengkap

1. **Pengguna meminta ekspor** (format, pertanyaan, metadata).
2. **Formatter** mengubah daftar pertanyaan + metadata menjadi `ExportDocument`.
3. **ExportService** mengambil pengekspor yang sesuai dari `ExportRegistry`.
4. **Exporter** menghasilkan file (misal PDF) dari `ExportDocument`.
5. **ExportResult** (konten biner, MIME type, nama file) dikembalikan.
6. **ExportPreview** dapat diminta sebelumnya untuk menampilkan ringkasan.
7. **ExportSession** melacak status (CREATED → PREVIEW_READY → DOWNLOAD_STARTED → COMPLETED → CLOSED).
8. **Structured Logging** mencatat setiap langkah.

## Diagram Alir (ASCII)
```

QuestionResponse
│
▼
Formatter → ExportDocument
│
▼
ExportService → ExportRegistry → Exporter
│
▼
ExportResult (file bytes)
│
▼
ExportSession (tracking)

```

## Pemisahan Tanggung Jawab
- Formatter hanya membuat `ExportDocument`, tidak peduli format output.
- Exporter hanya menerima `ExportDocument`, tidak tahu dari mana data berasal.
- Registry menyediakan pengekspor tanpa logika pemilihan di service.
```
