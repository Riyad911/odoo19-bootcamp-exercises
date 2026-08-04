"""TaggedLead — homework 4 starter."""
# TODO: subclass Lead, add tags support

from .lead import Lead

class TaggedLead(Lead):
    def __init__(self, name, email, stage="new", revenue=0.0, tags=None):
        super().__init__(name, email, stage, revenue)
        self.tags = tags if tags is not None else []

    def add_tag(self, tag):
        self.tags.append(tag)
