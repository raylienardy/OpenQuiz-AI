# OpenQuiz AI

AI-powered question generation platform (Version 1.0 MVP).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## 🚀 Current Features

- ✅ **Project Foundation** – React + Vite frontend, FastAPI backend
- ✅ **Upload System** – PDF, DOCX, TXT upload with validation & preview
- ✅ **Document Extraction** – Text extraction & cleaning pipeline
- ✅ **AI Provider Architecture** – Gemini, Groq, Mock (switch via `.env`)

## 🤖 AI Providers

OpenQuiz AI uses a provider-independent architecture. Switch providers by changing one line in `.env`.

| Provider   | Requires API Key | Internet | Best For                             |
| ---------- | ---------------- | -------- | ------------------------------------ |
| **Groq**   | Yes (free)       | Yes      | Fast development, generous free tier |
| **Gemini** | Yes (free)       | Yes      | Google ecosystem                     |
| **Mock**   | No               | No       | Offline development & testing        |

➡️ **Recommended for development:** Groq (fast & free tier)  
➡️ **For UI/frontend work:** Mock (no internet needed)

📖 **Full documentation:** [docs/ai-providers.md](docs/ai-providers.md)

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env           # edit .env, choose your AI provider
uvicorn app.main:app --reload
```

**Minimal `.env` for Groq:**

```
AI_PROVIDER=groq
GROQ_API_KEY=gsk_your_key_here
```

**For Gemini:**

```
AI_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=models/gemini-2.0-flash
```

**For offline development:**

```
AI_PROVIDER=mock
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173`

### 3. Verify AI Connection

```bash
curl http://localhost:8000/ai/test
```

## 📂 Project Structure

```
openquiz-ai/
├── backend/        # FastAPI server
├── frontend/       # React SPA
├── docs/           # Documentation
└── datasets/       # Future datasets
```

## 📖 Documentation

- [AI Providers](docs/ai-providers.md)
- [Configuration Guide](docs/configuration.md)
- [Gemini Setup](docs/gemini.md)
- [Groq Setup](docs/groq.md)
- [Mock Provider](docs/mock.md)

## 🔮 Roadmap

| Milestone                   | Status |
| --------------------------- | ------ |
| 1 – Project Foundation      | ✅     |
| 2 – Material Upload         | ✅     |
| 3 – Document Extraction     | ✅     |
| 4 – AI Provider Integration | ✅     |
| 5 – Question Generator      | 🔜     |

## 📜 License

MIT

````

---

### 3. Dokumentasi Baru

#### `docs/ai-providers.md`

```markdown
# AI Provider System

## Overview

OpenQuiz AI uses a **provider-independent architecture** for AI services. This means the application code never depends on a specific AI vendor (Google, Groq, OpenAI). Instead, all providers implement the same interface (`BaseAIClient`), and the active provider is chosen via environment variable.

## Why Provider-Independent?

- **No vendor lock-in** – switch providers without changing code
- **Easy to add new providers** – just implement one interface
- **Offline development** – use Mock provider when no internet
- **Future-proof** – supports Ollama, OpenAI, Claude, etc. later

## Architecture

````

Application
│
▼
AIService (reads AI_PROVIDER from .env)
│
▼
Provider Registry (maps name → class)
│
├── "gemini" → GeminiClient
├── "groq" → GroqClient
└── "mock" → MockClient

```

All clients return `AIResponse`, so the rest of the application never knows which provider is active.

## Available Providers

| Provider | Key Required | Internet | Use Case |
|----------|-------------|----------|----------|
| **groq** | Yes (free) | Yes | Recommended for development |
| **gemini** | Yes (free) | Yes | Google ecosystem users |
| **mock** | No | No | Offline development, testing |

## How to Switch Providers

Just change `AI_PROVIDER` in `.env` and restart the backend.

## Adding a New Provider

1. Create a new class inheriting from `BaseAIClient` (see `backend/app/ai/base_client.py`)
2. Implement `initialize()`, `generate()`, `health_check()`, `close()`
3. Register it in `backend/app/ai/providers.py`
4. Add the provider name to `SUPPORTED_PROVIDERS` in `backend/app/config.py`
5. Update `.env.example` with new environment variables

No changes needed in:
- API routes
- AIService
- Business logic
- Frontend

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Unsupported AI provider" | Check `AI_PROVIDER` spelling in `.env` |
| "API key is missing" | Add `GROQ_API_KEY` or `GEMINI_API_KEY` to `.env` |
| 429 Rate Limit | Wait and retry, or switch to another provider |
| Connection error | Check internet, firewall, or use Mock provider |
```

#### `docs/gemini.md`

````markdown
# Gemini Provider

## Overview

Google Gemini is a large language model available through Google AI Studio.

## Advantages

- Strong reasoning capabilities
- Good for complex question generation
- Large context window (1M tokens for Flash)

## Limitations

- Strict rate limits on free tier (5 RPM for some models)
- Quota resets periodically
- Requires Google account

## Getting an API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key

## Configuration

Add to `.env`:

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=models/gemini-2.0-flash
```
````

To find available models, run:

```bash
python list_models.py
```

(See `backend/list_models.py`)

## Rate Limits

Free tier: 5 requests per minute (varies by model). If you hit limits, switch to Groq or Mock for development.

## Common Issues

| Issue                | Solution                                               |
| -------------------- | ------------------------------------------------------ |
| 429 Rate Limit       | Wait 1 minute, or use Groq                             |
| 404 Model not found  | Update `GEMINI_MODEL` to a model from `list_models.py` |
| Authentication error | Verify API key is correct                              |

````

#### `docs/groq.md`

```markdown
# Groq Provider

## Overview

Groq provides ultra-fast inference for open-source models like Llama. It's recommended for OpenQuiz AI development due to its generous free tier and high speed.

## Advantages
- Very fast (up to 300+ tokens/second)
- Generous free tier
- Good for rapid iteration
- Supports Llama, Mixtral, etc.

## Getting an API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up with email or Google
3. Go to "API Keys"
4. Create a new key and copy it

## Configuration

Add to `.env`:

```env
AI_PROVIDER=groq
GROQ_API_KEY=gsk_your_key_here
GROQ_MODEL=llama-3.1-8b-instant
````

## Recommended Models

| Model                     | Best For                     |
| ------------------------- | ---------------------------- |
| `llama-3.1-8b-instant`    | Fast, free, good quality     |
| `llama-3.3-70b-versatile` | Better quality, rate limited |

## Free Tier

- No credit card required
- Generous RPM/TPM limits
- Check [Groq documentation](https://console.groq.com/docs/rate-limits) for current limits

## Why Groq is Recommended

For OpenQuiz AI development, Groq offers the best balance of speed, cost (free), and availability. Unlike Gemini, its free tier rarely blocks development due to quota exhaustion.

````

#### `docs/mock.md`

```markdown
# Mock Provider

## Overview

Mock provider generates deterministic responses without any external API call. It requires no API key, no internet, and no quota.

## When to Use

- **Frontend development** – build UI without waiting for AI
- **Offline work** – work without internet
- **Testing** – predictable responses for automated tests
- **Quota exhausted** – continue work when other providers hit limits

## Configuration

```env
AI_PROVIDER=mock
````

No other variables needed.

## Behavior

- Returns the same JSON response every time
- No delay, no errors
- Health check always passes

## Example Response

```json
{
  "success": true,
  "provider": "mock",
  "model": "mock-model",
  "response": "{\"questions\": [...]}"
}
```

## Future Enhancements

Mock may be extended to simulate:

- Network delays
- Timeouts
- Invalid responses (error testing)
- Rate limits

````

#### `docs/configuration.md`

```markdown
# Configuration Guide

## Environment Variables

Create a `.env` file in `backend/` by copying `.env.example`.

### Required for All Providers

| Variable | Description | Example |
|----------|-------------|---------|
| `AI_PROVIDER` | Active AI provider | `groq`, `gemini`, `mock` |

### Gemini-Specific

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes (for Gemini) | API key from Google AI Studio |
| `GEMINI_MODEL` | Yes (for Gemini) | Model name, e.g., `models/gemini-2.0-flash` |

### Groq-Specific

| Variable | Required | Description |
|----------|----------|-------------|
| `GROQ_API_KEY` | Yes (for Groq) | API key from Groq Console |
| `GROQ_MODEL` | Optional | Default: `llama-3.1-8b-instant` |

### Server Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` | Host to bind |
| `PORT` | `8000` | Port to bind |

## Common Mistakes

1. **Forgetting to set `AI_PROVIDER`** – required, no default
2. **Wrong provider name** – must match exactly (`groq`, `gemini`, `mock`)
3. **Missing API key** – each provider needs its own key
4. **Using `.env.example` directly** – copy to `.env` and edit

## Verifying Configuration

After setting `.env`, start the backend and visit `http://localhost:8000/ai/test`. A successful response confirms the provider is configured correctly.
````

---

### 4. Struktur Folder

```
docs/
├── ai-providers.md
├── gemini.md
├── groq.md
├── mock.md
└── configuration.md
```

---

### 5. Quick Start

Dengan dokumentasi ini, kontributor baru dapat:

1. Clone repo
2. Baca README (ringkasan)
3. Pilih provider → ikuti panduan spesifik
4. Konfigurasi `.env` (panduan di `configuration.md`)
5. Jalankan backend & frontend
6. Verifikasi dengan `http://localhost:8000/ai/test`

Dokumentasi mencakup troubleshooting, arsitektur, dan panduan menambah provider baru. Tidak ada kode yang diubah, hanya peningkatan dokumentasi yang membuat proyek siap untuk kontributor open-source.
