# A7* — Search by name
# Ask for a search term.
# Print leads whose name contains the term (case-insensitive).

leads = [
    {"name": "Ahmed Hassan", "stage": "new"},
    {"name": "Sara Ali", "stage": "won"},
    {"name": "Omar Hassan", "stage": "lost"},
    {"name": "Lina Ahmed", "stage": "new"},
]

term = input("please enter the term you want to search: ").lower()
flag = False
for lead in leads:
    if term in lead["name"].lower() or term in lead["stage"]:
        print(f"found it :{lead}")
        flag = True
        break
if not flag:
    print("Not fount")

