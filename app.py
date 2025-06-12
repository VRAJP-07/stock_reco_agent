import streamlit as st
from main import run_analysis
from config import DEFAULT_STOCKS

st.set_page_config(page_title="📈 StockWise AI", layout="wide")

st.title("📊 StockWise AI — Intelligent Stock Market Assistant")
st.markdown("Ask about today's market sentiment, stock picks, or technicals based on live data.")

with st.form("user_input_form"):
    user_input = st.text_input(
        "Enter tickers to analyze (comma-separated):",
        value=", ".join(DEFAULT_STOCKS)
    )
    submitted = st.form_submit_button("Analyze Stocks")

if submitted and user_input:
    tickers = [t.strip().upper() for t in user_input.split(",")]
    with st.spinner("🔍 Analyzing the market..."):
        result = run_analysis(tickers)
    st.subheader("🧠 AI Recommendation:")
    st.write(result)
