from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from deep_research_agent.tools.search_tools import find_companies, research_company, validate_company

lead_finder_agent = LlmAgent(
    name="LeadFinderAgent",
    model="gemini-2.5-flash",
    instruction="Use discovered patterns to find new companies showing similar signals. Search for companies exhibiting the identified pre-investment behaviors.",
    tools=[find_companies],
    description="Finds new leads based on discovered patterns"
)

lead_formatter_agent = LlmAgent(
    name="LeadFormatterAgent",
    model="gemini-2.5-flash", 
    instruction="Structure lead data for parallel processing. Format company information consistently.",
    description="Formats lead data for analysis"
)

validator_agent = LlmAgent(
    name="ValidatorAgent",
    model="gemini-2.5-flash",
    instruction="Validate company information and ensure data quality. Check if companies meet basic criteria.",
    tools=[validate_company],
    description="Validates company data quality"
)

lead_signal_analyzer_agent = LlmAgent(
    name="LeadSignalAnalyzerAgent",
    model="gemini-2.5-flash",
    instruction="Analyze leads to identify specific investment signals they are showing. Match against discovered patterns.",
    tools=[research_company],
    description="Analyzes investment signals in potential leads"
)

lead_research_orchestrator_agent = ParallelAgent(
    name="LeadResearchOrchestratorAgent", 
    sub_agents=[validator_agent, lead_signal_analyzer_agent],
    description="Manages parallel validation and analysis of leads"
)

report_orchestrator_agent = LlmAgent(
    name="ReportOrchestratorAgent",
    model="gemini-2.5-flash",
    instruction="Consolidate lead analysis findings into structured data for final reporting.",
    description="Consolidates lead analysis data"
)

report_compiler_agent = LlmAgent(
    name="ReportCompilerAgent",
    model="gemini-2.5-flash",
    instruction="Compile comprehensive lead generation report with analysis, recommendations, and confidence scores for each lead.",
    description="Compiles final lead generation report"
)

# Lead generation workflow
lead_generation_agent = SequentialAgent(
    name="LeadGenerationAgent",
    sub_agents=[
        lead_finder_agent,
        lead_formatter_agent, 
        lead_research_orchestrator_agent,
        report_orchestrator_agent,
        report_compiler_agent,
    ],
    description="Uses pre-discovered success patterns to find potential leads."
)