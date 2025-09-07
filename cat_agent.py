import os
import random
import requests

class CatAgent:
    CAT_COMMENTS = [
        "Purrhaps you should read this! 😸",
        "Meow! This caught my attention 🐾",
        "I batted at this headline, take a look! 🐱",
        "Hiss! But interesting nonetheless! 🐾",
        "Tail twitching over this one! 😺"
    ]

    CAT_FACTS = [
        "Cats sleep 12–16 hours a day. 💤",
        "A group of cats is called a clowder. 😸",
        "Cats have five toes on their front paws, but only four on the back. 🐾",
        "A cat can rotate its ears 180 degrees. 😺",
        "Whiskers help cats measure gaps and spaces! 🐱"
    ]

    NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"

    def __init__(self):
        # Pull API key from environment (works with Streamlit secrets too!)
        self.api_key = os.getenv("NEWSAPI_KEY", None)

    def fetch_news(self, topic: str, category="general", n=3, debug=False):
        if not self.api_key:
            return [f"Meow! 🐾 I need a `NEWSAPI_KEY` to fetch live news. Here's a pretend headline about '{topic}'!"]

        params = {
            "apiKey": self.api_key,
            "q": topic,
            "category": category,
            "pageSize": n,
            "language": "en"
        }

        try:
            resp = requests.get(self.NEWSAPI_ENDPOINT, params=params, timeout=10)
            data = resp.json()

            if debug:
                return [f"DEBUG: {data}"]

            articles = data.get("articles", [])

            # If no results, retry with just category
            if not articles:
                fallback_params = {
                    "apiKey": self.api_key,
                    "category": category,
                    "pageSize": n,
                    "language": "en"
                }
                resp = requests.get(self.NEWSAPI_ENDPOINT, params=fallback_params, timeout=10)
                data = resp.json()
                articles = data.get("articles", [])

                if not articles:
                    return [f"Meow! 🐾 No articles available right now for '{topic}' or category '{category}'. Try again later!"]

                # Add fallback message
                headlines = [f"Meow! Couldn’t find news for '{topic}', so here are some '{category}' headlines instead:"]
            else:
                headlines = []

            # Add cat commentary to each article
            for a in articles[:n]:
                title = a.get("title", "No title")
                comment = random.choice(self.CAT_COMMENTS)
                headlines.append(f"{title} — {comment}")

            return headlines

        except Exception as e:
            return [f"Oops! CatBot got distracted 😿 Error: {e}"]

    def random_cat_fact(self):
        return random.choice(self.CAT_FACTS)
