from google.adk.agents import Agent
from google.adk.tools import AgentTool

# Import sub-agents with absolute imports
from deep_research_agent.agents.intent_extractor import intent_extractor_agent
from deep_research_agent.agents.pattern_discovery import pattern_discovery_agent 
from deep_research_agent.agents.lead_generation import lead_generation_agent

from typing import List

def get_user_choice(question: str, options: List[str]) -> str:
    """Get user choice from multiple options"""
    choice_text = f"{question}\n"
    for i, option in enumerate(options, 1):
        choice_text += f"{i}. {option}\n"
    choice_text += "Please choose a number or describe your preference."
    return choice_text

# State management callbacks
def before_agent_run(callback_context) -> None:
    """Initialize session state before agent run"""
    session = callback_context.session
    if 'stage' not in session.state:
        session.state['stage'] = 'intent_extraction'
        session.state['discovered_patterns'] = None
        session.state['user_confirmed'] = False

def after_tool_run(callback_context=None, **kwargs) -> None:
    """Update session state after tool execution"""
    if callback_context is None:
        return
    
    session = callback_context.session
    tool_name = callback_context.tool_name
    tool_output = callback_context.tool_output
    
    if tool_name == "intent_extractor_agent":
        session.state['stage'] = 'pattern_discovery'
    elif tool_name == "pattern_discovery_agent":
        session.state['stage'] = 'pattern_confirmation'
        session.state['discovered_patterns'] = tool_output
    elif tool_name == "lead_generation_agent":
        session.state['stage'] = 'completed'

# Convert agents to tools
agent_tools = [
    AgentTool(agent=intent_extractor_agent),
    AgentTool(agent=pattern_discovery_agent),
    AgentTool(agent=lead_generation_agent)
]

# Root agent instruction
ROOT_AGENT_INSTRUCTION = """
You are a lead generation assistant. Your objective is to assist the user in finding new leads by discovering patterns in successful companies. 

Your process is to:
1. Understand user intent - Use intent_extractor_agent to parse requests
2. Execute a pattern discovery workflow - Use pattern_discovery_agent to analyze successful companies
3. Confirm findings with the user - Present patterns and get user approval
4. Execute a lead generation workflow based on confirmed patterns - Use lead_generation_agent to find new leads

Maintain an interactive, proactive, and thorough approach.
"""

# Main root agent
root_agent = Agent(
    name="InteractiveLeadGenerator",
    model="gemini-2.5-flash",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[
        get_user_choice,
        *agent_tools,
    ],
    before_agent_callback=[before_agent_run],
    after_tool_callback=[after_tool_run],
)