# Developer Mode

Mode developer diaktifkan melalui toggle di UI (disimpan di `localStorage`). Saat aktif:

- Backend mengumpulkan data debug di `QuestionService.debug_info` (prompt, raw response, parsed JSON, validation).
- API mengembalikan objek `debug` dalam respons.
- Frontend menampilkan `AIPipelineInspector` yang memvisualisasikan setiap langkah pipeline.

Keamanan: Data debug tidak pernah ditampilkan kecuali mode developer diaktifkan secara eksplisit oleh pengguna.
