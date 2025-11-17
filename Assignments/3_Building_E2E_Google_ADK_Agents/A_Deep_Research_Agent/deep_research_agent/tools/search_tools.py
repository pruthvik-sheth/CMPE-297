import os
from tavily import TavilyClient
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

# Initialize Tavily client
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str, max_results: int = 5) -> str:
    """Search the web using Tavily API"""
    try:
        response = tavily_client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results
        )
        
        results = []
        for result in response.get('results', []):
            results.append(f"Title: {result.get('title', '')}\n"
                         f"URL: {result.get('url', '')}\n"
                         f"Content: {result.get('content', '')[:500]}...\n")
        
        return "\n---\n".join(results)
    except Exception as e:
        return f"Search failed: {str(e)}"

def find_companies(industry: str, country: str, num_companies: int = 5) -> str:
    """Find companies in specific industry and country"""
    query = f"{industry} companies {country} startups funding investment 2024"
    return web_search(query, num_companies)

def research_company(company_name: str) -> str:
    """Research a specific company's background and investment patterns"""
    query = f"{company_name} company funding investment history expansion strategy"
    return web_search(query, 3)

def validate_company(company_name: str, industry: str) -> str:
    """Validate if a company is legitimate and relevant"""
    query = f"{company_name} {industry} verified company information"
    return web_search(query, 2)