import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SwarmTaskDecompositionAuctioneerClient

def main():
    client = SwarmTaskDecompositionAuctioneerClient()
    res = client.auction_and_allocate_tasks()
    print("=== Swarm Task Decomposition Auctioneer Output ===")
    print(f"Objective: {res['compound_objective']}")
    print(f"Decomposed: {res['subtasks_decomposed_count']} tasks across {res['agents_evaluated_count']} candidate agents")
    print(f"Status: {res['auction_status']} (Efficiency: {res['swarm_allocation_efficiency']*100}%)")
    print("\nTask Allocation Awards:")
    for a in res['allocated_subtask_roster']:
        print(f"  * [{a['subtask_id']}] {a['subtask_name']:35s} -> {a['awarded_agent_id']} (Bid Score: {a['bid_score']}, Rate: ${a['allocated_hourly_rate_usd']}/h)")

if __name__ == '__main__':
    main()
