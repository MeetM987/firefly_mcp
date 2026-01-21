from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Firefly MCP Server (Requests Client Compatible)")

class ToolCall(BaseModel):
    tool: str
    arguments: dict

@app.post("/call_tool")
def call_tool(payload: ToolCall):
    if payload.tool == "store_meeting_data":
        meeting = payload.arguments
        print("=== Meeting received from Fireflies ===")
        print(meeting)
        print("======================================")
        return {"result": "Meeting data received and processed locally"}

    return {"error": f"Unknown tool: {payload.tool}"}