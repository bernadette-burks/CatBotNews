# CatBotNews

\# CatBot News Agent 🐱📰



\*\*Purpose:\*\*  

CatBot News is a playful cat-themed agent that fetches live news headlines from NewsAPI.org and delivers them with expressive, whimsical cat commentary. If a search query returns no results, it automatically fetches top headlines in the selected category so CatBot always has something to say!



\*\*Files included:\*\*  

\- `app.py` — Streamlit UI with debug mode checkbox

\- `cat\_agent.py` — CatBot logic with fallback behavior

\- `requirements.txt`

\- `README.md`

\- `LICENSE` (MIT)

\- `sample\_screenshots/sample\_ui\_placeholder.png`



\*\*Setup \& Run:\*\*  



Run Windows PowerShell "as Administrator" and paste the following scripts one at a time to configure and launch this fun little app!
Requires: Python (https://www.python.org/downloads/)

-------1---
python -m venv .venv
.venv\\Scripts\\Activate.ps1

-------2---
pip install -r requirements.txt

-------3---
$env:NEWSAPI\_KEY="af80f81999534abf8b8195f00c9fcfa4"
streamlit run app.py





\*\*Notes:\*\*  

\- Debug mode shows raw JSON from NewsAPI if checked.  

\- Auto-fallback ensures CatBot always has headlines to share.







Bernadette Burks
September 7, 2025
New England College Graduate Studies

