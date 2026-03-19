import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import streamlit as st
from src.data_ingestion import generate_synthetic_dataframe
from src.analyzer import generate_summary, compute_correlations, suggest_charts, detect_anomalies
st.title("📈 Analysis")
df = generate_synthetic_dataframe(n_rows=200)
st.markdown(generate_summary(df))
suggestions = suggest_charts(df)
st.subheader("Suggested Charts")
for s in suggestions:
    st.markdown(f"- 📊 **{s['type'].title()}**: {s['reason']}")
corr = compute_correlations(df)
if not corr.empty:
    st.subheader("Correlation Matrix")
    st.dataframe(corr.round(3))
