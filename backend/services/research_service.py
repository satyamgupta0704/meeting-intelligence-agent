from integrations.tavily_search import (
    search_company,
    search_news,
    search_tech
)

def gather_company_research(company):

    print(f"Researching {company}")

    company_info = search_company(company)

    news = search_news(company)

    tech = search_tech(company)

    return {
        "company_info": company_info,
        "news": news,
        "tech": tech
    }