import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TON_API_KEY = os.getenv("TON_API_KEY")
TON_API_URL = "https://toncenter.com/api/v2"
