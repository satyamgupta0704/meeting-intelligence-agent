from integrations.tavily_search import (
    search_company,
    search_news,
    search_tech
)

company = "Linear"

print("\nCOMPANY\n")
print(search_company(company))

print("\nNEWS\n")
print(search_news(company))

print("\nTECH\n")
print(search_tech(company))