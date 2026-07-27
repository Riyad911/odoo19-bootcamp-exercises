# B1 — First function
# Write format_lead(name, company) that returns an f-string.
# Call it twice and print the results.

def format_lead(name, company):
# TODO: return something like "Ahmed @ Acme"
    lead = f"Name: {name} @ Company: {company}"
    return lead

print(format_lead("riyad", "ensyab"))
print(format_lead("sary", "microsoft"))
