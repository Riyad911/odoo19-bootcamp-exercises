# F1 — BOOKSHOP CHALLENGE (mix of Session 1 + 2 + 3) — NEW scenario
#
# This is a brand new task. It uses the SAME skills as the 3 homeworks,
# but a different domain (a bookshop), so it is fresh practice.
#
# ===========================================================
# PART 1 — Session 1 skills (in main.py)
# ===========================================================
# - Ask the shop clerk for: their name, and today's branch city
# - Print a welcome banner with f-strings + at least 2 comments
# - Bonus: ask how many hours the shop is open (text -> int) and
#   print closing message using try/except for bad input
#
# ===========================================================
# PART 2 — Session 2 skills (books data + reports)
# ===========================================================
# - 7+ books, with duplicate ISBNs on purpose
# - Remove duplicate ISBNs (keep first); print count before/after
# - total stock value, count per genre, average price per genre
# - out-of-stock titles, unique authors
#
# ===========================================================
# PART 3 — Session 3 skills (shop_tools package)
# ===========================================================
# - Fill shop_tools/validators.py and shop_tools/reports.py
# - validate_book raises ValueError for bad data
# - Use try/except + logging so bad books are skipped, not crashing
# - No JSON
#
# Run from this folder:
#   python3 main.py

import logging

# TODO: import validate_book from shop_tools.validators
# TODO: import the report functions you need from shop_tools.reports

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

# --- PART 1: clerk intro ---
# TODO: ask clerk name + branch city, print welcome banner (f-strings)

# --- PART 2 data (with duplicate ISBNs and 1-2 invalid books) ---
raw_books = [
    {"title": "Python 101", "author": "Ada", "isbn": "PY101", "genre": "tech", "stock": 5, "price": 120.0},
    {"title": "Kids ABC", "author": "Sam", "isbn": "KID01", "genre": "kids", "stock": 0, "price": 30.0},
    {"title": "Python 101 (copy)", "author": "Ada", "isbn": "PY101", "genre": "tech", "stock": 9, "price": 125.0},
    {"title": "Cooking Fast", "author": "Lina", "isbn": "COOK1", "genre": "food", "stock": 3, "price": 80.0},
    {"title": "", "author": "Ghost", "isbn": "BAD01", "genre": "misc", "stock": 1, "price": 10.0},  # invalid title
    {"title": "Cheap Deal", "author": "Omar", "isbn": "X", "genre": "misc", "stock": 2, "price": -5.0},  # invalid isbn + price
    {"title": "Kids 123", "author": "Sam", "isbn": "KID02", "genre": "kids", "stock": 7, "price": 35.0},
    {"title": "Data Science", "author": "Ada", "isbn": "DS200", "genre": "tech", "stock": 0, "price": 200.0},
]

# TODO PART 2 + 3:
# 1) print before count
# 2) remove_duplicate_isbn
# 3) validate each unique book (try/except + _logger.warning) -> valid list
# 4) print all the reports on VALID books
