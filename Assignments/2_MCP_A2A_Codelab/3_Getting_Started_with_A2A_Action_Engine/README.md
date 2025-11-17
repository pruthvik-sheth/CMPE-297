# Codelab 3: A2A Action Engine - Purchasing Concierge

## Overview

This codelab demonstrates the Agent2Agent (A2A) protocol in action by building a purchasing concierge system. You'll create a main concierge agent that communicates with specialized seller agents built using different frameworks (ADK, CrewAI, and LangGraph).

This shows how agents built with different frameworks can seamlessly work together using the A2A protocol, deployed on Google Cloud Run and Vertex AI Agent Engine.

## What You'll Learn

- Implement complete A2A client-server architecture
- Integrate agents built with different frameworks (ADK, CrewAI, LangGraph)
- Deploy agents to Vertex AI Agent Engine and Cloud Run
- Enable agent discovery using Agent Cards
- Build microservices-based multi-agent systems
- Handle task delegation between specialized agents

## The Purchasing Concierge System

```
User → Purchasing Concierge (ADK)
              ↓ A2A Protocol
        ┌─────┴─────┐
        ↓           ↓
  Burger Agent  Pizza Agent
   (CrewAI)     (LangGraph)
```

## How A2A Protocol Works Here

1. **Discovery**: Client fetches Agent Cards from seller agents at `/.well-known/agent.json`
2. **Request**: User places an order through the concierge
3. **Routing**: Concierge determines which seller can handle the order
4. **Delegation**: Concierge sends task to the appropriate seller via A2A
5. **Response**: Seller processes order and returns result

## Codelab Link

🔗 **[Access the Full Codelab](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge#0)**

## Video Walkthrough

📹 **[Watch Video Tutorial](https://youtu.be/B2rD2yquv1Y)**

## Code Location in Repository

```
2_MCP_A2A_Codelab/
└── 3_Getting_Started_with_A2A_Action_Engine/
    └── purchasing_concierge/
```

### Key Files
- **agent.py** - Purchasing concierge (ADK client) implementation
- **purchasing_agent.py** - Order routing and processing logic
- **remote_agent_connection.py** - A2A connection management
- **remote_seller_agents/** - Burger and pizza agent code

### Deployment Structure
```
Vertex AI Agent Engine
└── Purchasing Concierge (Client)

Google Cloud Run
├── Burger Agent (A2A Server)
└── Pizza Agent (A2A Server)
```

## Technologies Used

- **Agent2Agent (A2A) Protocol** - Open standard for agent communication
- **Google Agent Development Kit (ADK)** - Framework for client agent
- **CrewAI** - Framework for Burger agent
- **LangGraph** - Framework for Pizza agent
- **Vertex AI Agent Engine** - Managed deployment for concierge
- **Google Cloud Run** - Serverless hosting for seller agents
- **Python** - Primary programming language

## Key Features

- **Framework Agnostic**: Agents built with different frameworks work together
- **Agent Cards**: Each agent publishes its capabilities and skills
- **Microservices**: Independent services that scale separately
- **Secure Communication**: Enterprise-grade authentication
- **Service Isolation**: Each agent runs in its own environment

## Prerequisites

- Google Cloud Platform account with billing enabled
- Python 3.10+ installed
- Basic understanding of REST APIs and microservices
- Familiarity with cloud deployment

## Real-World Applications

This architecture pattern applies to:
- **Enterprise Systems**: Different department agents collaborating
- **E-commerce**: Inventory, payment, and shipping agents working together
- **Customer Service**: Routing queries to specialized support agents
- **Healthcare**: Coordinating diagnostic and treatment systems