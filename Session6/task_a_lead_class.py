"""
In-class Task A (guided) — Lead class

Learn / use:
  class     = blueprint for objects
  __init__  = constructor (runs when you create a Lead)
  self      = this specific lead
  Encapsulation = data + methods together on Lead

TODO: implement mark_won() and mark_lost() methods.
"""


class Lead:
    def __init__(self, name, email, stage="new", revenue=0.0):
        # Constructor: store attributes on this object
        self.name = name
        self.email = email
        self.stage = stage
        self.revenue = revenue

    def mark_won(self):
        self.stage = "won"

    def mark_lost(self):
        self.stage = "lost"

if __name__ == "__main__":
    lead = Lead("Test Deal", "test@co.com", revenue=1000)
    lead.mark_won()
    print(f"Stage: {lead.stage}")
