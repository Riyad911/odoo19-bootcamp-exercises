# Homework 3 — Lead Utilities Package (No JSON)

## Goal

Organize code into reusable functions and modules with validation, reporting, and error handling.

Use **hardcoded lead dicts** (same style as Session 2). Do **not** use JSON files.

## Structure

```
homework/
  lead_tools/
    __init__.py
    validators.py
    reports.py
  main.py
```

## Requirements

### `validators.py`
- `is_valid_email(email)` — returns `True` if email contains `@` and `.`
- `validate_lead(lead)` — raises `ValueError` with a clear message if name or email is invalid

### `reports.py`
- `build_stage_report(leads)` — returns `dict` like `{"new": 2, "won": 1}`
- `total_revenue(leads)` — returns sum of revenue

### `main.py`
- Define a list of at least **6 leads** as dicts (include 1–2 invalid ones on purpose)
- Validate each lead inside `try/except`
- Log errors with `logging` without crashing
- Print stage report and total revenue for **valid** leads only

## Bonus

Add `test_validators.py` with simple `assert` statements (or use pytest).

## Run

```bash
cd homework
python3 main.py
```

## Acceptance criteria

- [ ] Package imports work
- [ ] No JSON / file loading
- [ ] Invalid leads are logged, program continues
- [ ] Stage report + total revenue print correctly
- [ ] No duplicated logic across files