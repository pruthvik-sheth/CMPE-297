# MCP & A2A Protocol Assignment

## Overview

This repository contains implementations of three Google Codelabs focused on building multi-agent systems using cutting-edge AI agent technologies: Model Context Protocol (MCP), Agent Development Kit (ADK), and Agent2Agent (A2A) Protocol.

The assignment demonstrates how to create production-ready AI agents that can communicate with each other, access external tools, and work together regardless of the framework they're built with.

## What These Technologies Do

- **MCP (Model Context Protocol)**: Standardizes how agents connect to external tools and data sources
- **ADK (Agent Development Kit)**: Google's framework for building and orchestrating AI agents
- **A2A (Agent2Agent Protocol)**: Enables agents from different frameworks to discover and communicate with each other

## Repository Structure

```
2_MCP_A2A_Codelab/
├── README.md (this file)
├── 1_Multiagent_System_with_ADK/
│   ├── README.md
│   └── imagescoring/
├── 2_Getting_started_with_ADK_MCP_A2A/
│   ├── README.md
│   └── currency_agent/
└── 3_Getting_Started_with_A2A_Action_Engine/
    ├── README.md
    └── purchasing_concierge/
```

## Codelabs

### 1. Multi-Agent System with ADK and A2A Protocol

Build and deploy a hierarchical multi-agent system for image scoring using ADK and A2A protocol.

**What You'll Build**: An image scoring system with multiple specialized agents working together  
**Key Focus**: Multi-agent architecture, ADK basics, A2A protocol, Agent Engine deployment  
**Link**: https://codelabs.developers.google.com/codelabs/create-multi-agents-adk-a2a#0  
**Video**: [Add your video link]  
**Code**: `1_Multiagent_System_with_ADK/`

---

### 2. Getting Started with ADK, MCP and A2A

Create a currency converter agent that integrates all three technologies: MCP for tools, ADK for orchestration, and A2A for agent communication.

**What You'll Build**: A currency conversion agent accessible to other agents  
**Key Focus**: MCP tool integration, ADK agent building, A2A exposure, Cloud Run deployment  
**Link**: https://codelabs.developers.google.com/codelabs/currency-agent#0  
**Video**: [Add your video link]  
**Code**: `2_Getting_started_with_ADK_MCP_A2A/`

---

### 3. A2A Action Engine - Purchasing Concierge

Build a purchasing concierge system where agents built with different frameworks (ADK, CrewAI, LangGraph) communicate via A2A protocol.

**What You'll Build**: A multi-framework purchasing system with specialized seller agents  
**Key Focus**: Multi-framework integration, A2A client-server, microservices architecture  
**Link**: https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0  
**Video**: [Add your video link]  
**Code**: `3_Getting_Started_with_A2A_Action_Engine/`

---

## Technologies Stack

| Technology | Purpose | Used In |
|------------|---------|---------|
| **ADK** | Agent orchestration | All codelabs |
| **MCP** | Tool/data integration | Codelabs 2, 3 |
| **A2A** | Agent communication | All codelabs |
| **CrewAI** | Agent framework | Codelab 3 |
| **LangGraph** | Agent framework | Codelab 3 |
| **Cloud Run** | Serverless hosting | Codelabs 2, 3 |
| **Agent Engine** | Managed deployment | Codelabs 1, 3 |
| **Python** | Programming language | All codelabs |

## Prerequisites

- Google Cloud Platform account with billing enabled
- Python 3.10 or higher
- Google Cloud SDK installed
- Basic understanding of:
  - Python programming
  - REST APIs
  - Cloud computing concepts
  - Command-line interfaces