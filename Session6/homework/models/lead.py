"""Lead model — homework 4 starter."""

# TODO: implement Lead class with mark_won, mark_lost, display_name property
class Lead:
    def __init__(self, name, email, stage = "new", revenue = 0.0):
        self.name = name
        self.email = email
        self.stage = stage
        self.revenue = revenue


    def mark_won(self):
        self.stage = "won"

    def mark_lost(self):
        self.stage = "lost"


    @property
    def display_name(self):
        return f"Name: {self.name}"




