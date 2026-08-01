"""
In-class Task D (guided) — Override vs Overload

Fill the blanks / complete the code.
Remember:
  Override = child replaces parent method (same name)
  Overload = same method name, different parameters
             (Python: use defaults / optional args — no true overload)
"""


class Contact:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}"


class Partner(Contact):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    # TODO: OVERRIDE greet() so it includes company
    # Example result: "Hi, I am Omar from Acme"
    def greet(self):
        return f"Hi, I am {self.name} from {self.company}"


class LeadBox:
    def __init__(self):
        self.items = []

    # TODO: OVERLOAD-style — one method, optional email
    # add("Deal") and add("Deal", "a@co.com") should both work
    def add(self, name, email=None):
        pass  # store a dict like {"name": name, "email": email}


if __name__ == "__main__":
    p = Partner("Omar", "Acme")
    print(p.greet())  # should mention company (override)

    box = LeadBox()
    box.add("Website")
    box.add("ERP", "buyer@co.com")
    print(box.items)
