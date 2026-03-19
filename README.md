<div align="center">

# 📊 Personal AI Analyst

**AI-powered data analysis** with auto profiling, anomaly detection, trend analysis, and smart chart suggestions

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-14%20passed-success?style=flat-square)](#)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat-square&logo=pandas)](https://pandas.pydata.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=flat-square)](https://streamlit.io)

</div>

## Overview

An **AI data analyst** that ingests datasets (CSV, JSON, XLSX) and automatically generates insights including correlation analysis, anomaly detection, trend computation, and smart chart suggestions. Upload your data and get instant analysis.

## Features

- 📁 **Multi-format Ingestion** — CSV, JSON, XLSX, TXT with automatic type detection
- 🔎 **Data Profiling** — Column statistics, null analysis, data validation
- 📈 **Correlation Analysis** — Pearson correlation with heatmap visualization
- 🚨 **Anomaly Detection** — IQR and Z-score methods with configurable thresholds
- 📉 **Trend Analysis** — Rolling window trend computation with direction/magnitude
- 🎨 **Smart Chart Suggestions** — AI-recommended chart types based on data shape
- 📋 **Report Generation** — Markdown-formatted analysis reports

## Quick Start

```bash
git clone https://github.com/mohamed-elkholy95/personal-ai-analyst.git
cd personal-ai-analyst
pip install -r requirements.txt
python -m pytest tests/ -v
streamlit run streamlit_app/app.py
```

## Author

**Mohamed Elkholy** — [GitHub](https://github.com/mohamed-elkholy95) · melkholy@techmatrix.com
