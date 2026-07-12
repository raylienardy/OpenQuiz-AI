# Development Guide

This document explains how to run the OpenQuiz AI project in the local development environment.

---

# Prerequisites

Install the following software:

- Python 3.10 or newer
- Node.js 22 LTS or newer
- Git

---

# Clone the Repository

```bash
git clone <repository-url>
cd openquiz-ai
```

---

# Backend Setup

Move to the backend folder.

```bash
cd backend
```

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

## Activate Virtual Environment

Command Prompt (CMD)

```cmd
.venv\Scripts\activate
```

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Git Bash

```bash
source .venv/Scripts/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

HOST=0.0.0.0
PORT=8000
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

Health Check

```
http://localhost:8000/health
```

Leave this terminal open.

---

# Frontend Setup

Open a **new terminal**.

Move to the frontend folder.

```bash
cd frontend
```

---

## Install Dependencies

```bash
npm install
```

---

## Configure Environment

Create `.env`

Example:

```env
VITE_API_URL=http://localhost:8000
```

---

## Run Frontend

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

Leave this terminal open.

---

# Daily Workflow

Every time you start working on the project:

## Terminal 1

```bash
cd backend

.venv\Scripts\activate

uvicorn app.main:app --reload
```

---

## Terminal 2

```bash
cd frontend

npm run dev
```

---

Open the browser.

```
http://localhost:5173
```

---

# Verify Everything Works

Backend

Open:

```
http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "message": "Backend is running"
}
```

---

Frontend

Open:

```
http://localhost:5173
```

Expected result:

- Home page loads
- Backend status is connected
- Upload page is accessible

---

# Updating Dependencies

Backend

```bash
pip install -r requirements.txt
```

Frontend

```bash
npm install
```

---

# Stopping the Project

Press

```
CTRL + C
```

inside each terminal.

---

# Git Workflow

Check changes

```bash
git status
```

Stage changes

```bash
git add .
```

Commit

```bash
git commit -m "feat: describe your changes"
```

Push

```bash
git push
```

---

# Current Progress

- ✅ Milestone 1 — Project Foundation
- 🚧 Milestone 2 — Material Upload

Continue from the current milestone when resuming development.
