import os
from google.adk.agents import Agent
from google.adk.tools import AgentTool

# Import specialized agents
from .agents.bug_analysis_agents import (
    error_analyzer_agent,
    fix_suggestion_agent,
    documentation_agent,
    dependency_checker_agent,
    fix_validator_agent,
    parallel_analysis_agent,
    bug_assistance_workflow
)

# Convert agents to tools
agent_tools = [
    AgentTool(agent=error_analyzer_agent),
    AgentTool(agent=fix_suggestion_agent),
    AgentTool(agent=documentation_agent),
    AgentTool(agent=dependency_checker_agent),
    AgentTool(agent=fix_validator_agent),
    AgentTool(agent=bug_assistance_workflow)
]

# Main instruction
ROOT_AGENT_INSTRUCTION = """
You are a comprehensive software bug assistance agent that uses Model Context Protocol (MCP) tools to help developers debug, fix, and prevent software issues.

Your capabilities:
1. **Error Analysis** - Use ErrorAnalyzerAgent to analyze stack traces and error logs
2. **Fix Suggestions** - Use FixSuggestionAgent to recommend targeted bug fixes  
3. **Documentation Search** - Use DocumentationAgent to find relevant resources
4. **Dependency Checking** - Use DependencyCheckerAgent to analyze project dependencies
5. **Fix Validation** - Use FixValidatorAgent to validate proposed solutions
6. **Complete Workflow** - Use BugAssistanceWorkflow for comprehensive analysis

Workflow Recommendations:
- For simple bugs → Use individual specialist agents
- For complex issues → Use BugAssistanceWorkflow for complete analysis
- Always validate fixes before implementation

Be thorough, practical, and provide actionable solutions.
"""

# Root agent
root_agent = Agent(
    name="MCPBugAssistant",
    model="gemini-2.5-flash",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=agent_tools
)