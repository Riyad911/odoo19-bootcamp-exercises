"""
In-class Task B (guided) — TaggedLead subclass

Learn / use:
  Inheritance = TaggedLead(Lead) reuses Lead
  Override    = redefine summary() in the child (same name, new body)
  Polymorphism = Lead.summary and TaggedLead.summary behave differently

TODO:
  1. TaggedLead.__init__ with tags list (+ super().__init__)
  2. add_tag(tag)
  3. OVERRIDE summary() to include tags
"""


class Lead:
    def __init__(self, name, email, stage="new"):
        self.name = name
        self.email = email
        self.stage = stage

    def summary(self):
        return f"{self.name} <{self.email}> [{self.stage}]"


class TaggedLead(Lead):
    # TODO: __init__(self, name, email, tags=None, **kwargs)
    #       call super().__init__(...) then set self.tags

    def __init__(self, name, email, tags = None, **kwargs):
        super().__init__(name, email, **kwargs)
        self.tags = tags if tags is not None else []

    # TODO: add_tag(self, tag)

    def add_tag(self, tag):
        self.tags.append(tag)
    # TODO: override summary(self) → include tags in the string

    def summary(self):

        tags_summary = f" Tag: { ', '.join(self.tags)}" if self.tags else ""
        return tags_summary


if __name__ == "__main__":
    lead = TaggedLead("Deal", "a@co.com", tags=["hot"])
    lead.add_tag("vip")
    print(lead.name, lead.tags)
    print(lead.summary())  # should show tags (override)
