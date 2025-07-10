from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.generate import router as generate_router

app = FastAPI(
    title="NeuroNote API",
    description="An AI-powered study assistant that summarizes content and generates quizzes and flashcards.",
    version="1.0.0"
)

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev; tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the /api/generate route
app.include_router(generate_router, prefix="/api")

# Root route for testing
@app.get("/")
def home():
    return {"message": "NeuroNote API is running!"}
