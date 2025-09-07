import streamlit as st
import os
from cat_agent import CatAgent

# --- API Key Setup ---
api_key = None
try:
    api_key = st.secrets["NEWSAPI_KEY"]  # Works on Streamlit Cloud
except Exception:
    api_key = os.getenv("NEWSAPI_KEY")   # Works locally

# Pass this to the CatAgent
agent = CatAgent()
if api_key:
    agent.api_key = api_key

# --- Page Config ---
st.set_page_config(page_title="CatBot News 🐾", layout="centered")

st.markdown("# CatBot News 🐱📰")
st.markdown("Your feline friend who fetches headlines and gives playful cat commentary!")

# --- Sidebar Settings ---
with st.sidebar:
    st.header("Settings")
    category = st.selectbox(
        "News category",
        ["general","technology","business","sports","entertainment","health","science"],
        index=0
    )
    num_articles = st.slider("Number of headlines to fetch", 1, 5, 3)
    st.write("⚙️ Make sure you set `NEWSAPI_KEY` either in Streamlit secrets or as an environment variable.")

# --- User Input ---
st.subheader("Ask your CatBot")
user_input = st.text_area(
    "Type a question or topic (e.g., 'Show me today's tech news')",
    height=100,
    placeholder="Meow! What's new today?"
)

debug_mode = st.checkbox("Show raw API response (debug)", value=False)

# --- Action Buttons ---
col1, col2 = st.columns([1,1])

with col1:
    if st.button("Fetch news 🐾"):
        if not user_input.strip():
            st.warning("Please enter a topic or question first!")
        else:
            with st.spinner("CatBot sniffing out headlines..."):
                headlines = agent.fetch_news(user_input, category=category, n=num_articles, debug=debug_mode)

            st.markdown("### CatBot says:")
            for h in headlines:
                st.markdown(f"- {h}")

with col2:
    if st.button("Random Cat Fact 🐱"):
        fact = agent.random_cat_fact()
        st.markdown(f"### {fact}")

# --- Footer ---
st.markdown("---")
st.markdown("💡 **Notes:** CatBot adds a playful twist to live headlines. News is powered by [NewsAPI.org](https://newsapi.org).")
