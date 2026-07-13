# API Generasi Pertanyaan

**Endpoint:** `POST /questions/generate`

**Request Body (JSON):**

```json
{
  "text": "...",
  "question_type": "multiple_choice",
  "number_of_questions": 5,
  "difficulty": "medium",
  "language": "id"
}
```

**Response Sukses:**

```json
{
  "success": true,
  "data": { "questions": [...] },
  "metadata": { ... },
  "debug": { ... } // hanya jika ?debug=true
}
```

**Kode Error:** 401, 413, 422, 429, 502, 504

````json

#### `docs/api/review-system.md`
```markdown
# Sistem Review (Frontend)

Komponen utama:
- `QuestionReviewWorkspace` – Kontainer utama dengan kontrol pencarian/filter/urutan.
- `QuestionCard` – Kartu ringkas, dapat diklik untuk membuka detail.
- `QuestionDetailPanel` – Panel samping yang menampilkan detail lengkap.
- `QuestionAnalyticsPanel` – Statistik jumlah dan distribusi tipe.
- `AIMetadataPanel` – Metadata AI (provider, model, latency).
- `GenerationSessionPanel` – Ringkasan sesi generasi.
- `AIPipelineInspector` – Inspektor pipeline (hanya mode developer).

Semua komponen ada di `frontend/src/components/questions/`.
````
