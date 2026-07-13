# Struktur Proyek

```
openquiz-ai/
├── backend/
│ ├── app/
│ │ ├── ai/ # Klien AI (Gemini, Groq, Mock)
│ │ ├── api/ # Endpoint FastAPI
│ │ ├── services/ # Layanan bisnis (QuestionService, ExtractionService)
│ │ ├── question_generator/ # Prompt builder, parser, validator
│ │ ├── text_processing/ # Pembersihan teks
│ │ └── logging/ # Structured logging
│ └── tests/
├── frontend/
│ └── src/
│ ├── components/ # UI components (feedback, questions, debug)
│ ├── pages/ # Halaman utama (UploadPage)
│ ├── services/ # API service
│ ├── utils/ # Formatter, clipboard, statistics
│ └── session/ # Generation session helpers
└── docs/ # Dokumentasi pengembang
```
