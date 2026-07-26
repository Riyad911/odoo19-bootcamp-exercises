"""
Homework 3 — main driver

Hardcoded leads (no JSON). Validate, log errors, print reports.
Run from homework/: python3 main.py
"""

import logging
# TODO: import from lead_tools
from lead_tools import *
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)



if __name__ == "__main__":
    # TODO: at least 6 leads — include 1–2 invalid (empty name or bad email)
    leads = [
        {"name": "Website", "email": "abc@co.com", "stage": "won", "revenue": 5000},
        {"name": "CRM", "email": "abd@co.com", "stage": "new", "revenue": 3000},
        {"name": "Purchase", "email": "abe@co.com", "stage": "won", "revenue": 9000},
        {"name": "Inventory", "email": "acocom", "stage": "new", "revenue": 2000},
        {"name": "", "email": "abf@co.com", "stage": "new", "revenue": 3500},
        {"name": "Website", "email": "abg@co.com", "stage": "lost", "revenue": 1000}
    ]

    valid_leads = []
    # TODO: validate each lead, append valid ones, log invalid ones
    for lead in leads:
        try:
            validate_lead(lead)
            valid_leads.append(lead)
        except ValueError as e:
            _logger.error(f"Invalid lead: {lead} {e}")

    # TODO: print build_stage_report(valid_leads)
    print(build_stage_report(valid_leads))

    # TODO: print total_revenue(valid_leads)
    print(f"The Total of revenues is: {total_revenue(valid_leads):,.2f}")
