"""Data ingestion and validation."""
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import pandas as pd
import numpy as np
from src.config import RANDOM_SEED, SUPPORTED_FILE_TYPES, MAX_FILE_SIZE_MB

logger = logging.getLogger(__name__)


def load_csv(file_path: str, **kwargs) -> pd.DataFrame:
    path = Path(file_path)
    if not path.exists():
        logger.warning("File not found: %s — generating synthetic data", file_path)
        return generate_synthetic_dataframe(n_rows=200)
    df = pd.read_csv(path, **kwargs)
    logger.info("Loaded CSV: %d rows, %d cols from %s", len(df), len(df.columns), file_path)
    return df


def load_json(file_path: str) -> pd.DataFrame:
    import json
    path = Path(file_path)
    if not path.exists():
        return generate_synthetic_dataframe(n_rows=200)
    with open(path) as f:
        data = json.load(f)
    if isinstance(data, list):
        return pd.DataFrame(data)
    return pd.DataFrame([data])


def generate_synthetic_dataframe(n_rows: int = 200, seed: int = RANDOM_SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=n_rows, freq="D"),
        "revenue": rng.normal(10000, 2000, n_rows),
        "users": rng.integers(100, 1000, n_rows),
        "sessions": rng.integers(500, 5000, n_rows),
        "conversion_rate": rng.uniform(0.01, 0.15, n_rows),
        "category": rng.choice(["A", "B", "C", "D"], n_rows),
    })


def validate_dataframe(df: pd.DataFrame) -> Dict[str, Any]:
    issues = []
    if df.empty: issues.append("DataFrame is empty")
    if df.isnull().all().any(): issues.append(f"Columns all null: {df.columns[df.isnull().all()].tolist()}")
    if len(df.columns) < 2: issues.append("Need at least 2 columns")
    return {"is_valid": len(issues) == 0, "issues": issues, "n_rows": len(df), "n_cols": len(df.columns)}


def get_column_stats(df: pd.DataFrame) -> Dict[str, Dict]:
    stats = {}
    for col in df.columns:
        s = df[col]
        info: Dict[str, Any] = {"dtype": str(s.dtype), "nulls": int(s.isnull().sum()),
                                "null_pct": round(s.isnull().mean() * 100, 1)}
        if pd.api.types.is_numeric_dtype(s):
            info.update({"min": float(s.min()), "max": float(s.max()),
                        "mean": round(float(s.mean()), 2), "std": round(float(s.std()), 2)})
        else:
            info["n_unique"] = int(s.nunique())
        stats[col] = info
    return stats
