import pytest
import pandas as pd
from src.analyzer import compute_correlations, detect_anomalies, compute_trend, generate_summary, suggest_charts

@pytest.fixture
def df():
    from src.data_ingestion import generate_synthetic_dataframe
    return generate_synthetic_dataframe(n_rows=100)

class TestCorrelations:
    def test_shape(self, df):
        corr = compute_correlations(df)
        assert corr.shape[0] >= 2

class TestAnomalies:
    def test_iqr(self):
        s = pd.Series([1,2,3,4,5,100])
        result = detect_anomalies(s)
        assert result["count"] >= 1

class TestTrend:
    def test_direction(self, df):
        trend = compute_trend(df["revenue"])
        assert trend["direction"] in ["up", "down", "flat"]

class TestSummary:
    def test_output(self, df):
        assert "# Data Analysis" in generate_summary(df)

class TestSuggestions:
    def test_returns_list(self, df):
        suggestions = suggest_charts(df)
        assert isinstance(suggestions, list)
        assert len(suggestions) > 0
