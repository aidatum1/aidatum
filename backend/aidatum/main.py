from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models, api
from .database import engine
from .config import get_settings

settings = get_settings()

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Datum API",
    description="API for aggregating and presenting recall data to consumers",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Datum API",
        "docs": "/docs",
        "version": "0.1.0"
    }