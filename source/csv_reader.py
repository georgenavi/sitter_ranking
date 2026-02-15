"""Load sitter data from CSV."""

import csv
from typing import Dict
from .models import Sitter


def load_sitters(filepath: str) -> Dict[str, Sitter]:
    """
    Load sitters from CSV file.

    Returns:
        Dictionary mapping email to Sitter object
    """
    sitters: Dict[str, Sitter] = {}

    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    email = row["sitter_email"].strip()
                    name = row["sitter"].strip()

                    if email not in sitters:
                        sitters[email] = Sitter(email=email, name=name)

                    rating_str = row["rating"].strip()
                    if rating_str:
                        rating = float(rating_str)
                        if 0 <= rating <= 5:
                            sitters[email].ratings.append(rating)
                except (KeyError, ValueError) as e:
                    print(f"Warning: Skipping invalid row - {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return {}

    return sitters