"""Lead validation helpers."""


def is_valid_email(email):
    """Return True if email looks valid (contains @ and .)."""
    if "@" in email and "." in email:
        return True
    return False


def validate_lead(lead):
    """Validate lead dict; raise ValueError if invalid."""
    # TODO: check name and email using is_valid_email

    if not lead["name"]:
        raise ValueError("Name is required")

    if not is_valid_email(lead["email"]):
        raise ValueError("Invalid email")

