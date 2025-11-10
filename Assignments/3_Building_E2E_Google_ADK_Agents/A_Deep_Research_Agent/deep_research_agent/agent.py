from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from tools.search_tools import web_search, company_research

# Root agent instruction
ROOT_AGENT_INSTRUCTION = """
You are a lead generation assistant. Your objective is to assist the user in finding new leads by discovering patterns in successful companies. 

Use your search tools to find relevant companies when users ask about specific industries or regions.
Always search first, then provide insights based on what you find.
"""

# Create tools
search_tool = FunctionTool(
    func=web_search,
    name="web_search", 
    description="Search for companies in specific industries and regions"
)

research_tool = FunctionTool(
    func=company_research,
    name="company_research",
    description="Get detailed information about a specific company"
)

# Agent with tools
root_agent = Agent(
    name="InteractiveLeadGenerator",
    model="gemini-2.0-flash",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[search_tool, research_tool]
)