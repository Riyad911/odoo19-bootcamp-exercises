# B2 — Classify + default parameter
# Return "high" if score >= threshold, else "low".
# Default threshold = 70.

def classify_score(score, threshold=70):
    if score >= threshold:
        return "High"
    else:
        return "Low"

# TODO: test with and without threshold

print(classify_score(50, 70))
print(classify_score(50))
print(classify_score(80))