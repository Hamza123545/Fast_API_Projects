from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to FastDCA API",
    }


@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = Query(None)):
    data = {
        "item_id": item_id,
        "query": q or "No query provided",
    }
    return {
        "success": True,
        "data": data
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/status")
def get_status():
    return JSONResponse(content={
        "success": True,
        "service": "FastDCA API",
        "uptime": "Stable",
        "version": "0.1.0"
    }, status_code=200)
