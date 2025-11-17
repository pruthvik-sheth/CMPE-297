from google.adk.agents import LlmAgent

from ..tools.gemini_cli_tool import (
    analyze_code_with_cli, 
    generate_code_with_cli, 
    debug_code_with_cli,
    refactor_code_with_cli,
    create_tests_with_cli
)

code_analyzer_agent = LlmAgent(
    name="CodeAnalyzerAgent",
    model="gemini-2.0-flash",
    instruction="""You are a code analysis specialist. Use the Gemini CLI tools to:
    1. Analyze code quality and performance
    2. Identify bugs and issues
    3. Suggest improvements
    
    Always use the analyze_code_with_cli tool for code analysis tasks.""",
    tools=[analyze_code_with_cli],
    description="Analyzes code quality, performance, and identifies issues"
)

code_generator_agent = LlmAgent(
    name="CodeGeneratorAgent", 
    model="gemini-2.0-flash",
    instruction="""You are a code generation specialist. Use the Gemini CLI tools to:
    1. Generate clean, production-ready code
    2. Follow best practices and patterns
    3. Include proper documentation
    
    Always use the generate_code_with_cli tool for code generation tasks.""",
    tools=[generate_code_with_cli],
    description="Generates code based on requirements and specifications"
)

code_debugger_agent = LlmAgent(
    name="CodeDebuggerAgent",
    model="gemini-2.0-flash", 
    instruction="""You are a debugging specialist. Use the Gemini CLI tools to:
    1. Identify and fix bugs in code
    2. Explain root causes of issues
    3. Provide corrected solutions
    
    Always use the debug_code_with_cli tool for debugging tasks.""",
    tools=[debug_code_with_cli],
    description="Debugs code and fixes errors"
)

code_refactor_agent = LlmAgent(
    name="CodeRefactorAgent",
    model="gemini-2.0-flash",
    instruction="""You are a refactoring specialist. Use the Gemini CLI tools to:
    1. Improve code structure and readability
    2. Optimize performance
    3. Apply design patterns
    
    Always use the refactor_code_with_cli tool for refactoring tasks.""",
    tools=[refactor_code_with_cli],
    description="Refactors and improves existing code"
)

test_generator_agent = LlmAgent(
    name="TestGeneratorAgent",
    model="gemini-2.0-flash",
    instruction="""You are a test generation specialist. Use the Gemini CLI tools to:
    1. Create comprehensive unit tests
    2. Cover edge cases and error conditions
    3. Follow testing best practices
    
    Always use the create_tests_with_cli tool for test generation tasks.""",
    tools=[create_tests_with_cli],
    description="Generates unit tests for code"
)