import requests

MCP_SERVER_URL = "http://127.0.0.1:3333"

def send_meeting_data(meeting_data: dict):
    payload = {
        "tool": "store_meeting_data",
        "arguments": meeting_data
    }
    r = requests.post(f"{MCP_SERVER_URL}/call_tool", json=payload, timeout=30)
    r.raise_for_status()
    return r.json()