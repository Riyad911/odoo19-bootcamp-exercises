"""
Homework 4 — main driver
See README.md for requirements.
"""

from models.lead import Lead
from models.tagged_lead import TaggedLead
from repository import LeadRepository

# TODO: wire Lead, TaggedLead, LeadRepository, PipelineService


if __name__ == "__main__":
    # Crate the leads.
    lead01 = TaggedLead("Riyad", "riyad@gmail.com", revenue = 5000, tags = ["red"])
    lead01.mark_lost()
    lead02 = TaggedLead("Mona", "Mona@gmail.com", revenue = 9500, tags = ["blue"])
    lead02.mark_won()
    lead03 = Lead("Rami", "Rami@gmail.com", revenue = 1200)
    lead03.mark_won()
    lead04 = TaggedLead("Ahmed", "Ahmed@gmail.com", "won",420, tags = ["yellow"])
    lead05 = Lead("Ibrahim", "Ibrahim@gmail.com", revenue = 6000)
    lead06 = TaggedLead("Sara", "Sara@gmail.com", revenue =9000)
    lead06.add_tag("green")
    lead07 = Lead("Malak", "Malak@gmail.com", "lost",4000)

    # Crate a repository and add the leads inside it.
    repo = LeadRepository()
    repo.add_lead(lead01)
    repo.add_lead(lead02)
    repo.add_lead(lead03)
    repo.add_lead(lead04)
    repo.add_lead(lead05)
    repo.add_lead(lead06)
    repo.add_lead(lead07)

    print(lead01.display_name)
    print(repo.total_revenue())








