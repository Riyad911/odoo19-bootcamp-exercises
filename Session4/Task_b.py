"""
In-class Task B (guided) — safe_divide

Return None when dividing by zero and log a warning.
"""

import logging

_logger = logging.getLogger(__name__)


def safe_divide(a, b):
    """Return a / b, or None if b is zero."""
    if b == 0:
         _logger.warning("You can't divide by zero")
    return a / b

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide(100, 4))