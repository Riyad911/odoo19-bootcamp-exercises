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
    # We use loop method when order matters
    for tag in tags:
        if tag not in unique_tags:
            unique_tags.append(tag)
    print("Unique tags:", unique_tags)

    # Another solution
    # We use set method when no matter of order, It's faster than loop
    unique_tags_with_set = list(set(tags))
    print("Unique tags with set:", unique_tags_with_set)

    # TODO: Keep only first lead for each email

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

    for lead in leads:
        email = lead['email']
        if email not in seen_emails:
            seen_emails.append(email)
            unique_leads.append(lead)

    print(f"\nBefore: {len(leads)} leads")
    print(f"After:  {len(unique_leads)} unique emails")

    print("\nUnique leads:")
    for lead in unique_leads:
        print(
            f" - {lead['name']} <{lead['email']}>"
        )
