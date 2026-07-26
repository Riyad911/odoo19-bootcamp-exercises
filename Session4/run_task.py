"""Driver for Task C — import and run pipeline_stats."""
from pipeline_stats import average_revenue, count_by_stage, total_revenue


if __name__ == "__main__":
    leads = [
        {"name": "A", "stage": "new", "revenue": 1000},
        {"name": "B", "stage": "won", "revenue": 5000},
        {"name": "C", "stage": "new", "revenue": 2000},
        {"name": "D", "stage": "won", "revenue": 8000},
    ]

    print("Count by stage:", count_by_stage(leads))
    print("Total revenue:", total_revenue(leads))
    print("Average revenue:", average_revenue(leads))