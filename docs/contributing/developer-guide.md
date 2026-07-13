# Panduan Pengembang

## Menjalankan Proyek

1. Clone repo
2. Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`
3. Frontend: `cd frontend && npm install && npm run dev`
4. Salin `.env.example` ke `.env`, isi `AI_PROVIDER` dan API key.

## Struktur Proyek

- `backend/app/` – API, service, AI clients, question generator
- `frontend/src/` – Komponen, halaman, service, utilitas

## Menambahkan Fitur

- Provider AI baru: buat client di `backend/app/ai/`, daftarkan di registry.
- Panel baru: tambahkan komponen di `frontend/src/components/questions/`, integrasikan ke `UploadPage` atau `QuestionReviewWorkspace`.
- Formatter baru: tambahkan di `frontend/src/utils/export/`.

## Testing

- Backend: `pytest tests/`
- Frontend: jalankan dan uji manual dengan Mock provider (`AI_PROVIDER=mock`)
