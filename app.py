import streamlit as st
import os
import requests
import random
from streamlit_lottie import st_lottie
from cat_agent import CatAgent

# --- API Key Handling ---
api_key = None
try:
    api_key = st.secrets["NEWSAPI_KEY"]  # Streamlit Cloud
except Exception:
    api_key = os.getenv("NEWSAPI_KEY")   # Local dev

agent = CatAgent()
if api_key:
    agent.api_key = api_key

# --- Helper to load Lottie ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- List of cute cat animations ---
lottie_cats = [
    "https://assets2.lottiefiles.com/packages/lf20_j1adxtyb.json",  # dancing cat
    "https://assets2.lottiefiles.com/packages/lf20_touohxv0.json",  # sleepy cat
    "https://assets2.lottiefiles.com/packages/lf20_svy4ivvy.json",  # paw swipe
    "https://assets2.lottiefiles.com/packages/lf20_cgfwf1wd.json",  # sassy tail flick
]

def random_cat_animation():
    url = random.choice(lottie_cats)
    return load_lottieurl(url)

# --- Page Config ---
st.set_page_config(page_title="CatBot News 🐾", layout="centered")

st.markdown("# CatBot News 🐱📰")
st.markdown("Your feline friend who fetches headlines and gives playful cat commentary!")

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    category = st.selectbox(
        "News category",
        ["general","technology","business","sports","entertainment","health","science"],
        index=0
    )
    num_articles = st.slider("Number of headlines to fetch", 1, 5, 3)
    st.write("⚙️ Set `NEWSAPI_KEY` in Streamlit secrets or as an environment variable.")

# --- Input ---
st.subheader("Ask your CatBot")
user_input = st.text_area(
    "Type a question or topic (e.g., 'Show me today's tech news')",
    height=100,
    placeholder="Meow! What's new today?"
)

debug_mode = st.checkbox("Show raw API response (debug)", value=False)

# --- Actions ---
col1, col2 = st.columns([1,1])

with col1:
    if st.button("Fetch news 🐾"):
        if not user_input.strip():
            st.warning("Please enter a topic or question first!")
        else:
            with st.spinner("CatBot sniffing out headlines..."):
                headlines = agent.fetch_news(
                    user_input, category=category, n=num_articles, debug=debug_mode
                )

            col_text, col_img = st.columns([3,1])
            with col_text:
                st.markdown("### CatBot says:")
                for h in headlines:
                    st.markdown(f"- {h}")
            with col_img:
                lottie_anim = random_cat_animation()
                if lottie_anim:
                    st_lottie(lottie_anim, height=150)

with col2:
    if st.button("Random Cat Fact 🐱"):
        fact = agent.random_cat_fact()
        col_text, col_img = st.columns([3,1])
        with col_text:
            st.markdown(f"### {fact}")
        with col_img:
            lottie_anim = random_cat_animation()
            if lottie_anim:
                st_lottie(lottie_anim, height=150)

# --- Footer ---
st.markdown("---")
st.markdown("💡 **Notes:** CatBot adds a playful twist to live headlines. Powered by [NewsAPI.org](https://newsapi.org).")
