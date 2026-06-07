# Agentic Alpha: Automated Supply Chain Compliance Auditor

An automated system that generates synthetic supply chain shipping cost data, isolates statistically significant anomalies using Z-scores, and passes those risks through a coordinated LLM state machine to draft institutional corporate compliance audit reports.

---

## System Architecture

The application combines data science pipelines with an asynchronous multi-agent system exposed via a web API:

1. **Statistical Anomaly Detection (`analytics.py`):** Generates synthetic shipping cost time-series datasets and isolates anomalies using a vectorized mathematical $Z$-score formula where $|Z| > 3$.


2. **LangGraph State Machine (`agent.py`):**
* **Researcher Node:** Examines isolated data spikes or drops and derives 3 localized macro-economic or operational root causes using `llama3-8b-8192`.


* **Auditor Node:** Evaluates the researcher's observations and formats them into formal corporate compliance documentation highlighting financial risk mitigation.




3. **API Service (`main.py`):** A FastAPI server that runs the combined pipeline orchestration on-demand via an HTTP endpoint.

## Live Deployment Link:

* https://saad-com-agentic-alpha.hf.space/docs#/default/run_audit_run_audit_get
---

## Getting Started

### Prerequisites

* Python 3.10+
* A Groq API Key (Set up as an environment variable: `GROQ_API_KEY`)

### Installation and Execution

1. **Clone the repository:**
```bash
git clone https://github.com/sahed-saad/agentic-alpha.git
cd agentic-alpha

```



```

2. **Install dependencies:**
   ```bash
pip install -r requirements.txt

```

3. **Set your environment variable:**
```bash
export GROQ_API_KEY="your_groq_api_key_here"

```



```

4. **Launch the API Server:**
   ```bash
   uvicorn main:app --reload

```

---

## API Endpoints

### Run Audit

* **Endpoint:** `GET /run-audit`

* **Description:** Generates the time-series shipping dataset, isolates anomalies, streams them sequentially through the LangGraph workflow, and returns formal audit reports.



#### Sample JSON Response Structure:

```json
{
  "status": "Success",
  "total_anomalies_audited": 2,
  "reports": [
    {
      "date": "2026-02-15 00:00:00",
      "cost": 1200.0,
      "audit": "### CORPORATE COMPLIANCE AUDIT REPORT\n\n**Financial Risk Profile:** Severe Cost Overrun...\n\n**Immediate Mitigation Strategies:**..."
    }
  ]
}

```
