import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Constants
DEFAULT_STOCKS = ["AAPL", "TSLA", "GOOGL"]
LOOKBACK_DAYS = 5
