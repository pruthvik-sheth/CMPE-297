# AI Agents Using Google ADK

Complete implementation of Google ADK codelabs and hackathon projects demonstrating multi-agent AI systems from prototypes to production.

## About This Project

This repository showcases the full journey of building AI agents with Google's Agent Development Kit (ADK) - from simple prototypes to sophisticated multi-agent systems. Each implementation includes working code, comprehensive documentation, and video demonstrations.

## What You'll Learn

- **Agent Development Fundamentals**: Core ADK concepts and agent lifecycle management
- **Tool Integration**: Custom functions, built-in tools, and external API connections
- **Multi-Agent Orchestration**: Complex workflows and agent-to-agent communication
- **Database Integration**: MCP Toolbox for secure database interactions
- **Production Deployment**: Cloud-ready agent systems with proper authentication

## Project Structure

### Part A: Official ADK Codelabs

#### A1_Prototypes_to_Agents
Kitchen renovation proposal agent demonstrating the transition from AI Studio prototyping to production ADK agents with Cloud Storage integration.

#### A2_AI_Agents_with_Tools  
Personal assistant agent enhanced with custom tools, Google Search, and sub-agent delegation patterns for complex task handling.

#### A3_Travel_Agent_MCP
Hotel search and booking agent using MCP Toolbox for Databases to enable natural language querying of Cloud SQL PostgreSQL databases.

### Part B: Community Innovation

#### B_Hackathon_Agent
Advanced multi-agent system inspired by winning projects from the Google Cloud ADK Hackathon ($50,000 prize pool, 476 submissions worldwide).

## Prerequisites

- Google Cloud Platform account with billing enabled
- Python 3.8+ or Java 11+
- Agent Development Kit (ADK) installed
- Access to Vertex AI and Gemini APIs

## Quick Start

```bash
# Install ADK
pip install google-adk

# Set up credentials
export GOOGLE_API_KEY="your-api-key"
export GOOGLE_CLOUD_PROJECT="your-project-id"

# Navigate to any project
cd [A1_Prototypes_to_Agents | A2_AI_Agents_with_Tools | A3_Travel_Agent_MCP | B_Hackathon_Agent]

# Install dependencies
pip install -r requirements.txt

# Launch agent
adk web
```

## Resources

- [Agent Development Kit Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [Awesome ADK Agents Community](https://github.com/Sri-Krishna-V/awesome-adk-agents)
- [ADK Hackathon Gallery](https://googlecloudmultiagents.devpost.com/project-gallery)

Complete code implementations and video demonstrations available in respective directories.