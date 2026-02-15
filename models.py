"""Data models."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Sitter:
    """Represents a pet sitter with ratings."""
    email: str
    name: str
    ratings: List[float] = field(default_factory=list)

    def stays(self) -> int:
        """Return number of completed stays."""
        return len(self.ratings)

    def average_rating(self) -> float:
        """Calculate average rating from all reviews."""
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)