"""
In-class Task A (guided) — format_lead_summary

Write a function that returns a one-line summary for a lead dict.
Use: name, stage, revenue
"""


def format_lead_summary(lead_dict):
    """Return a formatted summary string for a lead dict."""
    name = lead_dict.get("name", "Unknown")
    stage = lead_dict["stage"]
    revenue = lead_dict["revenue"]
    return f"The name of lead is: {name}, in stage: {stage}, and revenue is: {revenue}"

if __name__ == "__main__":
    leads = [
        {"name": "Deal A", "stage": "new", "revenue": 1000},
        {"name": "Deal B", "stage": "won", "revenue": 5000},
        {"name": "Deal C", "stage": "lost", "revenue": 0},
    ]
    for lead in leads:
        print(format_lead_summary(lead))

