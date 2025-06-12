from langgraph.graph import StateGraph
from typing import List, Dict, Union, Any
from pydantic import BaseModel
from langgraph_app.agents.news_agent import news_agent
from langgraph_app.agents.price_agent import price_agent
from langgraph_app.agents.sentiment_agent import sentiment_agent
from langgraph_app.agents.decision_agent import decision_agent

class StockAgentState(BaseModel):
    input: List[str]
    news: Dict[str, str] = {}
    price_data: Dict[str, List[Dict[str, Any]]] = {}
    sentiment: dict[str, dict[str, Any]] = {}
    output: Union[str, None] = None

workflow = StateGraph(StockAgentState)

workflow.add_node("NewsAgent", news_agent)
workflow.add_node("PriceAgent", price_agent)
workflow.add_node("SentimentAgent", sentiment_agent)
workflow.add_node("DecisionAgent", decision_agent)

# Set transitions
workflow.set_entry_point("NewsAgent")
workflow.add_edge("NewsAgent", "PriceAgent")
workflow.add_edge("PriceAgent", "SentimentAgent")
workflow.add_edge("SentimentAgent", "DecisionAgent")
workflow.set_finish_point("DecisionAgent")

# Build graph
stock_analysis_graph = workflow.compile()
