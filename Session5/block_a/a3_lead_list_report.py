# print total count, then numbered names
names = ["ahmed", "sara", "Omer", "Lina"]

print(f"Total leads: {len(names)}")
for i, lead in enumerate(names, start = 1):
    print(f"{i}. {lead}")