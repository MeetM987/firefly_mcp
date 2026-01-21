from firefly_client.mcp_client import send_meeting_data

fireflies_meeting_data = {
    "source": "fireflies",
    "meeting_id": "ff-001",
    "meeting_title": "Sprint Planning",
    "summary": "Discussed sprint backlog and priorities",
    "action_items": ["Fix login bug", "Prepare client demo"],
    "participants": ["Manager", "Dev1", "Dev2"],
    "ended_at": "2025-12-18T11:30:00Z"
}

response = send_meeting_data(fireflies_meeting_data)
print("Response from MCP server:", response)