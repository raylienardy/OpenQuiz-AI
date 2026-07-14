#### `docs/export/export-metadata.md`

```markdown
# Export Metadata

## Tujuan

Setiap ekspor membawa metadata tentang asal-usul pertanyaan. Metadata ini disertakan dalam `ExportDocument` dan dapat ditampilkan di dalam file (misal, halaman informasi di PDF) atau digunakan oleh sistem eksternal.

## Field Metadata

- `generated_at` – timestamp pembuatan pertanyaan.
- `provider` – penyedia AI (Groq, Gemini, Mock).
- `model` – model yang digunakan.
- `generation_time` – durasi generasi.
- `prompt_version`, `schema_version` – versi prompt dan skema.
- `question_count` – jumlah pertanyaan.
- `language`, `difficulty` – bahasa dan kesulitan.
- `session_id`, `request_id` – ID korelasi.
- `export_format`, `formatter_name`, `formatter_version` – informasi format/ekspor.

## Aliran Metadata

1. `QuestionService.generate_questions()` menghasilkan metadata.
2. API menyertakan metadata di respons.
3. Frontend mengirim metadata kembali saat meminta ekspor.
4. Formatter menempelkan metadata ke `ExportDocument`.
5. Exporter membaca metadata dan menampilkannya (opsional).
```
