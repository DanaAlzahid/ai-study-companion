# AI Study Companion

A FastAPI + HTML project for summarizing text into study-friendly bullet points.

## Features
- `/summarize` endpoint for bullet summaries
- Frontend `index.html` to interact with the backend
- Health check endpoint at `/health`

## How to Run
```bash
uvicorn app.backend.main:app --reload
