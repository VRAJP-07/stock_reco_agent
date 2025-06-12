import requests
from config import NEWS_API_KEY

def get_recent_news(ticker):
    url = f"https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&q={ticker}&language=en"
    try:
        response = requests.get(url)
        data = response.json()
        headlines = [article["title"] for article in data.get("results", [])[:5]]
        return headlines
    except Exception as e:
        return [f"Error fetching news for {ticker}: {str(e)}"]
