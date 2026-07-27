# A6* — Unique tags
# Print one list of unique tags across all leads.

leads = [
    {"name": "A", "tags": ["hot", "egypt"]},
    {"name": "B", "tags": ["hot", "ksa"]},
    {"name": "C", "tags": ["egypt", "vip"]},
]

tags = []

for lead in leads:
    for tag in lead["tags"]:
        if tag not in tags:
            tags.append(tag)
print(tags)