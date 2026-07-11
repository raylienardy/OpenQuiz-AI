# OpenQuiz AI

> An open-source AI-powered question generation platform.

OpenQuiz AI is an open-source platform that helps educators, students, and developers generate high-quality questions from learning materials using Artificial Intelligence.

The project is designed to be modular, extensible, and easy to customize. It starts as a simple AI Question Generator and gradually evolves into a complete AI-powered assessment platform.

---

## ✨ Features

- Generate Multiple Choice Questions (MCQ)
- Generate Essay Questions
- Generate True/False Questions
- Generate Answer Keys
- Generate Question Explanations
- Upload PDF, DOCX, PPTX, or plain text
- AI-powered content understanding
- Export questions to PDF
- REST API for developers
- Open Dataset support

---

## 🎯 Project Goals

OpenQuiz AI aims to:

- Help teachers create assessments faster.
- Help students generate practice questions.
- Provide an open-source dataset for AI question generation.
- Become a research platform for AI in Education.
- Allow developers to build their own educational AI applications.

---

## 🏗 Project Structure

```
openquiz-ai/
│
├── frontend/
├── backend/
├── ai/
│   ├── prompting/
│   ├── rag/
│   ├── evaluation/
│   └── datasets/
│
├── datasets/
│
├── docs/
│
├── examples/
│
└── README.md
```

---

## 🧠 AI Technologies

The project is designed to support multiple AI providers.

Examples:

- Google Gemini
- OpenAI
- Claude
- Hugging Face
- Ollama
- Local LLMs

The AI backend is modular, making it easy to switch between different models.

---

## 📚 Dataset

OpenQuiz AI also provides an open dataset for educational question generation.

Example format:

```json
{
  "topic": "HTML",
  "material": "...",
  "question": "...",
  "choices": ["...", "...", "...", "..."],
  "answer": "...",
  "difficulty": "easy",
  "type": "multiple_choice"
}
```

The dataset is intended for:

- AI training
- Fine-tuning
- Evaluation
- Research
- Benchmarking

---

## 🚀 Vision

OpenQuiz AI is not just another AI application.

The long-term vision is to become a complete open-source ecosystem for AI-powered educational assessment.

Instead of building only an application, this project aims to provide:

- AI models
- Datasets
- APIs
- Tools
- Research resources
- Community contributions

---

## ❤️ Open Source

Everyone is welcome to contribute.

Ideas include:

- New datasets
- New AI models c
- Better prompts
- UI improvements
- Bug fixes
- Documentation

---

## 📄 License

MIT License
