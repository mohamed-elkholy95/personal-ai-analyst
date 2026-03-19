"""Report generation."""
import logging
from typing import Any, Dict
import pandas as pd

logger = logging.getLogger(__name__)


def generate_full_report(df: pd.DataFrame, analysis: Dict[str, Any]) -> str:
    lines = ["# Personal AI Analyst — Full Report", ""]
    lines.append(f"## Dataset Overview\n- Rows: {len(df):,}\n- Columns: {len(df.columns)}")
    numeric = df.select_dtypes(include=["number"])
    if not numeric.empty:
        lines.append(f"\n## Numeric Summary")
        lines.append(numeric.describe().to_markdown())
    if "summary" in analysis:
        lines.append(f"\n## AI Summary\n{analysis['summary']}")
    if "suggestions" in analysis:
        lines.append("\n## Suggested Charts")
        for s in analysis["suggestions"]:
            lines.append(f"- {s['type']}: {s['reason']}")
    return "\n".join(lines)
