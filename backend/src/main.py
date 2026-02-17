# backend/src/main.py
from fastapi import FastAPI

app = FastAPI(title="TeamUp Dev API")

@app.get("/")
def root():
    return {"message": "TeamUp Dev API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}