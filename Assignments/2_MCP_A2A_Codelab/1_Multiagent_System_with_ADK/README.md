# Codelab 1: Multi-Agent System with ADK and A2A Protocol

## Overview

This codelab teaches you to build a multi-agent system using Google's Agent Development Kit (ADK), deploy it to Google Cloud's Agent Engine, and implement the Agent2Agent (A2A) protocol for inter-agent communication.

You'll create an image scoring system where multiple specialized agents work together in a hierarchical structure. This demonstrates how to build modular, scalable applications by composing multiple agents that can delegate tasks to each other.

## What You'll Learn

- Build multi-agent systems with hierarchical agent structures
- Use Google's Agent Development Kit (ADK) for agent development
- Deploy agents to Vertex AI Agent Engine on Google Cloud Platform
- Implement A2A protocol for agent discovery and communication
- Create and publish Agent Cards that describe agent capabilities
- Work with Cloud Storage and other GCP services

## Key Concepts

- **Multi-Agent Systems**: Multiple specialized agents working together to solve complex problems
- **Agent Cards**: Standardized metadata describing agent capabilities, published at `/.well-known/agent-card.json`
- **A2A Protocol**: Open standard enabling agents to discover and communicate with each other
- **Hierarchical Architecture**: Root agents delegating tasks to specialized sub-agents

## Codelab Link

🔗 **[Access the Full Codelab]( https://codelabs.developers.google.com/codelabs/create-multi-agents-adk-a2a#0)**

## Video Walkthrough

📹 **[Watch Video Tutorial](https://youtu.be/ahKLAEmhv-4)**

## Code Location in Repository

```
2_MCP_A2A_Codelab/
└── 1_Multiagent_System_with_ADK/
```

## Technologies Used

- **Google Agent Development Kit (ADK)** - Framework for building AI agents
- **Agent2Agent (A2A) Protocol** - Open standard for agent communication
- **Google Cloud Agent Engine** - Managed deployment service for agents
- **Google Cloud Storage** - Storage for agent artifacts
- **Python** - Primary programming language
- **Poetry** - Dependency management

## Prerequisites

- Google Cloud Platform account with billing enabled
- Basic Python knowledge
- Google Cloud Shell access
- Familiarity with command-line interfaces