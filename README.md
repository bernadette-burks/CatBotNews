# CatBotNews
Live news feed (w/ basic search function) delivered by a "cat" 🐱

Run Windows PowerShell "as Administrator" and paste the following scripts one at a time to configure and launch this fun little app!
Requires: Python (https://www.python.org/downloads/)

-------1---
python -m venv .venv
.venv\Scripts\Activate.ps1

-------2---
pip install -r requirements.txt

-------3---
$env:NEWSAPI_KEY="af80f81999534abf8b8195f00c9fcfa4"
streamlit run app.py


Bernadette Burks
September 7, 2025
New England College Graduate Studies

