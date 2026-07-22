"""
Homework 2 — Mini CRM in memory
See README.md for requirements.
Includes duplicate removal and average revenue per stage.
"""

if __name__ == "__main__":
    # TODO: Define at least 7 leads (include duplicate emails on purpose)
    raw_leads = [
        {"name": "Riyad", "email": "riyad@gmail.com", "stage": "new", "revenue": 5000, "tags": "tag_1"},
        {"name": "Ahmed", "email": "ahmed@gmail.com", "stage": "won", "revenue": 6000, "tags": "tag_2"},
        {"name": "Mohammed", "email": "mohammed@gmail.com", "stage": "lost", "revenue": 0, "tags": "tag_3"},
        {"name": "Sari", "email": "riyad@gmail.com", "stage": "new", "revenue": 5500, "tags": "tag_1"},
        {"name": "Ali", "email": "ali@gmail.com", "stage": "won", "revenue": 10000, "tags": "tag_2"},
        {"name": "Rami", "email": "rami@gmail.com", "stage": "lost", "revenue": 2000, "tags": "tag_3"},
        {"name": "Khaled", "email": "khaled@gmail.com", "stage": "won", "revenue": 1500, "tags": "tag_1"}
    ]

    # TODO: Deduplicate by email (keep first occurrence)
    leads = []
    seen_email = []
    for lead in raw_leads:
        email = lead['email']
        if email not in seen_email:
            seen_email.append(email)
            leads.append(lead)

    # TODO: Print before/after counts
    print(f"Number of leads before delete: {len(raw_leads)}"
          f"\nNumber of leads after delete: {len(leads)}")

    # TODO: Total revenue, count per stage, average revenue per stage
    total = 0
    for amount in leads:
        total += amount["revenue"]
    print(f"Total revenue is: {total:,.2f}")

    counts = {}

    for lead in leads:
        stage = lead["stage"]
        counts[stage] = counts.get(stage, 0)+1
    print(counts)


    report = {}
    for lead in leads:
        stage = lead["stage"]
        if stage not in report:
            report[stage] = {
                "count": 0,
                "total_revenue": 0
            }
        report[stage]["count"] += 1
        report[stage]["total_revenue"] += lead["revenue"]
    for stage, data in report.items():
        average = data["total_revenue"] / data["count"]
        print(f"{stage}: average revenue = {average:,.2f}")

    # TODO: Won emails list
    won_emails = []
    for lead in leads:
        if lead["email"] not in won_emails:
            won_emails.append(lead["email"])
    print(f"The only won email of leads is: {won_emails}")

    # TODO: Unique tags across all leads
    unique_tags = []
    for lead in leads:
        unique_tag = lead["tags"]
        if unique_tag not in unique_tags:
            unique_tags.append(unique_tag)
    print(f"The Unique tags of leads is: {unique_tags}")

    # BONUS: search by name (case-insensitive)
    pass