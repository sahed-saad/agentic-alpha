import os
from typing import TypedDict, Annotated, Sequence
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

# Define the data structure passed between agents
class AgentState(TypedDict):
    anomaly_data: dict
    research_notes: str
    final_report: str

# Initialize the Free LLM
llm = ChatGroq(model="llama3-8b-8192", temperature=0.1)

def researcher_node(state: AgentState):
    """Agent 1: Evaluates the raw math data and contextually rationalizes it."""
    data = state['anomaly_data']
    prompt = f"Analyze this supply chain anomaly data point: {data}. Brainstorm 3 potential real-world economic risks or operational root causes for this deviation."
    
    response = llm.invoke(prompt)
    return {"research_notes": response.content}

def auditor_node(state: AgentState):
    """Agent 2: Formats the research into an institutional compliance report."""
    notes = state['research_notes']
    prompt = f"Take these research notes: '{notes}'. Format them into a professional corporate compliance audit report. Be concise, highlight financial risk, and offer immediate mitigation strategies."
    
    response = llm.invoke(prompt)
    return {"final_report": response.content}

# Construct the LangGraph State Machine
workflow = StateGraph(AgentState)

# Add nodes to graph
workflow.add_node("Researcher", researcher_node)
workflow.add_node("Auditor", auditor_node)

# Connect edges explicitly (Design over random loops)
workflow.add_edge(START, "Researcher")
workflow.add_edge("Researcher", "Auditor")
workflow.add_edge("Auditor", END)

# Compile the graph
agent_app = workflow.compile()