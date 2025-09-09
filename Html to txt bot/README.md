# HTML to TXT Telegram Bot

This project converts HTML files to text + links using a Render-hosted API and a Telegram bot.

## Setup
1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt
3. Run API locally:
   uvicorn app:app --reload
4. Deploy API to Render
5. Update API_URL in bot.py with your Render URL
6. Run bot:
   python bot.py
   
