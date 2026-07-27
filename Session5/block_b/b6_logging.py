# B6* — Logging
# Validate leads. Log invalid ones with logging.warning. Continue.
from typing import Protocol

import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)


def is_valid_email(email):
    return ("@" in email) and ("." in email)


def validate_lead(lead):
    if not lead.get("name"):
        raise ValueError("name is required")
    if not is_valid_email(lead.get("email", "")):
        raise ValueError(f"invalid email: {lead.get('email')}")


leads = [
    {"name": "Ahmed", "email": "ahmed@acme.com"},
    {"name": "", "email": "x@y.com"},
    {"name": "Sara", "email": "bad-email"},
    {"name": "Omar", "email": "omar@x.com"},
]

valid = []

# TODO: loop, try/except, _logger.warning on errors, append valid leads
for lead in leads:
    try:
        validate_lead(lead)
        valid.append(lead)
    except ValueError as e:
        _logger.warning("%s", e)

print(valid)