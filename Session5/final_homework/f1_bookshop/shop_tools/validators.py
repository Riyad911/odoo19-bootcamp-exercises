# F1 — validators (Session 3 skills) — Bookshop
#
# is_valid_isbn(isbn) -> True if isbn is a non-empty string with length >= 5
# validate_book(book) -> raise ValueError if:
#     - title is empty, OR
#     - isbn is invalid, OR
#     - price < 0


def is_valid_isbn(isbn):
    return isinstance(isbn, str) and isbn and len(isbn) >= 5

def validate_book(book):
    # TODO: raise ValueError with a clear message
    if not book["title"]:
        raise ValueError("Title is required.")
    elif not is_valid_isbn(book["isbn"]):
        raise ValueError("Invalid ISBN.")
    elif book["price"] < 0:
        raise ValueError("Price cannot be negative.")
    return True

