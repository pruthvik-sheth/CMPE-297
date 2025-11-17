# Codelab 2: Getting Started with ADK, MCP and A2A

## Overview

This codelab provides a comprehensive introduction to building AI agents using three key technologies: Model Context Protocol (MCP), Agent Development Kit (ADK), and Agent2Agent (A2A) Protocol.

You'll build a currency converter agent that demonstrates how these technologies work together. The agent can convert between different currencies using MCP tools, is orchestrated by ADK, and can be discovered and used by other agents through the A2A protocol.

## What You'll Learn

- Create and deploy MCP servers that provide tools to agents
- Build agents using Google's Agent Development Kit (ADK)
- Connect ADK agents to MCP tools for external data access
- Expose agents via A2A protocol for inter-agent communication
- Deploy agents to Google Cloud Run for production use
- Understand how MCP, ADK, and A2A complement each other

## The Currency Agent

The agent you'll build can:
- Convert between different country currencies (e.g., "What is 250 CAD to USD?")
- Access real-time exchange rates through MCP tools
- Be discovered by other agents via Agent Cards
- Handle natural language queries about currency conversion

### How It Works

```
User Query → ADK Agent → MCP Tools → Currency API
                ↓
          A2A Protocol
                ↓
    Other Agents Can Use It
```

- **MCP** provides standardized access to currency conversion tools
- **ADK** orchestrates the agent's reasoning and tool usage
- **A2A** makes the agent discoverable and usable by other agents

## Codelab Link

🔗 **[Access the Full Codelab](https://codelabs.developers.google.com/codelabs/currency-agent#0)**

## Video Walkthrough

📹 **[Watch Video Tutorial](https://youtu.be/t8su3M-3FPo)**

## Code Location in Repository

```
2_MCP_A2A_Codelab/
└── 2_Getting_started_with_ADK_MCP_A2A/
```

## Technologies Used

- **Model Context Protocol (MCP)** - Standardizes how agents access tools and data
- **Google Agent Development Kit (ADK)** - Agent orchestration framework
- **Agent2Agent (A2A) Protocol** - Enables agent-to-agent communication
- **Google Cloud Run** - Serverless deployment platform
- **Python** - Primary programming language
- **Gemini Models** - Google's LLMs for agent reasoning

## Development Features

### Testing Locally
Use ADK's dev UI to test your agent:
```bash
adk web
```
Access at `http://localhost:8000`

### Agent Card
Your agent publishes capabilities at `/.well-known/agent.json` including:
- Agent skills and what it can do
- How other agents can interact with it
- Authentication requirements

## Prerequisites

- Google Cloud Platform account with billing enabled
- Python 3.10+ installed
- Basic understanding of REST APIs
- Familiarity with cloud deployment concepts