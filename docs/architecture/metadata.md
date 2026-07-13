# Aliran Metadata AI

Metadata dihasilkan di backend saat generasi pertanyaan:

- `QuestionService.generate_questions()` mengisi `QuestionResponse.metadata` dan menambahkan `provider`, `model`, `generation_time`.
- API `/questions/generate` mengembalikan metadata dalam objek terpisah (`metadata`) untuk konsumsi frontend.
- Frontend menyimpan metadata di state `generationMeta` dan menampilkannya di `AIMetadataPanel` serta `GenerationSessionPanel`.

Metadata mencakup: provider, model, latency, prompt_version, schema_version, timestamp, token usage, finish_reason.
