# C2 — Warehouse Inventory Report (Session 2 skills)
# NEW task (not the old homework).
#
# Skills: for loops, if/elif/else, lists, dicts, remove duplicates, counting dict.
#
# Each product is a dict: name, sku, category, qty, price
# NOTE: there are duplicate SKUs on purpose.
#
# Do all of this:
# 1) Remove duplicate products by SKU (keep the FIRST one). Print count before/after.
# 2) Total stock value = sum(qty * price) for unique products.
# 3) Count products per category (dict).
# 4) Low stock: print names where qty < 5.
# 5) Unique categories list (no duplicates).
from unicodedata import category

products = [
    {"name": "USB Cable", "sku": "A1", "category": "cables", "qty": 30, "price": 20.0},
    {"name": "HDMI Cable", "sku": "A2", "category": "cables", "qty": 3, "price": 55.0},
    {"name": "USB Cable v2", "sku": "A1", "category": "cables", "qty": 99, "price": 21.0},
    {"name": "Mouse", "sku": "B1", "category": "accessories", "qty": 12, "price": 150.0},
    {"name": "Keyboard", "sku": "B2", "category": "accessories", "qty": 2, "price": 300.0},
    {"name": "Monitor", "sku": "C1", "category": "screens", "qty": 4, "price": 2500.0},
    {"name": "Mouse Clone", "sku": "B1", "category": "accessories", "qty": 50, "price": 100.0},
]

#---------------------------
# 1) Remove duplicate SKUs
#---------------------------
unique_product = list()
seen_sku = list()
for pro in products:
    if pro["sku"] not in seen_sku:
        seen_sku.append(pro["sku"])
        unique_product.append(pro)

print(f"The products before and after remove the duplicates: \n"
      f"before: {len(products)}\n"
      f"after: {len(unique_product)}")

#---------------------------
# 2) Total Stock Value
#---------------------------
total_stock = 0
for pro in unique_product:
    total_stock += pro["qty"] * pro["price"]
print(f"The Total stock value is: ${total_stock:,.2f}")
#---------------------------
# 3) Count products by category
#---------------------------
count_products = dict()
for pro in unique_product:
    category = pro.get("category", "Unknown")
    count_products[category] = count_products.get(category, 0) + 1
print(count_products)

#---------------------------
# 4) Print low stock
#---------------------------
for pro in unique_product:
    if pro["qty"] < 5:
        print(f"{pro["name"]} --> {pro["qty"]}")

#---------------------------
# 5) Unique categories
#---------------------------
unique_categories = list(count_products.keys())
print(f"Unique categories: {unique_categories}")