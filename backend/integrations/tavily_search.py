from tavily import TavilyClient
import os

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_company(company):

    return client.search(
        query=f"{company} company overview",
        search_depth="advanced",
        max_results=5
    )


def search_news(company):

    return client.search(
        query=f"{company} latest news funding announcements",
        search_depth="advanced",
        max_results=5
    )


def search_tech(company):

    return client.search(
        query=f"{company} tech stack engineering jobs github",
        search_depth="advanced",
        max_results=5
    )