# Structured Logging

Backend menggunakan modul `app/logging` untuk mencatat setiap langkah pipeline dalam format JSON terstruktur.

- **Event** didefinisikan di `events.py` (GENERATION_STARTED, PROMPT_BUILT, dll.)
- **GenerationContext** menyimpan ID korelasi (request_id, session_id) dan metadata provider.
- **Logger helpers** (`logger.py`) dipanggil di `QuestionService` pada setiap tahap.
- Format log JSON dapat dikonfigurasi dengan `JsonFormatter`.

Log tidak menyimpan konten sensitif (API key, dokumen penuh). Mode developer dapat mengaktifkan logging prompt/response.
