from services.stock_data import get_price_data

def price_agent(state):
    tickers = state.input
    if isinstance(tickers, str):
        tickers = [tickers]

    prices = {}

    for ticker in tickers:
        df = get_price_data(ticker)
        if df is not None and not df.empty:
            prices[ticker] = df.to_dict(orient="records")
        else:
            print(f"[ERROR] No price data for {ticker}")
            prices[ticker] = []

    # ✅ Correct: mutate and return the full state
    state.price_data = prices
    return state  # ✅ MUST return the full state object
