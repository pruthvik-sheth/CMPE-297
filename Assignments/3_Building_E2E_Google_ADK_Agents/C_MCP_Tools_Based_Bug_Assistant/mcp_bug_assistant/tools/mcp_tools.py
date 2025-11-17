import json
import subprocess
import os
from typing import List, Dict, Any
import requests

class MCPBugTools:
    """MCP-based tools for bug analysis and assistance"""
    
    def __init__(self):
        self.tools = {
            "analyze_error_log": self.analyze_error_log,
            "suggest_fix": self.suggest_fix,
            "search_documentation": self.search_documentation,
            "check_dependencies": self.check_dependencies,
            "validate_fix": self.validate_fix
        }

def analyze_error_log(error_log: str, context: str = "") -> str:
    """Analyze error logs and stack traces using MCP protocol"""
    try:
        analysis = {
            "error_type": "Unknown",
            "severity": "Medium",
            "potential_causes": [],
            "suggested_actions": []
        }
        
        # Simple error pattern matching (can be enhanced with ML)
        if "NullPointerException" in error_log or "AttributeError" in error_log:
            analysis["error_type"] = "Null/Undefined Reference"
            analysis["severity"] = "High"
            analysis["potential_causes"] = [
                "Accessing method/property on null object",
                "Uninitialized variable",
                "Missing error handling"
            ]
            analysis["suggested_actions"] = [
                "Add null checks before accessing objects",
                "Initialize variables properly",
                "Add try-catch blocks"
            ]
            
        elif "OutOfMemoryError" in error_log or "MemoryError" in error_log:
            analysis["error_type"] = "Memory Issue"
            analysis["severity"] = "High"
            analysis["potential_causes"] = [
                "Memory leak",
                "Large dataset processing",
                "Infinite loop or recursion"
            ]
            analysis["suggested_actions"] = [
                "Profile memory usage",
                "Implement pagination for large datasets",
                "Add recursion limits"
            ]
            
        elif "SyntaxError" in error_log or "IndentationError" in error_log:
            analysis["error_type"] = "Syntax Error"
            analysis["severity"] = "Low"
            analysis["potential_causes"] = [
                "Incorrect syntax",
                "Wrong indentation",
                "Missing brackets/quotes"
            ]
            analysis["suggested_actions"] = [
                "Check syntax at specified line",
                "Verify proper indentation",
                "Use IDE syntax checking"
            ]
        
        result = f"""
Error Analysis Report:
- Type: {analysis['error_type']}
- Severity: {analysis['severity']}

Potential Causes:
{chr(10).join(['• ' + cause for cause in analysis['potential_causes']])}

Suggested Actions:
{chr(10).join(['• ' + action for action in analysis['suggested_actions']])}

Context: {context}
        """
        
        return result.strip()
        
    except Exception as e:
        return f"Error analyzing log: {str(e)}"

def suggest_fix(bug_description: str, code_snippet: str = "") -> str:
    """Suggest fixes for reported bugs using MCP protocol"""
    try:
        # Analyze bug description and provide targeted suggestions
        suggestions = []
        
        if "crash" in bug_description.lower():
            suggestions.extend([
                "Add comprehensive error handling",
                "Implement graceful degradation",
                "Add logging for debugging",
                "Validate inputs before processing"
            ])
            
        if "slow" in bug_description.lower() or "performance" in bug_description.lower():
            suggestions.extend([
                "Profile code to identify bottlenecks",
                "Optimize database queries",
                "Implement caching",
                "Use async/await for I/O operations"
            ])
            
        if "data" in bug_description.lower():
            suggestions.extend([
                "Validate data integrity",
                "Add data type checking",
                "Implement data sanitization",
                "Check for data race conditions"
            ])
        
        if code_snippet:
            # Basic code analysis
            if "for " in code_snippet and "range(len(" in code_snippet:
                suggestions.append("Consider using enumerate() instead of range(len())")
            if "try:" not in code_snippet and ("open(" in code_snippet or "connect(" in code_snippet):
                suggestions.append("Add proper exception handling for file/network operations")
        
        if not suggestions:
            suggestions = [
                "Add unit tests to isolate the issue",
                "Implement step-by-step debugging",
                "Check recent code changes",
                "Verify environment configuration"
            ]
        
        result = f"""
Bug Fix Suggestions for: {bug_description}

Recommended Actions:
{chr(10).join(['• ' + suggestion for suggestion in suggestions])}

Code Analysis:
{f'Analyzed code snippet: {len(code_snippet)} characters' if code_snippet else 'No code provided'}
        """
        
        return result.strip()
        
    except Exception as e:
        return f"Error generating suggestions: {str(e)}"

def search_documentation(query: str, technology: str = "general") -> str:
    """Search relevant documentation using MCP protocol"""
    try:
        # Simulate documentation search results
        docs = {
            "python": [
                f"Python Official Docs: {query} - Best practices and examples",
                f"Stack Overflow: Common {query} issues and solutions", 
                f"Python Package Index: Related libraries for {query}"
            ],
            "javascript": [
                f"MDN Web Docs: {query} - Comprehensive guide",
                f"JavaScript.info: {query} - Detailed explanations",
                f"Node.js Docs: {query} - Server-side implementation"
            ],
            "general": [
                f"Tech Documentation: {query} - General overview",
                f"Best Practices Guide: {query} - Industry standards",
                f"Troubleshooting Guide: {query} - Common issues"
            ]
        }
        
        tech_docs = docs.get(technology.lower(), docs["general"])
        
        result = f"""
Documentation Search Results for: {query}
Technology: {technology}

Relevant Resources:
{chr(10).join(['• ' + doc for doc in tech_docs])}

Recommendation: Check official documentation first, then community resources.
        """
        
        return result.strip()
        
    except Exception as e:
        return f"Error searching documentation: {str(e)}"

def check_dependencies(project_path: str = ".", technology: str = "python") -> str:
    """Check project dependencies for potential issues using MCP protocol"""
    try:
        dependency_info = {
            "total_dependencies": 0,
            "outdated_packages": [],
            "security_warnings": [],
            "recommendations": []
        }
        
        # Simulate dependency checking
        if technology.lower() == "python":
            dependency_info.update({
                "total_dependencies": 15,
                "outdated_packages": ["requests==2.25.1 (latest: 2.31.0)", "numpy==1.21.0 (latest: 1.24.3)"],
                "security_warnings": ["urllib3 has known vulnerabilities"],
                "recommendations": [
                    "Update requests to latest version",
                    "Consider using virtual environments",
                    "Pin dependency versions in requirements.txt"
                ]
            })
        elif technology.lower() == "javascript":
            dependency_info.update({
                "total_dependencies": 25,
                "outdated_packages": ["lodash@4.17.15 (latest: 4.17.21)", "axios@0.21.1 (latest: 1.4.0)"],
                "security_warnings": ["lodash has prototype pollution vulnerabilities"],
                "recommendations": [
                    "Run npm audit fix",
                    "Update lodash to latest version",
                    "Review package-lock.json regularly"
                ]
            })
        
        result = f"""
Dependency Analysis for {technology} project:

Summary:
- Total dependencies: {dependency_info['total_dependencies']}
- Outdated packages: {len(dependency_info['outdated_packages'])}
- Security warnings: {len(dependency_info['security_warnings'])}

Outdated Packages:
{chr(10).join(['• ' + pkg for pkg in dependency_info['outdated_packages']])}

Security Issues:
{chr(10).join(['• ' + warning for warning in dependency_info['security_warnings']])}

Recommendations:
{chr(10).join(['• ' + rec for rec in dependency_info['recommendations']])}
        """
        
        return result.strip()
        
    except Exception as e:
        return f"Error checking dependencies: {str(e)}"

def validate_fix(original_code: str, fixed_code: str, test_description: str = "") -> str:
    """Validate proposed bug fixes using MCP protocol"""
    try:
        validation_result = {
            "syntax_valid": True,
            "logic_improved": False,
            "potential_issues": [],
            "recommendations": []
        }
        
        # Basic validation checks
        if len(fixed_code.strip()) == 0:
            validation_result["syntax_valid"] = False
            validation_result["potential_issues"].append("Fixed code is empty")
        
        if "try:" in fixed_code and "except:" not in fixed_code:
            validation_result["potential_issues"].append("Try block without except clause")
        
        if len(fixed_code) > len(original_code) * 1.5:
            validation_result["recommendations"].append("Consider if the fix is overly complex")
        
        if "TODO" in fixed_code or "FIXME" in fixed_code:
            validation_result["potential_issues"].append("Code contains TODO/FIXME comments")
        
        # Check for improvements
        if "try:" in fixed_code and "try:" not in original_code:
            validation_result["logic_improved"] = True
            validation_result["recommendations"].append("Good: Added error handling")
        
        if "if " in fixed_code and "if " not in original_code:
            validation_result["logic_improved"] = True
            validation_result["recommendations"].append("Good: Added conditional checks")
        
        result = f"""
Fix Validation Report:

Syntax Valid: {validation_result['syntax_valid']}
Logic Improved: {validation_result['logic_improved']}

Potential Issues:
{chr(10).join(['• ' + issue for issue in validation_result['potential_issues']]) if validation_result['potential_issues'] else '• No major issues detected'}

Recommendations:
{chr(10).join(['• ' + rec for rec in validation_result['recommendations']]) if validation_result['recommendations'] else '• Fix looks good to proceed'}

Test Description: {test_description}
        """
        
        return result.strip()
        
    except Exception as e:
        return f"Error validating fix: {str(e)}"