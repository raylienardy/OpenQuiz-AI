Berikut dokumentasi lengkap untuk modul Export. Semua file dibuat di dalam folder `docs/export/`.

---

### 1. Perintah Git Bash

```bash
mkdir -p docs/architecture docs/export
touch docs/export/export-architecture.md
touch docs/export/export-flow.md
touch docs/export/export-capability.md
touch docs/export/export-session.md
touch docs/export/export-metadata.md
touch docs/export/export-registry.md
touch docs/export/export-roadmap.md
```

### 2. File Dokumentasi

#### `docs/export/export-architecture.md`

```markdown
# Export Architecture

## Overview

Sistem ekspor mengubah `QuestionResponse` menjadi file yang dapat diunduh. Arsitekturnya mengikuti pola yang sama dengan AI Provider: setiap pengekspor mewarisi `BaseExporter`, didaftarkan di `ExportRegistry`, dan dipilih secara dinamis oleh `ExportService` tanpa hardcode.

## Komponen Utama

- **BaseExporter** – antarmuka abstrak untuk semua pengekspor.
- **ExportRegistry** – menyimpan instance pengekspor, menyediakan pencarian berdasarkan format.
- **ExportService** – orkestrator yang menggabungkan formatter dan registry.
- **Formatter Layer** – mengubah data pertanyaan menjadi `ExportDocument` agar pengekspor tidak perlu tahu detail QuestionResponse.
- **ExportDocument** – representasi universal yang dapat dikonsumsi oleh semua pengekspor.
- **ExportPreview** – ringkasan ekspor sebelum dihasilkan.
- **ExportSession** – melacak siklus hidup ekspor.
- **ExportCapability** – mendeskripsikan fitur yang didukung pengekspor.
- **ExportMetadata** – informasi tentang asal-usul pertanyaan yang disertakan dalam setiap ekspor.

## Prinsip Desain

- **Tidak ada hardcode** – `ExportService` tidak pernah memeriksa jenis pengekspor.
- **Plugin siap** – tambah pengekspor baru hanya dengan membuat kelas dan mendaftarkannya.
- **Pemisahan tanggung jawab** – format, ekspor, metadata, dan sesi adalah lapisan yang independen.
```
