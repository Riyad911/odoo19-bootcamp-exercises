# A5 — Remove duplicate emails
# Keep the FIRST lead for each email.
# Print count before and after.

leads = [
    {"name": "Ahmed", "email": "a@x.com"},
    {"name": "Sara", "email": "s@x.com"},
    {"name": "Ahmed Copy", "email": "a@x.com"},
    {"name": "Omar", "email": "o@x.com"},
    {"name": "Sara Copy", "email": "s@x.com"},
]

seen_email = []

for lead in leads:
    email = lead["email"]
    if email not in seen_email:
        seen_email.append(email)

print(f"Count leads before delete the duplicate: {len(leads)}")
print(f"Count leads after delete the duplicate: {len(seen_email)}")
print(seen_email)