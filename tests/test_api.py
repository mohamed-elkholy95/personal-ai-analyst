import pytest
from fastapi.testclient import TestClient
from src.api.main import app
client = TestClient(app)

class TestHealth:
    def test_health(self):
        assert client.get("/health").status_code == 200

class TestAnalyze:
    def test_analyze(self):
        resp = client.post("/analyze", json={"n_rows": 100})
        assert resp.status_code == 200
        data = resp.json()
        assert data["n_rows"] == 100
        assert "summary" in data
