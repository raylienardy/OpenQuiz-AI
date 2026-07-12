# Groq Provider

## Overview

Groq provides lightning‑fast inference for open‑source models (Llama, Mixtral, etc.). It is the **recommended provider** for OpenQuiz AI development because of its generous free tier and high speed.

## Getting an API Key

1. Visit [Groq Console](https://console.groq.com).
2. Sign up (email or Google account).
3. Navigate to **API Keys** and create a new key.

## Configuration

Add these to `backend/.env`:

```env
AI_PROVIDER=groq
GROQ_API_KEY=gsk_your_key_here
GROQ_MODEL=llama-3.1-8b-instant
```

`GROQ_MODEL` is optional; the default is `llama-3.1-8b-instant`, which offers excellent speed and is free to use.

## Recommended Models

| Model                     | Quality | Speed     | Free Tier |
| ------------------------- | ------- | --------- | --------- |
| `llama-3.1-8b-instant`    | Good    | Very fast | Yes       |
| `llama-3.3-70b-versatile` | Better  | Fast      | Limited   |

## Why Groq?

- **No credit card** required for the free tier.
- **High rate limits** compared to Gemini’s free tier – you’re less likely to be blocked during development.
- **Latency** is extremely low, making it ideal for interactive applications.

## Troubleshooting

| Error                    | Solution                                                                                       |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| 401 Authentication error | Verify your `GROQ_API_KEY`; the key should start with `gsk_`                                   |
| 429 Rate limit           | You’ve exceeded the free tier limit – wait a few seconds and retry                             |
| Model not found          | Check the model name or consult the [Groq documentation](https://console.groq.com/docs/models) |
