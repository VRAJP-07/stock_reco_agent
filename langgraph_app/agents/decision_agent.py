from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

with open("prompts/decision_prompt.txt", "r") as f:
    decision_template = PromptTemplate.from_template(f.read())

def decision_agent(state):
    news = state.news  # access via attribute, not .get()
    sentiment = state.sentiment

    output = llm.invoke(decision_template.format(
        news=str(news),
        sentiment=str(sentiment)
    ))
    return {"output": output.content}
