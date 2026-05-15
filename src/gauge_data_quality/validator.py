"""
Data quality validation logic.
"""

from typing import Any, Dict, List
from pydantic import BaseModel, Field
from datetime import datetime, timezone

class DataQualityReport(BaseModel):
    is_valid: bool
    missing_fields: List[str] = Field(default_factory=list)
    confidence_score: float = Field(default=1.0)
    warnings: List[str] = Field(default_factory=list)

def validate_result(data: Dict[str, Any], required_fields: List[str] = None) -> DataQualityReport:
    if required_fields is None:
        required_fields = ["result", "evidence", "sources", "confidence"]
    
    missing = [field for field in required_fields if field not in data or data[field] is None]
    warnings = []
    
    confidence = float(data.get("confidence", 1.0))
    if confidence < 0.5:
        warnings.append("Low confidence score detected")
        
    return DataQualityReport(
        is_valid=len(missing) == 0,
        missing_fields=missing,
        confidence_score=confidence,
        warnings=warnings
    )

def check_freshness(timestamp_str: str, max_age_days: int = 30) -> bool:
    try:
        dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        age = (now - dt).days
        return age <= max_age_days
    except Exception:
        return False


