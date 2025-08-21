# app/backend/main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path

# --- Paths ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FRONTEND_DIR = PROJECT_ROOT / "frontend"
INDEX_FILE = FRONTEND_DIR / "index.html"
STATIC_DIR = FRONTEND_DIR / "static"

print(f"[main] FRONTEND_DIR = {FRONTEND_DIR}")
print(f"[main] INDEX_FILE   = {INDEX_FILE} (exists={INDEX_FILE.exists()})")
print(f"[main] STATIC_DIR   = {STATIC_DIR} (exists={STATIC_DIR.exists()})")

# --- App ---
app = FastAPI(title="AI Study Companion")

# Serve index.html at "/"
@app.get("/", response_class=HTMLResponse)
async def root():
    if INDEX_FILE.exists():
        return FileResponse(str(INDEX_FILE))
    return HTMLResponse(f"<pre>index.html not found at:\n{INDEX_FILE}</pre>", status_code=404)

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Summarization endpoint
class SummarizeIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize(body: SummarizeIn):
    bullets = [s.strip() for s in body.text.split(".") if s.strip()][:3]
    return {"bullets": bullets}

# --- Static files (optional) ---
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")





