import os
import streamlit as st
from cat_agent import CatAgent

import streamlit as st
api_key = st.secrets["OPENAI_API_KEY"]

import os
api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(page_title="CatBot News 🐾", layout="centered")

st.markdown("# CatBot News 🐱📰")
st.markdown("Your feline friend who fetches headlines and gives playful cat commentary!")

agent = CatAgent()

with st.sidebar:
    st.header("Settings")
    category = st.selectbox("News category", ["general","technology","business","sports","entertainment","health","science"], index=0)
    num_articles = st.slider("Number of headlines to fetch", 1, 5, 3)
    st.write("Make sure you set `NEWSAPI_KEY` in your environment to fetch live news.")

st.subheader("Ask your CatBot")
user_input = st.text_area("Type a question or topic (e.g., 'Show me today's tech news')", height=100, placeholder="Meow! What's new today?")

debug_mode = st.checkbox("Show raw API response (debug)", value=False)

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

st.markdown("---")
st.markdown("💡 **Notes:** Make sure `NEWSAPI_KEY` is set as an environment variable. The CatBot adds a playful cat twist to each headline!")
