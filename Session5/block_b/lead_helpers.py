# B5* — helper module
# Put reusable functions here. Import them from run_b5.py.


def format_lead(name, company):
    return f"{name} @ {company}"


def is_valid_email(email):
    return ("@" in email) and ("." in email)


def classify_score(score, threshold=70):
    if score >= threshold:
        return "high"
    return "low"
