"""FastAPI for Personal AI Analyst."""
import logging
from typing import Any, Dict, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
app = FastAPI(title="Personal AI Analyst API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class AnalyzeRequest(BaseModel):
    n_rows: int = Field(default=200, ge=10, le=10000)

class ColumnStat(BaseModel):
    dtype: str; nulls: int; null_pct: float

class AnalyzeResponse(BaseModel):
    summary: str; n_rows: int; n_cols: int; stats: Dict[str, Any]

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest):
    from src.data_ingestion import generate_synthetic_dataframe, validate_dataframe
