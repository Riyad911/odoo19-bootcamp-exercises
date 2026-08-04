"""LeadRepository — homework 4 starter."""

# TODO: implement add, find_by_stage, total_revenue
class LeadRepository:
    def __init__(self):
        self.__records = []


    def add_lead(self, lead):
        self.__records.append(lead)

    def find_by_stage(self, stage):
        leads = []
        for lead in self.__records:
            if lead.stage == stage:
                leads.append(lead)
        return leads

    def find_by_stage1(self, stage):
        # List Comprehensive
        return [lead for lead in self.__records if lead.stage == stage]

    def total_revenue(self):
        total = 0
        for lead in self.__records:
            total += lead.revenue
        return total