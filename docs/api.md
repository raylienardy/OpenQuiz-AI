# API Reference

Base URL: `http://localhost:8000`

## Health Check

### `GET /health`

Check if the backend is running.

**Response**

```json
{
  "status": "ok",
  "message": "Backend is running"
}
```

## Upload & Extraction

### `POST /upload`

Upload a learning material file (PDF, DOCX, TXT). The backend validates, extracts text, cleans it, and returns metadata along with the extracted content.

**Request**

- Multipart form-data
- Field: `file` (required)

**Success Response** (200)

```json
{
  "success": true,
  "message": "File uploaded and processed successfully.",
  "data": {
    "filename": "lecture.pdf",
    "content_type": "application/pdf",
    "size": 245873,
    "text": "Extracted and cleaned text...",
    "character_count": 4200,
    "word_count": 680,
    "warnings": [],
    "metadata": {
      "page_count": 12
    }
  }
}
```

**Error Responses**

- **400** – Missing file or empty file
- **413** – File exceeds 20 MB
- **415** – Unsupported file type
- **422** – Validation error

Example:

```json
{
  "success": false,
  "message": "Unsupported file type '.png'. Allowed types: .pdf, .docx, .txt.",
  "errors": {
    "detail": "Unsupported file type '.png'. Allowed types: .pdf, .docx, .txt."
  }
}
```

## AI Test (Development)

### `GET /ai/test`

Send a simple prompt to the configured AI provider to verify connectivity and configuration. This endpoint is intended for development and may be removed in future releases.

**Response**

```json
{
  "success": true,
  "provider": "groq",
  "model": "llama-3.1-8b-instant",
  "response": "CONNECTED"
}
```

**Possible Errors**

- `401` – Invalid API key
- `502` – Connection error or unexpected provider response
- `429` – Rate limit exceeded
- `504` – Request timed out

## Data Formats

All successful responses contain `"success": true` and a `data` object. Errors contain `"success": false`, a human-readable `message`, and optionally an `errors` object with machine-readable details.
