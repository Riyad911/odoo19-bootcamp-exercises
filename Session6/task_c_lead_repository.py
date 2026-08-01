"""
In-class Task C (independent) — LeadRepository

Learn / use:
  Encapsulation = hide the list as self._records
  Abstraction   = callers use add / find_by_stage / total_revenue
                  without caring how storage works

TODO: add(lead), find_by_stage(stage), total_revenue()
"""
class Lead:
    def __init__(self, name, address, stage = "New", revenue = 0.0):
        self.name = name
        self.address = address
        self.stage = stage
        self.revenue = revenue

class LeadRepository:
    def __init__(self):
        self.__records = []  # private-ish storage (encapsulation)

    # TODO: add(self, lead) → append to self._records

    def add(self, lead):
        self.__records.append(lead)


    # TODO: find_by_stage(self, stage) → return matching leads

    def find_by_stage(self, stage):
        return [lead for lead in self.__records if lead.stage == stage]

    # TODO: total_revenue(self) → sum of lead.revenue
    def total_revenue(self):
        total = 0
        for lead in self.__records:
            total += lead.revenue
        return total

if __name__ == "__main__":
    from task_a_lead_class import Lead  # students may copy Lead class here instead

    repo = LeadRepository()
    repo.add(Lead("A", "a@co.com", revenue=1000))
    repo.add(Lead("B", "b@co.com", stage="won", revenue=5000))

    print("Won:", [l.name for l in repo.find_by_stage("won")])
    print("Total:", repo.total_revenue())


