import streamlit as st
import random, requests

class CatAgent:
    CAT_COMMENTS = [
        "Purrhaps you should read this! 😸",
        "Meow! This caught my attention 🐾",
        "I batted at this headline, take a look! 🐱",
        "Hiss! But interesting nonetheless! 🐾",
        "Tail twitching over this one! 😺"
    ]

    CAT_FACTS = [
        "Cats sleep 12-16 hours a day. 💤",
        "A group of cats is called a clowder. 😸",
        "Cats have five toes on front paws, four on back. 🐾",
        "A cat can rotate its ears 180 degrees. 😺",
        "Whiskers help cats measure gaps and spaces! 🐱"
    ]

    NEWSAPI_ENDPOINT = "https://newsapi.org/v2/top-headlines"

    def __init__(self):
        self.api_key = os.getenv("NEWSAPI_KEY", None)

    def fetch_news(self, topic: str, category="general", n=3, debug=False):
        if not self.api_key:
            return [f"Meow! 🐾 I need a NEWSAPI_KEY to fetch live news. Here's a pretend headline about '{topic}'." for _ in range(n)]

        params = {"apiKey": self.api_key, "q": topic, "category": category, "pageSize": n, "language":"en"}
        try:
            resp = requests.get(self.NEWSAPI_ENDPOINT, params=params)
            data = resp.json()
            if debug:
                return [f"DEBUG: {data}"]

            articles = data.get("articles", [])

            # Fallback if no articles found
            headlines = []
            if not articles:
                fallback_params = {"apiKey": self.api_key, "category": category, "pageSize": n, "language": "en"}
                resp = requests.get(self.NEWSAPI_ENDPOINT, params=fallback_params)
                data = resp.json()
                articles = data.get("articles", [])
                if articles:
                    fallback_msg = f"Meow! Couldn't find articles for '{topic}', so here are the top headlines in '{category}' instead:"
                    headlines.append(fallback_msg)
                else:
                    return [f"Meow! 🐾 No articles available at the moment. Try again later!"]

            # Add cat commentary
            for a in articles:
                title = a.get("title","No title")
                comment = random.choice(self.CAT_COMMENTS)
                headlines.append(f"{title} — {comment}")

            return headlines[:n]

        except Exception as e:
            return [f"Oops! CatBot got distracted 😿 Error: {e}"]

    def random_cat_fact(self):
        return random.choice(self.CAT_FACTS)
