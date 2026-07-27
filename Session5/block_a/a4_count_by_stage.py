# A4 — Count by stage
# Build a dict like {"new": 2, "won": 2, "lost": 1} and print it.

leads = [
    {"name": "Ahmed", "stage": "new"},
    {"name": "Sara", "stage": "won"},
    {"name": "Omar", "stage": "new"},
    {"name": "Lina", "stage": "lost"},
    {"name": "Nour", "stage": "won"},
]

stage_count = {}

for lead in leads:
    stage = lead.get("stage", "N/A")
    stage_count[stage] = stage_count.get(stage, 0) + 1

print(stage_count)