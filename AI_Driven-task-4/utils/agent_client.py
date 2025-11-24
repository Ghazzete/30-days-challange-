# utils/agent_client.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
MCP_API_KEY = os.getenv("MCP_API_KEY")  # optional, agar server require kare

def call_agent_via_mcp(prompt, instructions=None):
    """
    Send user PDF text to MCP server via JSON-RPC 2.0 format
    """
    if MCP_SERVER_URL is None:
        return {"error": "MCP_SERVER_URL not set in environment variables."}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    if MCP_API_KEY:
        headers["Authorization"] = f"Bearer {MCP_API_KEY}"

    # JSON-RPC 2.0 payload
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "study_notes_agent.run",  # <- exact agent name + .run
        "params": {
            "instructions": instructions or "Summarize and generate quiz",
            "input": prompt
        }
    }

    try:
        response = requests.post(MCP_SERVER_URL, json=payload, headers=headers, timeout=60)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
