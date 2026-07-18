
"""
In-class Task D (independent) — Remove duplicates

Part 1: Remove duplicate tags from a list (keep first occurrence order)
Part 2: Remove duplicate leads by email from a list of dicts
"""

if __name__ == "__main__":
    # Part 1 — unique tags
    tags = ["hot", "vip", "hot", "new", "vip", "enterprise"]
    unique_tags = []

    # TODO: Build unique_tags without duplicates, preserving first-seen order

    print("Unique tags:", unique_tags)

    # Part 2 — unique leads by email
    leads = [
        {"name": "Website", "email": "a@co.com"},
        {"name": "Website Copy", "email": "a@co.com"},
        {"name": "CRM", "email": "b@co.com"},
        {"name": "Support", "email": "c@co.com"},
        {"name": "CRM Duplicate", "email": "b@co.com"},
    ]
    unique_leads = []
    seen_emails = []

    # TODO: Keep only first lead for each email

    print("\nUnique leads:")
    for lead in unique_leads:
        print(f"  - {lead['name']} <{lead['email']}>")