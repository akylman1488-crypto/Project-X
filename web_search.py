from duckduckgo_search import DDGS
from logger import sys_logger

class SearchTool:
    def __init__(self):
        self.ddgs = DDGS()

    def execute(self, query, max_results=5):
        sys_logger.think("SEARCH", f"Searching for: {query}")
        try:
            results = list(self.ddgs.text(query, max_results=max_results))
            if not results:
                return "No results found."
            
            summary = ""
            for res in results:
                summary += f"Title: {res['title']}\nLink: {res['href']}\nBody: {res['body']}\n\n"
            return summary
        except Exception as e:
            sys_logger.error(f"Search failed: {e}")
            return "Search unavailable."
