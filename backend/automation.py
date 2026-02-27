import requests
from config import N8N_WEBHOOK_URL


def trigger_workflow(data):
    try:
        requests.post(N8N_WEBHOOK_URL, json=data)
    except:
        pass