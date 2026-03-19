import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import streamlit as st
from src.data_ingestion import load_csv, generate_synthetic_dataframe, validate_dataframe, get_column_stats
st.title("📁 Upload Data")
uploaded = st.file_uploader("Upload CSV or JSON", type=["csv", "json"])
if uploaded:
    import pandas as pd, io
    df = pd.read_csv(io.BytesIO(uploaded.read())) if uploaded.name.endswith(".csv") else pd.read_json(io.BytesIO(uploaded.read()))
    st.dataframe(df.head())
    validation = validate_dataframe(df)
    st.json(validation)
else:
    st.info("No file uploaded — using synthetic demo data")
    df = generate_synthetic_dataframe()
    st.dataframe(df.head())
stats = get_column_stats(df)
st.subheader("Column Statistics")
for col, s in stats.items():
    st.markdown(f"**{col}** ({s['dtype']}): {s['nulls']} nulls ({s['null_pct']}%)")
