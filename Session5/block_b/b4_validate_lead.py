# B4 — Validate + raise
# is_valid_email: True if email contains "@" and "."
# validate_lead: raise ValueError if name empty or email invalid
# Loop leads with try/except — print valid, show error for invalid.

def is_valid_email(email):
    return ("@" in email) and ("." in email)


def validate_lead(lead):
    # TODO: raise ValueError with a clear message when invalid
    if not lead.get("name"):
        raise ValueError("Lead must have a name")
    if not is_valid_email(lead.get("email", "")):
        raise ValueError(f"invalid email : {lead.get('email', '')}")


leads = [
    {"name": "Ahmed", "email": "ahmed@acme.com"},
    {"name": "", "email": "bad@acme.com"},
    {"name": "Sara", "email": "not-an-email"},
    {"name": "Omar", "email": "omar@x.com"},
]

# TODO: loop + try/except

for lead in leads:
    try:
        validate_lead(lead)
        print(f"OK: {lead['name']}")
    except ValueError as e:
        print(f"ERROR: {e}")