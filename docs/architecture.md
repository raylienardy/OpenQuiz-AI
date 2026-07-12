# Architecture

## High‑Level Overview

OpenQuiz AI follows a layered architecture that separates presentation, business logic, and infrastructure.

```
┌─────────────────────────────────────────────┐
│               Frontend (React)              │
│   Upload UI, Preview, Question Viewer       │
└──────────────────────┬──────────────────────┘
                       │ HTTP/REST
┌──────────────────────▼──────────────────────┐
│              Backend (FastAPI)              │
│                                             │
│  ┌───────────────┐   ┌───────────────────┐  │
│  │    Routes     │   │ AI Provider Layer │  │
│  └───────┬───────┘   └─────────┬─────────┘  │
│          │                     │            │
│  ┌───────▼─────────────────────▼─────────┐  │
│  │           Service Layer               │  │
│  │  UploadService, ExtractionService,    │  │
│  │  AIService                            │  │
│  └───────────────────┬───────────────────┘  │
│                      │                      │
│  ┌───────────────────▼───────────────────┐  │
│  │         Domain / Utilities            │  │
│  │  Extractors, Cleaners, Validators     │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

## Key Design Decisions

### Provider‑Independent AI

All AI providers implement `BaseAIClient`. The application asks `AIService` for a response; `AIService` delegates to a provider obtained from the `Provider Registry`. No business logic depends on a specific vendor.

### Layered Backend

- **Routes** – only handle HTTP concerns (parsing requests, returning responses).
- **Services** – coordinate business operations (e.g., `ExtractionService` runs the right extractor and then the cleaning pipeline).
- **Extractors / AI Clients** – low‑level implementations that can be replaced without affecting upper layers.

### Stateless

Version 1 stores nothing permanently. Files are processed in memory. Future milestones will introduce storage.

### Configuration over Code

All environment‑specific values (API keys, model names, CORS origins) live in `.env` and are loaded via Pydantic’s `Settings`. No hardcoded values exist in the source.

## Adding a Feature (example)

1. Create the service/logic in the appropriate `services/` or `ai/` module.
2. Expose it through a route in `api/`.
3. Register the route in `main.py`.
4. Document the new endpoint in `docs/api.md`.
