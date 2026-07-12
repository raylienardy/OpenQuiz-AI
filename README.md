# OpenQuiz AI

AI-powered question generation platform (Version 1.0 MVP).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Status: Milestone 2 Complete](https://img.shields.io/badge/status-milestone%202-brightgreen)](#)

## 🚀 Current Features (v1.0 in Progress)

- ✅ **Project Foundation** – React + Vite frontend, FastAPI backend, health-check communication.
- ✅ **Upload System** – Drag & drop, file selection, client & server validation, clear feedback states.
  - Supported formats: **PDF**, **DOCX**, **TXT**
  - Maximum file size: **20 MB**
- ⬜ Text Extraction (next milestone)
- ⬜ AI Question Generation (Gemini)
- ⬜ Result Viewer & PDF Export

## 📂 Project Structure

```

openquiz-ai/
├── backend/ # FastAPI server (Python)
├── frontend/ # React SPA (Vite + JavaScript)
├── docs/ # Documentation
├── datasets/ # Future open datasets
└── examples/ # Usage examples

```

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- Git

### 1. Clone & setup backend

```bash
cd backend
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env           # add your GEMINI_API_KEY (optional for now)
uvicorn app.main:app --reload
```

API runs at [http://localhost:8000](http://localhost:8000).

### 2. Setup frontend

```bash
cd frontend
npm install
cp .env.example .env           # adjust VITE_API_URL if needed
npm run dev
```

App opens at [http://localhost:5173](http://localhost:5173).  
The home page shows backend connectivity status.  
Navigate to `/upload` to test the upload feature.

### 3. Verify upload

Drag a PDF, DOCX, or TXT file onto the upload page or use the file browser.  
After client-side validation, click **Upload** – the backend will validate again and return file metadata.  
No text extraction or AI processing occurs yet.

## 📄 Upload Flow (Milestone 2)

```
Select File → Client Validation → POST /upload → Server Validation → Success Metadata
```

Full details: [docs/upload.md](docs/upload.md)

## 🔮 Roadmap

| Milestone              | Status      |
| ---------------------- | ----------- |
| 1 – Project Foundation | ✅ Complete |
| 2 – Material Upload    | ✅ Complete |
| 3 – Text Extraction    | 🔜 Next     |
| 4 – Gemini Integration | ⬜          |
| 5 – Question Generator | ⬜          |
| 6 – Result Viewer      | ⬜          |
| 7 – PDF Export         | ⬜          |
| 8 – UI Polish          | ⬜          |
| 9 – Testing            | ⬜          |
| 10 – Release v1.0      | ⬜          |

## 🤝 Contributing

OpenQuiz AI is an open-source project. Contributions, issues and feature requests are welcome.  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) (if available) before submitting a pull request.

## 📜 License

MIT © OpenQuiz AI

````

### 2. `docs/upload.md` (baru)

```markdown
# Upload System Documentation

## Overview
The upload feature allows users to provide learning materials (PDF, DOCX, TXT) through a modern, responsive interface. The system performs validation on both client and server to ensure only valid files are accepted, and provides clear feedback throughout the process.

## Architecture

The upload flow is built with a layered architecture:

````

Frontend (React)
│ UploadPage → UploadCard → FileDropzone / SelectedFile
│ Validation: utils/validateFile.js
│ Service: services/uploadService.js → api.js (Axios)
│
Backend (FastAPI)
│ Route: api/upload.py
│ Service: services/upload_service.py
│ Validator: utils/file_validator.py
│ Config: config.py

````

**Separation of concerns:**
- **Frontend** handles UI states (idle, ready, uploading, success, error) and client-side validation.
- **Backend** independently re-validates every upload for security, then returns file metadata.
- No file is permanently stored; future milestones will add text extraction.

## Upload Flow

1. **User selects a file** via drag & drop or file browser.
2. **Client-side validation** checks file extension (.pdf, .docx, .txt) and size ≤ 20 MB.
   - If invalid, an error message is shown immediately; upload is disabled.
   - If valid, the file card displays “Ready to upload” and the Upload button becomes active.
3. **User clicks Upload** → `POST /upload` with multipart/form-data.
4. **Server-side validation** performs the same checks (plus empty file detection) for security.
5. On success, the frontend shows a success card with file metadata (name, size, type) and a note “Ready for Text Extraction” (future step).
6. On failure, a user-friendly error message is displayed; the user can try again.

## API Reference

### `POST /upload`

Upload a learning material file.

- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Form field:** `file` (required)

#### Success Response

**Code:** `200 OK`

```json
{
  "success": true,
  "message": "File uploaded successfully.",
  "data": {
    "filename": "lecture.pdf",
    "content_type": "application/pdf",
    "size": 245873
  }
}
````

#### Error Responses

**400 Bad Request** – Missing or empty file.

```json
{
  "success": false,
  "message": "No file uploaded.",
  "errors": {
    "detail": "No file uploaded."
  }
}
```

**413 Request Entity Too Large** – File exceeds 20 MB.

```json
{
  "success": false,
  "message": "File exceeds the maximum upload size (20 MB).",
  "errors": {
    "detail": "File exceeds the maximum upload size (20 MB)."
  }
}
```

**415 Unsupported Media Type** – Invalid file extension.

```json
{
  "success": false,
  "message": "Unsupported file type '.exe'. Allowed types: .pdf, .docx, .txt.",
  "errors": {
    "detail": "Unsupported file type '.exe'. Allowed types: .pdf, .docx, .txt."
  }
}
```

## Validation Rules

| Rule                                  | Client | Server | Error Message                                   |
| ------------------------------------- | ------ | ------ | ----------------------------------------------- |
| File must be provided                 | ✅     | ✅     | “No file uploaded.”                             |
| Empty file (0 bytes)                  | ❌     | ✅     | “Uploaded file is empty.”                       |
| Allowed extensions: .pdf, .docx, .txt | ✅     | ✅     | “Unsupported file type …”                       |
| Maximum size 20 MB                    | ✅     | ✅     | “File exceeds the maximum upload size (20 MB).” |

> **Note:** Frontend validation improves user experience, but **backend validation is mandatory for security** – it cannot be bypassed.

## Upload Lifecycle (UI States)

| State         | Frontend Display                            | Backend                |
| ------------- | ------------------------------------------- | ---------------------- |
| **Idle**      | Dropzone, file browser                      | –                      |
| **Ready**     | Selected file info + “Ready to upload”      | –                      |
| **Uploading** | Spinner, progress bar, “Uploading…”         | Processing             |
| **Success**   | File metadata + “Ready for Text Extraction” | File metadata returned |
| **Error**     | Friendly error message, “Try Again”         | Validation failure     |

## Supported File Types

| Format | Extension | MIME Type                                                               |
| ------ | --------- | ----------------------------------------------------------------------- |
| PDF    | .pdf      | application/pdf                                                         |
| Word   | .docx     | application/vnd.openxmlformats-officedocument.wordprocessingml.document |
| Text   | .txt      | text/plain                                                              |

Other formats (images, archives, executables) are rejected with a clear message.

## Future Enhancements

In the next milestones, the upload system will be extended to:

- **Text Extraction** – Extract plain text from uploaded documents.
- **AI Processing** – Send extracted text to Google Gemini for question generation.
- **Question Preview & Export** – Display generated questions and download as PDF.

The upload API is designed to accommodate these additions with minimal changes – the validation layer and service structure remain unchanged.
