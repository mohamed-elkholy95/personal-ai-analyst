"""Chart generation."""
import logging
from typing import Any, Dict, List, Optional
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

try:
    import plotly.graph_objects as go
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

THEME = {"paper_bgcolor": "#0e1117", "plot_bgcolor": "#262730", "font_color": "white"}


def create_line_chart(df: pd.DataFrame, x: str, y: str, title: str = "") -> Optional[Dict]:
    if not HAS_PLOTLY: return None
    fig = go.Figure(go.Scatter(x=df[x] if x in df.columns else df.index, y=df[y], mode="lines", name=y))
    fig.update_layout(title=title or f"{y} over {x}", **THEME)
    return {"fig": fig, "type": "line"}


def create_bar_chart(df: pd.DataFrame, x: str, y: str, title: str = "") -> Optional[Dict]:
    if not HAS_PLOTLY: return None
    fig = px.bar(df, x=x, y=y, title=title or f"{y} by {x}")
    fig.update_layout(**THEME)
    return {"fig": fig, "type": "bar"}


def create_scatter_chart(df: pd.DataFrame, x: str, y: str, title: str = "") -> Optional[Dict]:
    if not HAS_PLOTLY: return None
    fig = px.scatter(df, x=x, y=y, title=title or f"{x} vs {y}", color_continuous_scale="Blues")
    fig.update_layout(**THEME)
    return {"fig": fig, "type": "scatter"}


def create_histogram(df: pd.DataFrame, x: str, title: str = "") -> Optional[Dict]:
    if not HAS_PLOTLY: return None
    fig = px.histogram(df, x=x, title=title or f"Distribution of {x}", nbins=30)
    fig.update_layout(**THEME)
    return {"fig": fig, "type": "histogram"}
