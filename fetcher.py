from tavily import TavilyClient

TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

def fetch_articles(query="latest AI news"):
    results = client.search(
        query=query,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        max_results=5
    )
    return results.get("results", [])