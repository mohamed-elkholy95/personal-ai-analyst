import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
import streamlit as st
st.title("📊 Personal AI Analyst — Overview")
st.markdown("Upload data and get instant analysis with AI-generated insights and visualizations.")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Features"); st.markdown("- Auto data profiling\n- Correlation analysis\n- Anomaly detection\n- Trend analysis\n- Smart chart suggestions")
with col2:
    st.subheader("Supported Formats"); st.markdown("- CSV, JSON, XLSX, TXT\n- Automatic type detection\n- Handle missing values\n- Statistical summaries")
st.metric("Supported Chart Types", "6")
st.metric("Max File Size", "100 MB")
