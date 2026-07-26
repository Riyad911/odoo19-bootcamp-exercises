"""
In-class Task C (independent) — pipeline_stats module
Implement count_by_stage and total_revenue.
Then run with: python3 run_task_c.py
"""

def count_by_stage(leads):
    counts = {}
    for lead in leads:
        stage = lead.get("stage", "Unknown")
        counts[stage] = counts.get(stage, 0) + 1
    return counts

def total_revenue(leads):
    total = 0
    for amount in leads:
        total += amount.get("revenue", 0)
    return total

def average_revenue(leads):
    if not leads:
        return 0.0
    return total_revenue(leads) / len(leads)