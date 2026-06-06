from fastapi import FastAPI
from analytics import generate_mock_data, find_anomalies
from agent import agent_app

app = FastAPI(title="Agentic Alpha API")

@app.get("/run-audit")
def run_audit():
    # 1. Fetch and process data with pandas/numpy
    df = generate_mock_data()
    anomalies = find_anomalies(df)
    
    reports = []
    # 2. Process detected anomalies through the agent state machine
    for anomaly in anomalies:
        initial_state = {"anomaly_data": anomaly, "research_notes": "", "final_report": ""}
        output = agent_app.invoke(initial_state)
        reports.append({
            "date": str(anomaly['Date']),
            "cost": anomaly['Shipping_Cost'],
            "audit": output['final_report']
        })
        
    return {"status": "Success", "total_anomalies_audited": len(reports), "reports": reports}