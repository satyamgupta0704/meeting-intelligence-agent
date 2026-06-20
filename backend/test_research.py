from services.research_service import (
    gather_company_research
)

from services.brief_generator import (
    generate_brief
)

company = "Linear"

research = gather_company_research(
    company
)

brief = generate_brief(
    company,
    research
)

print(brief)