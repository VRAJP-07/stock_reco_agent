import pandas as pd
from services.ta_utils import analyze_technicals

def sentiment_agent(state):
    prices = state.price_data  # ✅ safe now

    sentiment_results = {}
    for ticker, price_data_list in prices.items():
        df = pd.DataFrame(price_data_list)
        sentiment_results[ticker] = analyze_technicals(df)

    state.sentiment = sentiment_results
    return state  # ✅ again, return full state

