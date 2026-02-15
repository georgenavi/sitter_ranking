import csv
from typing import List
from .models import Sitter
from .scoring import calculate_profile_score, calculate_search_score
from .utils import round2


def save_sitters(sitters: List[Sitter], filepath: str) -> None:
    """
    Save sitter rankings to CSV file.

    Results are sorted by search_score (desc), then name (asc).
    """
    rows = []

    for s in sitters:
        profile_score = calculate_profile_score(s.name)
        ratings_score = s.average_rating()
        search_score = calculate_search_score(
            profile_score,
            ratings_score,
            s.stays()
        )

        rows.append({
            "email": s.email,
            "name": s.name,
            "profile_score": f"{round2(profile_score):.2f}",
            "ratings_score": f"{round2(ratings_score):.2f}",
            "search_score": f"{round2(search_score):.2f}",
        })

    # Sort by search_score descending, then name ascending
    rows.sort(key=lambda x: (-float(x["search_score"]), x["name"].lower()))

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["email", "name", "profile_score", "ratings_score", "search_score"]
        )
        writer.writeheader()
        writer.writerows(rows)