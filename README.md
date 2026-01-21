# Firefly MCP Server (Local) – FINAL (No MCP SDK Conflicts)

This version avoids MCP Python SDK conflicts by implementing a local tool server using **FastAPI**
and calling it using **requests**.

## Setup
```powershell
py -3.11 -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
**Terminal 1 (Server):**
```powershell
uvicorn mcp_server.server:app --port 3333 --reload
```

**Terminal 2 (Client Simulator):**
```powershell
python -m firefly_client.fireflies_simulator
```

## Expected Output
Server prints meeting payload, client prints JSON response.