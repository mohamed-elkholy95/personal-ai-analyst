import pytest
import pandas as pd
from src.data_ingestion import generate_synthetic_dataframe, validate_dataframe, get_column_stats, load_csv

class TestGenerateSynthetic:
    def test_shape(self):
        df = generate_synthetic_dataframe(n_rows=100)
        assert df.shape == (100, 6)
    def test_columns(self):
        df = generate_synthetic_dataframe()
        assert "revenue" in df.columns
    def test_reproducible(self):
        assert generate_synthetic_dataframe(seed=42).equals(generate_synthetic_dataframe(seed=42))

class TestValidate:
    def test_valid(self):
        assert validate_dataframe(generate_synthetic_dataframe())["is_valid"]
    def test_empty(self):
        assert not validate_dataframe(pd.DataFrame())["is_valid"]

class TestColumnStats:
    def test_numeric(self):
        stats = get_column_stats(generate_synthetic_dataframe())
        assert "revenue" in stats
        assert "mean" in stats["revenue"]

class TestLoadCsv:
    def test_missing_file(self):
        df = load_csv("/nonexistent/path.csv")
        assert len(df) > 0  # falls back to synthetic
