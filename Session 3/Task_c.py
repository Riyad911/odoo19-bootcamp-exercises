"""
In-class Task C (independent) — Pipeline report with counts and revenue

Given stage events, build a report dict:
- key: stage name
- value: {"count": N, "total_revenue": X}

Sample revenue per event index (same order as events):
"""

if __name__ == "__main__":
    events = ["new", "new", "won", "lost", "new", "won", "won"]
    revenues = [1000, 1500, 8000, 0, 2000, 5000, 12000]

# TODO: Build report dict with count and total_revenue per stage
    report = {}
    for stage, revenue in zip(events, revenues):
        if stage not in report:
            report[stage] = {'count' : 0, 'total_revenue' : 0}
        report[stage]['count'] += 1
        report[stage]['total_revenue'] += revenue

# TODO: Print summary lines like: new: count=3, revenue=4500
    print("Pipeline summary:")
    for stage, data in report.items():
       print(
           f" {stage} : count={data['count']}, revenue={data['total_revenue']:,.2f}"
       )
