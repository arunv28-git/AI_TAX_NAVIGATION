from groq import Groq
from config import MODEL_NAME
from rag_engine import build_retriever
from tax_calculator import calculate_old_regime, calculate_new_regime
from risk_engine import detect_compliance_risk
from automation import trigger_workflow


def load_api_key():
    with open("api_key.txt", "r") as f:
        return f.read().strip()


class TaxAgent:

    def __init__(self):
        self.client = Groq(api_key=load_api_key())
        self.retriever = build_retriever()

    def analyze(self, user_input):

        income = user_input["income"]
        deductions = user_input["deductions"]

        old_tax = calculate_old_regime(income, deductions)
        new_tax = calculate_new_regime(income)

        if old_tax < new_tax:
            recommended = "Old"
        elif new_tax < old_tax:
            recommended = "New"
        else:
            recommended = "Either (Both Same Tax)"

        risks = detect_compliance_risk(user_input, recommended)

        # RAG retrieval
        query = "Tax regime rules and deduction eligibility"
        retrieved_docs = self.retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in retrieved_docs])

        explanation_prompt = f"""
User Income: {income}
Deductions: {deductions}

Old Regime Tax: {old_tax}
New Regime Tax: {new_tax}

Official Rules:
{context}

Explain clearly why {recommended} regime is better.
Keep explanation short.
"""

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": explanation_prompt}],
            temperature=0.2
        )

        explanation = response.choices[0].message.content.strip()

        result = {
            "income": income,
            "old_regime_tax": old_tax,
            "new_regime_tax": new_tax,
            "recommended_regime": recommended,
            "risks": risks,
            "explanation": explanation
        }

        if risks:
            trigger_workflow(result)

        return result


def build_agent():
    return TaxAgent()