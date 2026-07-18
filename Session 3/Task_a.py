
"""
In-class Task A (guided) — Classify lead scores (3 levels)

For each score print:
- "high"   if score >= 80
- "medium" if score >= 50
- "low"    otherwise
"""

if __name__ == "__main__":
    scores = [20, 75, 45, 90, 50, 81]

    for score in scores:
        if score >= 80:
            label = "high"
        elif score >= 50:
            label = "medium"
        else:
            label = "low"
        print(f"{score} --> {label}")