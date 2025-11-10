# Google Agent Development Kit (ADK) - E2E Agent Implementation Projects

Complete end-to-end implementation of production-ready AI agents using Google's Agent Development Kit. This repository showcases five distinct agent architectures demonstrating the full spectrum of ADK capabilities from research to production deployment.

## What You'll Learn

Build sophisticated multi-agent systems using Google's Agent Development Kit, master Model Context Protocol (MCP) integration, implement production-quality code review workflows, develop e-commerce solutions with database integration, and deploy scalable AI agents to Google Cloud infrastructure.

## A. Deep Research Agent for Lead Generation
Advanced research agent that analyzes market data, validates information, and generates qualified leads using hierarchical agent orchestration with parallel execution capabilities.

**Video Walkthrough:** [Watch on YouTube](https://youtube.com/temp-lead-generation-walkthrough)

**Key Features:**
- Interactive Lead Generator with primary orchestrator
- LeadResearchOrchestratorAgent for parallel task execution  
- ValidatorAgent and LeadSignalAnalyzerAgent coordination
- State management across multi-turn conversations
- Pattern discovery and validation workflows

**Resources:**
- [Google Cloud Blog - Build a Deep Research Agent](https://cloud.google.com/blog/products/ai-machine-learning/build-a-deep-research-agent-with-google-adk)
- [GitHub Repository](https://github.com/MagnIeeT/leadGenerationAgentADK)

## B. Advanced Tool Agent with Gemini CLI Integration
Production-grade agent that integrates Gemini CLI as a tool within ADK pipelines, deployed on Cloud Run with real-time agent analysis and code generation capabilities.

**Video Walkthrough:** [Watch on YouTube](https://youtube.com/temp-gemini-cli-agent-walkthrough)

**Key Features:**
- Gemini CLI integration within ADK framework
- Cloud Run deployment with SSE transport
- Agent source code analysis and explanation
- Real-time code generation assistance
- MCP server interactions with local development

**Resources:**
- [Medium Article - Combine ADK with Gemini CLI](https://medium.com/@derrickchwong/combine-adk-gemini-cli-and-cloud-run-c5dea5118853)
- [GitHub Repository](https://github.com/derrickchwong/gemini-cli-on-adk)

## C. MCP Tools-Based Bug Assistant Agent
Software bug assistant leveraging Model Context Protocol tools for database queries, GitHub integration, and comprehensive ticket management with Cloud SQL backend.

**Video Walkthrough:** [Watch on YouTube](https://youtube.com/temp-mcp-bug-assistant-walkthrough)

**Key Features:**
- Function Tools for basic operations
- Built-in Tools (Google Search integration)
- Third-Party Tools from LangChain framework
- MCP Tools for Cloud SQL PostgreSQL database
- GitHub MCP server integration for issue tracking

**Resources:**
- [Google Cloud Blog - Tools Make an Agent](https://cloud.google.com/blog/topics/developers-practitioners/tools-make-an-agent-from-zero-to-assistant-with-adk)
- [Google Codelabs Tutorial](https://codelabs.developers.google.com/codelabs/cloud-run/tools-make-an-agent)
- [GitHub Code Sample](https://github.com/google/adk-samples/tree/main/python/agents/software-bug-assistant)

## D. Production Quality Code Review Assistant
Sophisticated multi-agent code review system with deterministic analysis tools, automated testing execution, style compliance validation, and iterative fix pipeline.

**Video Walkthrough:** [Watch on YouTube](https://youtube.com/temp-code-review-assistant-walkthrough)

**Key Features:**
- Multi-agent review pipeline (Analyzer, Style Checker, Test Runner)
- Code synthesis agent with feedback orchestration
- AST parsing with async execution patterns  
- Automated fix pipeline with user interaction
- Production-grade state management and error handling

**Resources:**
- [Google Codelabs - Code Review Assistant](https://codelabs.developers.google.com/adk-code-reviewer-assistant/instructions)
- [GitHub Repository](https://github.com/ayoisio/adk-code-review-assistant)

## E. Production Quality E-Commerce Agent with AlloyDB
Enterprise-grade sports shop AI assistant with natural language product search, store localization, order management, and advanced database integration using MCP Toolbox.

**Video Walkthrough:** [Watch on YouTube](https://youtube.com/temp-ecommerce-agent-walkthrough)

**Key Features:**
- Natural language product catalog search
- Nearby store finder with geolocation
- Order placement and status tracking
- AlloyDB integration with vector search
- OAuth2 authentication and prompt injection protection
- MCP Toolbox for Databases with AI-powered SQL generation

**Resources:**
- [Google Codelabs - Sports Agent](https://codelabs.developers.google.com/codelabs/sports-agent-adk-mcp-alloydb)
- [GitHub Repository](https://github.com/mtoscano84/sports-agent-adk-mcp-alloydb/)

---

## Technical Stack
- **Framework:** Google Agent Development Kit (ADK)
- **Models:** Gemini 2.5 Pro/Flash, Gemini 2.0 Flash
- **Databases:** AlloyDB, Cloud SQL PostgreSQL, Firestore
- **Deployment:** Cloud Run, Vertex AI Agent Engine
- **Tools:** MCP Toolbox, Gemini CLI, Google Cloud APIs
- **Languages:** Python, SQL, YAML

## Architecture Patterns
- Multi-agent orchestration with sequential and parallel workflows
- Model Context Protocol (MCP) server/client implementations
- Production deployment with containerization and CI/CD
- State management and session persistence
- Real-time streaming and bidirectional communication

Each implementation demonstrates production-ready patterns for building, testing, evaluating, and deploying sophisticated AI agent systems at enterprise scale.