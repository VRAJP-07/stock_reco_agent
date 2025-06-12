import pandas as pd
import ta

def analyze_technicals(df):
    if df.empty:
        return {"signal": "no data", "details": {}}

    try:
        df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()

        # Simple logic for signal based on RSI
        rsi_value = df["rsi"].iloc[-1]
        if rsi_value > 70:
            signal = "Overbought (Possible Sell)"
        elif rsi_value < 30:
            signal = "Oversold (Possible Buy)"
        else:
            signal = "Neutral"

        support = df["Low"].rolling(window=5).min().iloc[-1]
        resistance = df["High"].rolling(window=5).max().iloc[-1]

        return {
            "signal": signal,
            "rsi": round(rsi_value, 2),
            "support": round(support, 2),
            "resistance": round(resistance, 2)
        }

    except Exception as e:
        return {"signal": "error", "error": str(e)}
