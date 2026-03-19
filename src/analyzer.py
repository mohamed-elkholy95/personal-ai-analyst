"""Data analysis engine."""
import logging
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


def compute_correlations(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    numeric = df.select_dtypes(include=[np.number])
    if numeric.shape[1] < 2:
        return pd.DataFrame()
    return numeric.corr(method=method).round(4)


def detect_anomalies(series: pd.Series, method: str = "iqr", threshold: float = 1.5) -> Dict[str, Any]:
    if method == "iqr":
        q1, q3 = series.quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
        anomalies = series[(series < lower) | (series > upper)]
    else:
        mean, std = series.mean(), series.std()
        anomalies = series[abs(series - mean) > threshold * std]
    return {"count": int(len(anomalies)), "indices": anomalies.index.tolist()[:20],
            "values": anomalies.values.tolist()[:20]}


def compute_trend(series: pd.Series, window: int = 7) -> Dict[str, Any]:
    rolling = series.rolling(window=window).mean()
    trend = rolling.iloc[-1] - rolling.iloc[window]
    direction = "up" if trend > 0 else "down" if trend < 0 else "flat"
    return {"direction": direction, "magnitude": round(float(trend), 2),
            "window": window, "current_avg": round(float(rolling.iloc[-1]), 2)}


def generate_summary(df: pd.DataFrame) -> str:
    lines = [f"# Data Analysis Summary", f"**Rows:** {len(df):,} | **Columns:** {len(df.columns)}", ""]
    numeric = df.select_dtypes(include=[np.number])
    for col in numeric.columns[:5]:
        lines.append(f"- **{col}:** mean={numeric[col].mean():.2f}, std={numeric[col].std():.2f}")
    corr = compute_correlations(df)
    if not corr.empty and corr.shape[0] >= 2:
        top_corr = corr.abs().unstack().sort_values(ascending=False).drop_duplicates()
        if len(top_corr) > 1:
            pair = top_corr.index[1]
            lines.append(f"- **Strongest correlation:** {pair[0]} ↔ {pair[1]} ({corr.loc[pair[0], pair[1]]:.2f})")
    return "\n".join(lines)


def suggest_charts(df: pd.DataFrame) -> List[Dict[str, str]]:
    suggestions = []
    numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    categoric = df.select_dtypes(exclude=[np.number]).columns.tolist()
    if len(numeric) >= 2:
        suggestions.append({"type": "scatter", "x": numeric[0], "y": numeric[1], "reason": "Two numeric columns"})
    if len(numeric) >= 1 and len(categoric) >= 1:
        suggestions.append({"type": "bar", "x": categoric[0], "y": numeric[0], "reason": "Numeric by category"})
    if len(numeric) >= 1:
        suggestions.append({"type": "histogram", "x": numeric[0], "reason": "Distribution of numeric data"})
    if len(categoric) >= 1:
        suggestions.append({"type": "pie", "x": categoric[0], "reason": "Category distribution"})
    if len(numeric) >= 1:
        suggestions.append({"type": "line", "x": df.index.name or "index", "y": numeric[0], "reason": "Time series"})
    return suggestions[:5]
