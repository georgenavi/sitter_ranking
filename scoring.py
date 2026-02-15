from config import MAX_ALPHABET_SIZE, MAX_PROFILE_SCORE, FULL_WEIGHT_THRESHOLD


def count_distinct_letters(name: str) -> int:
    """Count unique letters in a name (case-insensitive)."""
    letters = {c.lower() for c in name if "a" <= c.lower() <= "z"}
    return len(letters)


def calculate_profile_score(name: str) -> float:
    """Calculate profile score based on name diversity."""
    return MAX_PROFILE_SCORE * (count_distinct_letters(name) / MAX_ALPHABET_SIZE)


def calculate_ratings_score(ratings: list[float]) -> float:
    """Calculate average rating score."""
    if not ratings:
        return 0.0
    return sum(ratings) / len(ratings)


def calculate_search_score(
        profile_score: float,
        ratings_score: float,
        stays: int
) -> float:
    """
    Calculate weighted search score.

    - 0 stays: 100% profile score
    - 10+ stays: 100% ratings score
    - 1-9 stays: weighted blend
    """
    if stays == 0:
        return profile_score
    if stays >= FULL_WEIGHT_THRESHOLD:
        return ratings_score

    weight_r = stays / FULL_WEIGHT_THRESHOLD
    weight_p = 1 - weight_r
    return profile_score * weight_p + ratings_score * weight_r