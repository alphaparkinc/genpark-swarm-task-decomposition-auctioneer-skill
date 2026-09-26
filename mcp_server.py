import json, sys
from client import SwarmTaskDecompositionAuctioneerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "swarm-task-decomposition-auctioneer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "auction_and_allocate_tasks", "description": "Decomposes compound objectives into subtasks and calculates optimal auction awards for worker agents."}]}}
    elif method == "tools/call":
        client = SwarmTaskDecompositionAuctioneerClient()
        res = client.auction_and_allocate_tasks()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = SwarmTaskDecompositionAuctioneerClient()
        print(json.dumps(client.auction_and_allocate_tasks(), indent=2))
