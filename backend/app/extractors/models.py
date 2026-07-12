from dataclasses import dataclass, field
from typing import List

@dataclass
class ExtractionResult:
    """Standardized output from any document extractor."""
    text: str = ""
    file_type: str = ""
    character_count: int = 0
    word_count: int = 0
    warnings: List[str] = field(default_factory=list)