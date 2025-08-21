# AI Study Companion

AI Study Companion is a lightweight **FastAPI + HTML app** that helps students turn raw text into concise, study-friendly bullet points.  

✨ Designed for quick learning and revision, it provides:
- A simple web UI (`index.html`)
- An API endpoint for summarization
- A health check endpoint  

👉 Once running locally, open the app in your browser at: [http://127.0.0.1:8001](http://127.0.0.1:8001)


## Features
- `/summarize` endpoint for bullet summaries
- Frontend `index.html` to interact with the backend
- Health check endpoint at `/health`

## How to Run
```bash
uvicorn app.backend.main:app --reload




