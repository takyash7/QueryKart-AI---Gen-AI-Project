import streamlit as st

st.set_page_config(
    page_title="QueryKart AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 QueryKart AI")

st.subheader(
    "AI Powered Retail Database Assistant"
)

st.markdown("---")

st.markdown(
    """
# 👋 Welcome to QueryKart AI

QueryKart AI is an AI-powered SQL assistant.

It converts natural language questions into SQL queries
and fetches answers directly from the database.

## 🚀 Features

- Natural Language to SQL
- AI Generated Queries
- Sales Analytics
- Inventory Analysis
- Customer Insights
- Revenue Intelligence
- Payment Analytics

Use the sidebar to navigate between pages.
"""
)

st.success("✅ System Ready")

st.markdown("---")

st.caption(
    "Built by Yash Tak"
)