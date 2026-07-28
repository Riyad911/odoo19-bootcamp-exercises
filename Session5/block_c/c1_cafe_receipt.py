# C1 — Cafe Order Receipt (Session 1 skills)
# NEW task (not the old homework).
#
# Skills: input, int/float conversion, f-strings, comments.
#
# Ask the user for:
#   - customer name
#   - drink name
#   - unit price (float, e.g. 45.5)
#   - quantity (int)
# Then print a small receipt with f-strings:
#   Customer, drink x quantity, and TOTAL = price * quantity
#
# Bonus: if total > 100, print a "10% loyalty discount" line with the new total.


customer_name = input("Please enter your name: ")
drink = input("Please enter your drink: ")
unit_price = int(input("unit Price: "))
qty = int(input("qty: "))

total = unit_price * qty

print(f"--- Receipt for Customer {customer_name} ---")
print(f"{drink} x {qty}")
print(f"TOTAL: {total}")

if total > 100:
    # total_after_discount = total - (total * 0.10)
    total_after_discount = total * 0.9
    print(f"Total after discount 10% --> {total_after_discount}")