"""
In-class Task B (guided) — Filter active leads with minimum revenue

Print name, email, and revenue for leads where:
- active is True
- revenue >= 2000
"""

if __name__ == "__main__":
    leads = [
        {"name": "Deal A", "email": "a@co.com", "revenue": 5000, "active": True},
        {"name": "Deal B", "email": "b@co.com", "revenue": 800, "active": True},
        {"name": "Deal C", "email": "c@co.com", "revenue": 3000, "active": False},
        {"name": "Deal D", "email": "d@co.com", "revenue": 2500, "active": True},
        {"name": "Deal E", "email": "e@co.com", "revenue": 1200, "active": True},
    ]

    min_revenue = 2000

    print(f" Active Leads with revenue >= {min_revenue:,.2f} :")
    for lead in leads:
        if lead["active"] and lead["revenue"] >= min_revenue:
            print(f" - {lead['name']} : {lead['email']} : {lead['revenue']:,.2f}")