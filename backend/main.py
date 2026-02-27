from fastapi import FastAPI
from agent import build_agent

app = FastAPI()
agent = build_agent()


@app.post("/analyze")
def analyze_tax(data: dict):
    return agent.analyze(data)