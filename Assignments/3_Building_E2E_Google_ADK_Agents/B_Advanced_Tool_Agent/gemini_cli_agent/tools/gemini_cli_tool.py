import subprocess
import os
import re
from typing import Dict, Any, Optional

def call_gemini_cli(prompt: str, model: str = "gemini-2.0-flash") -> str:
    """Execute Gemini CLI as a tool"""
    try:
        # Get API key from environment
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Error: GOOGLE_API_KEY not found in environment"
        
        # Set up environment with API key for Gemini CLI
        env = os.environ.copy()
        env["GEMINI_API_KEY"] = api_key
        
        # Escape the prompt for shell - replace quotes
        escaped_prompt = prompt.replace('"', '\\"').replace('\n', ' ')
        
        # Call Gemini CLI with the prompt in non-interactive mode
        # Using output-format text to get clean output
        cmd = f'gemini --output-format text "{escaped_prompt}"'
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            env=env,
            shell=True,
            stdin=subprocess.DEVNULL  # Prevent interactive mode
        )
        
        if result.returncode == 0:
            # Clean up the output - remove CLI formatting
            output = result.stdout.strip()
            # Remove any ANSI color codes or special characters
            output = re.sub(r'\x1b\[[0-9;]*m', '', output)
            return output if output else "No response from Gemini CLI"
        else:
            error = result.stderr.strip()
            return f"Gemini CLI Error: {error if error else 'Unknown error'}"
            
    except subprocess.TimeoutExpired:
        return "Gemini CLI call timed out after 30 seconds"
    except Exception as e:
        return f"Error calling Gemini CLI: {str(e)}"

def analyze_code_with_cli(code: str, analysis_type: str = "general") -> str:
    """Use Gemini CLI to analyze code"""
    prompt = f"""Analyze this code for {analysis_type}:

{code}

Provide:
1. Code quality assessment  
2. Potential issues
3. Improvements
4. Best practices"""
    
    return call_gemini_cli(prompt)

def generate_code_with_cli(requirements: str, language: str = "python") -> str:
    """Use Gemini CLI to generate code from requirements"""
    prompt = f"""Generate {language} code for the following requirements:

{requirements}

Provide:
1. Clean, production-ready code
2. Proper documentation and comments
3. Error handling
4. Best practices"""
    
    return call_gemini_cli(prompt)

def debug_code_with_cli(code: str, error_message: str = "") -> str:
    """Use Gemini CLI to debug code and fix errors"""
    prompt = f"""Debug this code and fix the errors:

Code:
{code}

Error message:
{error_message}

Provide:
1. Root cause analysis
2. Fixed code
3. Explanation of the fix"""
    
    return call_gemini_cli(prompt)

def refactor_code_with_cli(code: str, refactor_goal: str = "improve readability") -> str:
    """Use Gemini CLI to refactor code"""
    prompt = f"""Refactor this code to {refactor_goal}:

{code}

Provide:
1. Refactored code
2. Explanation of changes
3. Performance improvements"""
    
    return call_gemini_cli(prompt)

def create_tests_with_cli(code: str, test_framework: str = "pytest") -> str:
    """Use Gemini CLI to generate unit tests"""
    prompt = f"""Generate comprehensive {test_framework} unit tests for this code:

{code}

Provide:
1. Complete test suite
2. Edge case coverage
3. Mock/fixture setup if needed"""
    
    return call_gemini_cli(prompt)
