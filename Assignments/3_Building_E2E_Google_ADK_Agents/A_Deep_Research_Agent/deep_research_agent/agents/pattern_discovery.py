from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from deep_research_agent.tools.search_tools import find_companies, research_company, validate_company

# Individual specialized agents
company_finder_agent = LlmAgent(
    name="CompanyFinderAgent",
    model="gemini-2.5-flash",
    instruction="Find companies that have successfully invested in the target market. Use the find_companies tool to search for relevant companies.",
    tools=[find_companies],
    description="Finds companies in specific industries and regions"
)

company_formatter_agent = LlmAgent(
    name="CompanyFormatterAgent", 
    model="gemini-2.5-flash",
    instruction="Take raw company search results and format them into a clean, structured list with company names, descriptions, and key details.",
    description="Formats company data into structured format"
)

validator_agent = LlmAgent(
    name="ValidatorAgent",
    model="gemini-2.5-flash", 
    instruction="Validate companies against strict criteria: legitimate business, relevant to target industry, recent activity, sufficient information available.",
    tools=[validate_company],
    description="Validates company legitimacy and relevance"
)

researcher_agent = LlmAgent(
    name="ResearcherAgent",
    model="gemini-2.5-flash",
    instruction="Research company backgrounds, investment patterns, and pre-investment signals. Focus on activities 6-12 months before major investments.",
    tools=[research_company],
    description="Researches company investment patterns and signals"
)

# Parallel orchestrator for research
research_orchestrator_agent = ParallelAgent(
    name="ResearchOrchestratorAgent",
    sub_agents=[validator_agent, researcher_agent],
    description="Manages parallel validation and research of companies"
)

synthesizer_orchestrator_agent = LlmAgent(
    name="SynthesizerOrchestratorAgent",
    model="gemini-2.5-flash",
    instruction="Gather and consolidate all research data from parallel pipelines. Prepare unified dataset for pattern analysis.",
    description="Consolidates research data"
)

pattern_synthesizer_agent = LlmAgent(
    name="PatternSynthesizerAgent",
    model="gemini-2.5-flash",  # Use more powerful model for analysis
    instruction="Analyze consolidated company data to identify common investment patterns. Look for: timing patterns, market entry strategies, funding stages, geographic expansion patterns, technology adoption signals. Provide evidence-based patterns with source citations.",
    description="Identifies and synthesizes investment patterns"
)

# Main pattern discovery workflow
pattern_discovery_agent = SequentialAgent(
    name="PatternDiscoveryAgent",
    sub_agents=[
        company_finder_agent,
        company_formatter_agent,
        research_orchestrator_agent,
        synthesizer_orchestrator_agent,
        pattern_synthesizer_agent,
    ],
    description="Orchestrates the multi-step process of discovering investment patterns."
)