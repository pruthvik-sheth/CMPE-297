import os
from google.adk.agents import Agent
from google.adk.tools import AgentTool

# Import specialized agents
from .agents.code_analysis_agent import (
    code_analyzer_agent,
    code_generator_agent,
    code_debugger_agent,
    code_refactor_agent,
    test_generator_agent
)

# Convert agents to tools
agent_tools = [
    AgentTool(agent=code_analyzer_agent),
    AgentTool(agent=code_generator_agent),
    AgentTool(agent=code_debugger_agent),
    AgentTool(agent=code_refactor_agent),
    AgentTool(agent=test_generator_agent)
]

# Main instruction
ROOT_AGENT_INSTRUCTION = """
You are an advanced coding assistant that uses Gemini CLI as a powerful tool for code analysis, generation, and improvement.

Your capabilities:
1. **Code Analysis** - Use CodeAnalyzerAgent to analyze code quality, performance, and identify issues
2. **Code Generation** - Use CodeGeneratorAgent to create new code from requirements  
3. **Debugging** - Use CodeDebuggerAgent to find and fix bugs
4. **Refactoring** - Use CodeRefactorAgent to improve code structure and performance
5. **Test Generation** - Use TestGeneratorAgent to create comprehensive unit tests

Workflow:
- For code analysis requests → Use CodeAnalyzerAgent
- For code generation requests → Use CodeGeneratorAgent  
- For debugging requests → Use CodeDebuggerAgent
- For refactoring requests → Use CodeRefactorAgent
- For test creation requests → Use TestGeneratorAgent

Always delegate to the appropriate specialist agent based on the user's needs.
Provide clear explanations and actionable recommendations.
"""

# Root agent
root_agent = Agent(
    name="GeminiCliAgent",
    model="gemini-2.0-flash", 
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=agent_tools
)