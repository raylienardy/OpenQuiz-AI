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
python -m venv .venv
source .venv/bin/activate      # Windows: venv\Scripts\activate
source .venv/Scripts/activate   # Windows: venv\Scripts\activate
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
