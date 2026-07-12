# AI Providers

OpenQuiz AI uses a **provider-independent architecture** – the application never depends on a specific AI vendor. All providers implement the same interface (`BaseAIClient`), and switching between them only requires changing one environment variable.

## Supported Providers

| Provider   | API Key    | Internet     | Typical Use                            |
| ---------- | ---------- | ------------ | -------------------------------------- |
| **Groq**   | Yes (free) | Required     | Fast development, generous free tier   |
| **Gemini** | Yes (free) | Required     | Google ecosystem, strong reasoning     |
| **Mock**   | No         | Not required | Offline development, UI testing, CI/CD |

## Switching Providers

Change `AI_PROVIDER` in your `.env` file:

```env
# Use Groq
AI_PROVIDER=groq

# Use Gemini
AI_PROVIDER=gemini

# Use Mock
AI_PROVIDER=mock
```

No code changes are needed. The backend reads this variable and loads the correct client.

## How It Works

```
.env (AI_PROVIDER)
        │
        ▼
Settings (validates provider)
        │
        ▼
AIService (requests client by name)
        │
        ▼
Provider Registry (maps name → class)
        │
        ├── "gemini" → GeminiClient
        ├── "groq"   → GroqClient
        └── "mock"   → MockClient
```

All clients return the same `AIResponse` structure, so the rest of the application is completely provider-agnostic.

## Adding a New Provider

1. Create a new class in `backend/app/ai/` that implements `BaseAIClient`.
2. Register it in `backend/app/ai/providers.py`.
3. Add the provider name to `SUPPORTED_PROVIDERS` in `backend/app/config.py`.
4. Update `.env.example` with the necessary environment variables.

No changes are required in routes, services, or business logic.

## Troubleshooting

| Problem                   | Likely Cause                                                   |
| ------------------------- | -------------------------------------------------------------- |
| `Unsupported AI provider` | `AI_PROVIDER` value misspelled or not in the supported list    |
| `API key missing`         | The required key (e.g., `GROQ_API_KEY`) is not set in `.env`   |
| 429 Rate Limit            | Free tier limits reached – wait, or switch to another provider |
| Connection error          | Internet unavailable – try Mock provider for offline work      |

```

```
