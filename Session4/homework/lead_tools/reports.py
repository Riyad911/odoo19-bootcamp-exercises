"""Lead reporting helpers."""

def build_stage_report(leads):
    """Return dict mapping stage -> count."""
    # TODO: build_stage_report(leads)` — returns `dict` like `{"new": 2, "won": 1}`
    report = {}
    for lead in leads:
        stage = lead.get("stage", "Unknown")
        report[stage] = report.get(stage, 0) + 1
    return report

def total_revenue(leads):
    """Return sum of revenue across leads."""
    # TODO: total_revenue(leads)` — returns sum of revenue
    total = 0
    for lead in leads:
        amount = lead.get("revenue", 0)
        total += amount

    return total