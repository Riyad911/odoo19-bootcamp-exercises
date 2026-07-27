# B3 — Safe int
# Use try/except. Return int(text) or None if invalid.

def safe_int(text):
    try:
       # return int(text)
        return int(text) + text
    except ValueError:
        return None
    except TypeError:
        return False

print(safe_int("42"))   # expect 42
print(safe_int("abc"))  # expect None
print(safe_int("7.5"))  # expect None (int() fails on "7.5")
