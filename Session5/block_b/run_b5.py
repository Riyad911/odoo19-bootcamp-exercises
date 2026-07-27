# B5* — Modules
# Import helpers from lead_helpers.py and demo them.

import lead_helpers as lead
from lead_helpers import format_lead, is_valid_email, classify_score
# TODO:
# from lead_helpers import format_lead, is_valid_email, classify_score
# print a few demo calls

print(format_lead("Ahmed", "Acme"))
print(is_valid_email("a@b.com"))
print(classify_score(80))
print(classify_score(40))
