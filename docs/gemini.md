# Gemini Provider

## Overview

Google Gemini is a family of large language models accessible through the Gemini API. In OpenQuiz AI, Gemini can be used to generate questions, answers, and explanations from uploaded documents.

## Getting an API Key

1. Go to [Google AI Studio](https://aistudio.google.com/apikey).
2. Sign in with your Google account.
3. Click **Create API Key** and copy it.

## Configuration

Set these variables in `backend/.env`:

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=models/gemini-2.0-flash
```

To find available models for your account, run the helper script:

```bash
cd backend
python list_models.py
```

Choose a model from the output and place it in `GEMINI_MODEL`.

## Rate Limits

The free tier imposes strict limits (e.g., 5 requests per minute for some models). If you encounter a `429` error, wait a minute and try again, or switch to **Groq** or **Mock** for uninterrupted development.

## Advantages

- Strong at reasoning and complex instructions.
- Large context window (up to 1 million tokens for Flash models).
- Free tier available for testing.

## Limitations

- Rate limits can interrupt development.
- Model names occasionally change; use `list_models.py` to get the current list.
- Requires internet access.

## Troubleshooting

| Error                | Solution                                                   |
| -------------------- | ---------------------------------------------------------- |
| 404 Model not found  | Update `GEMINI_MODEL` using the list from `list_models.py` |
| 429 Rate limit       | Wait, or switch to another provider                        |
| Authentication error | Check `GEMINI_API_KEY`; ensure it’s copied correctly       |
