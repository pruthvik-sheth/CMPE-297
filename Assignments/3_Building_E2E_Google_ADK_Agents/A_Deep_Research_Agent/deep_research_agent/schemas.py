from pydantic import BaseModel
from typing import List, Optional

class IntentExtractionResult(BaseModel):
    industry: str
    country: str
    num_companies: int = 5
    additional_context: Optional[str] = None

class Company(BaseModel):
    name: str
    description: str
    location: str
    industry: str
    funding_stage: Optional[str] = None
    website: Optional[str] = None

class PatternResult(BaseModel):
    pattern_name: str
    description: str
    evidence: List[str]
    companies_exhibiting: List[str]