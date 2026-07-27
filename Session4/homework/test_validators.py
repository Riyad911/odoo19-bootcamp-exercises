from lead_tools import (
    is_valid_email,
    validate_lead,
    total_revenue,
    build_stage_report,
)
import pytest


# Test the is_valid_email() function.
# This function returns True if the email is valid,
# and False if the email is invalid.
# Therefore, we can test it using assert statements.
def test_valid_email():
    # Valid email should return True
    assert is_valid_email("riyad@gmail.com")

    # Invalid emails should return False
    assert not is_valid_email("riyadgmail.com")
    assert not is_valid_email("riyad@gmailcom")


# Test the validate_lead() function.
# This function does not return True or False.
# Instead, it raises ValueError when the lead is invalid.
# Therefore, we use pytest.raises() to check that
# the expected exception is raised.
def test_invalid_lead():
    lead = {
        "name": "",
        "email": "riyad@gmail.com"
    }

    # We expect ValueError because the name is empty
    with pytest.raises(ValueError):
        validate_lead(lead)


# Test the total_revenue() function.
# This function calculates the sum of all revenues
# and returns a number.
# We use assert to compare the returned value
# with the expected result.
def test_total_revenue():
    leads = [
        {"name": "Website", "revenue": 5000},
        {"name": "CRM", "revenue": 3000},
    ]

    # Expected total revenue = 5000 + 3000 = 8000
    assert total_revenue(leads) == 8000


# Test the build_stage_report() function.
# This function groups leads by their stage
# and counts how many leads exist in each stage.
# It returns a dictionary containing stage names as keys
# and the number of leads as values.
def test_build_stage_report():
    leads = [
        {"stage": "new"},
        {"stage": "new"},
        {"stage": "won"},
    ]

    report = build_stage_report(leads)

    # Check that the "new" stage contains 2 leads
    assert report["new"] == 2

    # Check that the "won" stage contains 1 lead
    assert report["won"] == 1