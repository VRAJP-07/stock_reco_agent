from langgraph_app.graph import stock_analysis_graph

def run_analysis(user_input):
    """
    Takes in a list of stock tickers or a single ticker as input.
    Runs the LangGraph pipeline and returns the final output from the DecisionAgent.
    """
    if isinstance(user_input, str):
        user_input = [ticker.strip().upper() for ticker in user_input.split(",")]

    result = stock_analysis_graph.invoke({
        "input": user_input
    })

    return result.get("output", "⚠️ No output generated.")


# This is the test line
