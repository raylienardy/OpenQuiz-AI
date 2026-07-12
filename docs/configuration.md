# Configuration Guide

All configuration is done through environment variables, typically stored in a `.env` file inside the `backend/` directory.

## Creating Your `.env`

1. Copy the example file:

   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in the required values.

## Environment Variables

### AI Provider Selection

| Variable      | Required | Description                                           |
| ------------- | -------- | ----------------------------------------------------- |
| `AI_PROVIDER` | **Yes**  | Must be one of: `groq`, `gemini`, `mock`. No default. |

### Gemini

| Variable         | Required                 | Description                                                         |
| ---------------- | ------------------------ | ------------------------------------------------------------------- |
| `GEMINI_API_KEY` | Yes (if provider=gemini) | API key from [Google AI Studio](https://aistudio.google.com/apikey) |
| `GEMINI_MODEL`   | Yes (if provider=gemini) | Model identifier, e.g., `models/gemini-2.0-flash`                   |

### Groq

| Variable       | Required               | Description                                           |
| -------------- | ---------------------- | ----------------------------------------------------- |
| `GROQ_API_KEY` | Yes (if provider=groq) | API key from [Groq Console](https://console.groq.com) |
| `GROQ_MODEL`   | No                     | Default: `llama-3.1-8b-instant`                       |

### Mock

No additional variables are required. Just set `AI_PROVIDER=mock`.

### Server

| Variable | Default   | Description  |
| -------- | --------- | ------------ |
| `HOST`   | `0.0.0.0` | Host address |
| `PORT`   | `8000`    | Port number  |

## Common Mistakes

- **Missing `AI_PROVIDER`** – the application will refuse to start.
- **Wrong provider name** – must be exactly `groq`, `gemini`, or `mock` (lowercase).
- **Forgetting to copy `.env.example`** – the `.env` file is not created automatically.
- **Using the example API keys** – replace them with your own credentials.

## Verifying Configuration

Start the backend and navigate to `http://localhost:8000/ai/test`. A successful response indicates the provider is configured correctly.
