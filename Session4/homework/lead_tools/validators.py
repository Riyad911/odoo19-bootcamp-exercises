"""Lead validation helpers."""


def is_valid_email(email):
    """Return True if email looks valid (contains @ and .)."""
    if not email or not isinstance(email, str):
        return False
    return "@" in email and "." in email.split("@")[-1]



def validate_lead(lead):
    """Validate lead dict; raise ValueError if invalid."""
    # TODO: check name and email using is_valid_email
    if not lead["name"]:
        raise ValueError("Name is required")

    if not is_valid_email(lead["email"]):
        raise ValueError("Invalid email")

    return True