from services.news_fetcher import get_recent_news
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

# Load prompt template
with open("prompts/news_prompt.txt", "r") as f:
    prompt_template = PromptTemplate.from_template(f.read())

def news_agent(state):
    tickers = state.input
    if isinstance(tickers, str):
        tickers = [tickers]

    news_dict = {}  # ✅ Use dictionary instead of list
    for ticker in tickers:
        headlines = get_recent_news(ticker)
        if headlines:
            summary = llm.invoke(prompt_template.format(
                ticker=ticker,
                headlines="\n".join(headlines)
            ))
            news_dict[ticker] = summary.content
        else:
            news_dict[ticker] = "No recent news found."

    return {"news": news_dict}  # ✅ Return a single merged dictionary
