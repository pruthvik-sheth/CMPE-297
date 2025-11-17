from google.adk.agents import LlmAgent
from ..schemas import IntentExtractionResult

INTENT_EXTRACTOR_PROMPT = """
You are an intent extraction specialist. Parse user requests to extract:
- Target industry (e.g., fintech, e-commerce, healthcare)
- Target country/region
- Number of companies to analyze (default: 5)
- Any additional context

Extract structured information from the user's request about lead generation needs.
"""

intent_extractor_agent = LlmAgent(
    name="intent_extractor_agent",
    model="gemini-2.5-flash",
    instruction=INTENT_EXTRACTOR_PROMPT,
    output_schema=IntentExtractionResult,
    description="Extracts key parameters like user intent, country, and industry.",
)