# OpenQuiz AI — Version 1.0 Milestones

> **Goal:** Build a complete Minimum Viable Product (MVP) that allows users to upload learning materials and generate AI-powered questions using Google Gemini.

---

# Overview

Version 1 focuses on building the complete core workflow.

```
Upload Material
      │
      ▼
Extract Text
      │
      ▼
Google Gemini
      │
      ▼
Generate Questions
      │
      ▼
Preview Result
      │
      ▼
Export PDF
```

Everything outside this workflow belongs to future versions.

---

# Milestone 1 — Project Foundation

## Objective

Create a clean project foundation and ensure both frontend and backend can communicate successfully.

## Tasks

- Initialize Git repository
- Create project folder structure
- Configure React + Vite
- Configure FastAPI
- Create development environment
- Configure CORS
- Verify frontend can communicate with backend
- Create basic landing page
- Create backend health check endpoint

## Expected Output

- Frontend runs successfully
- Backend runs successfully
- API connection works
- Development environment is ready

## Definition of Done

- React is running
- FastAPI is running
- `GET /health` returns success
- Frontend receives backend response

---

# Milestone 2 — Material Upload

## Objective

Allow users to upload learning materials.

## Supported Formats

- PDF
- DOCX
- TXT

## Tasks

- Upload page
- Drag & Drop upload
- File picker
- File validation
- Maximum file size validation
- Supported file type validation

## Expected Output

Users can upload learning materials successfully.

## Definition of Done

- All supported file types upload successfully
- Invalid files are rejected
- User receives clear feedback

---

# Milestone 3 — Text Extraction

## Objective

Convert uploaded files into plain text.

## Tasks

- PDF extraction
- DOCX extraction
- TXT reading
- Text cleaning
- Text preview

## Expected Output

Extracted text is displayed correctly.

## Definition of Done

- All supported formats are converted into readable text
- Empty documents are handled properly
- Extraction errors are handled gracefully

---

# Milestone 4 — Gemini Integration

## Objective

Connect the backend to Google Gemini.

## Tasks

- Configure Gemini API
- API key management
- Test connection
- Basic prompt
- Receive structured response

## Expected Output

Gemini successfully responds to requests.

## Definition of Done

- Connection established
- Error handling implemented
- JSON response received successfully

---

# Milestone 5 — Question Generator

## Objective

Generate educational questions using AI.

## Supported Question Types

- Multiple Choice
- Essay
- True / False

## Tasks

- Prompt engineering
- Number of questions selection
- Question type selection
- JSON output validation

## Expected Output

AI generates structured questions.

## Definition of Done

- Questions are generated successfully
- Output follows predefined JSON format
- Invalid AI responses are handled

---

# Milestone 6 — Result Viewer

## Objective

Display generated questions in a clean interface.

## Tasks

- Question list
- Answer display
- Loading state
- Error state
- Copy to clipboard

## Expected Output

Users can review generated questions before exporting.

## Definition of Done

- Questions display correctly
- UI remains responsive
- Loading and error states work correctly

---

# Milestone 7 — PDF Export

## Objective

Allow users to download generated questions.

## Tasks

- Generate PDF
- Clean document layout
- Download button

## Expected Output

Users receive a properly formatted PDF.

## Definition of Done

- PDF downloads successfully
- Questions and answers are formatted correctly
- Layout is readable

---

# Milestone 8 — UI Polish

## Objective

Improve user experience.

## Tasks

- Responsive layout
- Better typography
- Better spacing
- Loading animations
- Empty states
- Success messages
- Error messages

## Expected Output

The application feels polished and user-friendly.

## Definition of Done

- Responsive on desktop and tablet
- UI is visually consistent
- User interactions feel smooth

---

# Milestone 9 — Testing

## Objective

Ensure the application works reliably.

## Tasks

- Upload testing
- Extraction testing
- AI generation testing
- Export testing
- Error handling testing
- Edge case testing

## Expected Output

Major workflows function correctly without critical issues.

## Definition of Done

- Core workflow passes all manual tests
- No critical bugs remain
- Error handling works as expected

---

# Milestone 10 — Release Version 1.0

## Objective

Prepare the first public release.

## Tasks

- Final cleanup
- Update README
- Update documentation
- Capture screenshots
- Record demo video
- Tag version v1.0.0
- Publish to GitHub

## Expected Output

OpenQuiz AI Version 1.0 is publicly available.

## Definition of Done

- Repository is organized
- Documentation is complete
- Demo is available
- Version 1.0 is ready for users

---

# Version 1 Success Criteria

Version 1 is considered complete when a user can:

1. Open the application.
2. Upload a PDF, DOCX, or TXT file.
3. Extract the document text.
4. Generate AI-powered questions using Google Gemini.
5. Preview the generated questions.
6. Export the questions as a PDF.

If all six steps work reliably, Version 1 is successfully completed.

---

# Out of Scope

The following features are intentionally excluded from Version 1 and will be considered for future releases:

- User authentication
- Database
- User history
- Question bank
- Cloud storage
- Multi-provider AI
- Ollama integration
- RAG
- Vector database
- Fine-tuning
- Multi-language support
- Difficulty classification
- Bloom Taxonomy classification
- AI evaluation
- Plugin system
- Collaboration features
- Admin dashboard

Keeping Version 1 focused ensures a stable foundation for future development.
