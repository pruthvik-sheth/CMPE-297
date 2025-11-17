from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.mcp_tools import (
    analyze_error_log,
    suggest_fix,
    search_documentation,
    check_dependencies,
    validate_fix
)

# Bug Analysis Agents
error_analyzer_agent = LlmAgent(
    name="ErrorAnalyzerAgent",
    model="gemini-2.5-flash",
    instruction="""You are an error analysis specialist. Use the MCP analyze_error_log tool to:
    1. Analyze stack traces and error logs
    2. Identify error patterns and root causes
    3. Assess severity and impact
    
    Always use the analyze_error_log tool for error analysis tasks.""",
    tools=[analyze_error_log],
    description="Analyzes error logs and stack traces using MCP protocol"
)

fix_suggestion_agent = LlmAgent(
    name="FixSuggestionAgent",
    model="gemini-2.5-flash",
    instruction="""You are a fix suggestion specialist. Use the MCP suggest_fix tool to:
    1. Provide targeted bug fix recommendations
    2. Suggest best practices and patterns
    3. Recommend testing strategies
    
    Always use the suggest_fix tool for bug fix suggestions.""",
    tools=[suggest_fix],
    description="Suggests fixes for reported bugs using MCP protocol"
)

documentation_agent = LlmAgent(
    name="DocumentationAgent",
    model="gemini-2.5-flash",
    instruction="""You are a documentation research specialist. Use the MCP search_documentation tool to:
    1. Find relevant documentation and resources
    2. Provide learning materials and examples
    3. Suggest official references
    
    Always use the search_documentation tool for documentation searches.""",
    tools=[search_documentation],
    description="Searches documentation using MCP protocol"
)

dependency_checker_agent = LlmAgent(
    name="DependencyCheckerAgent",
    model="gemini-2.5-flash",
    instruction="""You are a dependency analysis specialist. Use the MCP check_dependencies tool to:
    1. Analyze project dependencies
    2. Identify outdated or vulnerable packages
    3. Recommend updates and security patches
    
    Always use the check_dependencies tool for dependency analysis.""",
    tools=[check_dependencies],
    description="Checks dependencies using MCP protocol"
)

fix_validator_agent = LlmAgent(
    name="FixValidatorAgent",
    model="gemini-2.5-flash",
    instruction="""You are a fix validation specialist. Use the MCP validate_fix tool to:
    1. Validate proposed bug fixes
    2. Check for potential side effects
    3. Ensure code quality standards
    
    Always use the validate_fix tool for fix validation.""",
    tools=[validate_fix],
    description="Validates proposed fixes using MCP protocol"
)

# Parallel analysis workflow
parallel_analysis_agent = ParallelAgent(
    name="ParallelAnalysisAgent",
    sub_agents=[error_analyzer_agent, documentation_agent, dependency_checker_agent],
    description="Runs error analysis, documentation search, and dependency check in parallel"
)

# Complete bug assistance workflow
bug_assistance_workflow = SequentialAgent(
    name="BugAssistanceWorkflow",
    sub_agents=[
        parallel_analysis_agent,
        fix_suggestion_agent,
        fix_validator_agent
    ],
    description="Complete workflow for comprehensive bug analysis and assistance"
)