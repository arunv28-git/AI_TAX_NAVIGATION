# 🧠 AI Current Tax Regime Navigator

An intelligent tax comparison and compliance-aware system that:

- Compares Old vs New Indian tax regimes
- Detects compliance risks
- Uses RAG (Retrieval-Augmented Generation) for grounded explanations
- Automatically triggers n8n workflows when risks are detected
- Uses FastAPI (backend) + Streamlit (frontend)

---

# 🔄 Complete Workflow

## 1️⃣ User Input (Frontend – Streamlit)

The user enters:

- Annual Income
- Total Deductions
- Whether HRA is claimed

When the user clicks **Analyze**, the frontend sends a POST request to the FastAPI backend.

---

## 2️⃣ API Layer (FastAPI – `main.py`)

The `/analyze` endpoint:

1. Receives JSON input
2. Passes data to the Tax Agent
3. Returns structured response

This layer acts as a bridge between UI and AI logic.

---

## 3️⃣ Agent Layer (Core Brain – `agent.py`)

This file orchestrates the entire system.

It performs:

### A. Tax Calculation

Uses:

- `tax_calculator.py`

Calculates:

- Old regime tax
- New regime tax

This is deterministic logic (no AI here).

---

### B. Compliance Risk Detection

Uses:

- `risk_engine.py`

Detects:

- 80C exceeding ₹1.5 lakh
- HRA misuse in New regime
- Invalid deductions

Returns:

```json
"risks": []
```

or a list of risk messages.

---

### C. RAG-Based Explanation

Uses:

- `rag_engine.py`

Steps:

1. Loads official tax documents
2. Splits them into chunks
3. Creates embeddings
4. Builds vector store
5. Retrieves relevant sections
6. Sends retrieved content to LLM
7. Generates grounded explanation

Prevents hallucination.

---

### D. Automation Trigger (Agentic Behavior)

If risks exist:

```
if risks:
    trigger_n8n_workflow(payload)
```

The backend sends a webhook request to n8n.

If no risks → no automation is triggered.

---

## 4️⃣ Automation Layer (n8n)

When triggered:

- Receives structured JSON
- Logs compliance risk
- Can:
  - Send email
  - Store report
  - Generate audit log
  - Notify admin

This makes the system Agentic.

---

## 5️⃣ Structured Output Returned

Example output:

```json
{
  "income": 2000000,
  "old_regime_tax": 585000,
  "new_regime_tax": 400000,
  "recommended_regime": "New",
  "risks": [],
  "explanation": "New regime results in lower tax liability..."
}
```

Frontend displays:

- Tax comparison
- Recommended regime
- Risk warnings (if any)
- Explanation

---

# 📁 Project Structure

```
AI_TAX_NAVIGATION/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── tax_calculator.py
│   ├── risk_engine.py
│   ├── rag_engine.py
│   ├── automation.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

# 📌 File Responsibilities

## frontend/app.py

- Streamlit UI
- Collects inputs
- Sends request to backend
- Displays JSON output and warnings

---

## backend/main.py

- FastAPI server
- Defines `/analyze` endpoint
- Calls agent logic
- Returns structured response

---

## backend/agent.py

- Central orchestration file
- Calls:
  - Tax calculator
  - Risk engine
  - RAG engine
  - n8n automation (if required)
- Returns final structured output

---

## backend/tax_calculator.py

- Contains slab-based tax calculation logic
- Deterministic
- No AI used

---

## backend/risk_engine.py

- Rule-based compliance checks
- Prevents misuse of deductions
- Adds guardrails

---

## backend/rag_engine.py

- Loads government tax documents
- Builds embeddings
- Retrieves relevant content
- Grounds LLM explanations

---

## backend/automation.py

- Sends POST request to n8n webhook
- Triggered only if risks are detected

---

## backend/config.py

- Loads GROQ API key from environment variables
- Stores model configuration

---

# 🏗 Architecture Overview

```
User (Streamlit UI)
        ↓
FastAPI Endpoint
        ↓
Agent Orchestrator
        ↓
Tax Logic + Risk Engine + RAG
        ↓
LLM Explanation
        ↓
Conditional n8n Trigger
        ↓
Structured JSON Response
```

---

# 🔐 Security Features

- API keys stored in environment variables
- No secrets committed to GitHub
- RAG prevents hallucination
- Rule-based guardrails enforce compliance

---

# 🚀 Key Highlights

✔ Retrieval-Augmented Generation (RAG)  
✔ Agentic AI behavior  
✔ Guardrails for compliance  
✔ Structured JSON output  
✔ Frontend/Backend separation  
✔ Automation using n8n  
✔ Production-style architecture

---

# 🧩 Summary

The AI Current Tax Regime Navigator is a compliance-aware tax assistant that:

- Calculates taxes deterministically
- Uses AI only for explanation
- Detects rule violations
- Triggers automated workflows
- Grounds answers in official documents
- Maintains secure architecture

---
