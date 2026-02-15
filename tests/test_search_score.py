import pytest
from source.scoring import calculate_search_score


class TestSearchScoreLogic:
    """Validates core business logic for ranking algorithm."""

    def test_zero_stays_uses_profile_only(self):
        """With 0 stays, should return 100% profile score."""
        result = calculate_search_score(
            profile_score=2.0,
            ratings_score=5.0,
            stays=0
        )
        assert result == 2.0, "0 stays should use 100% profile score"

    def test_five_stays_equal_weighting(self):
        """With 5 stays, should be 50/50 weighted average."""
        result = calculate_search_score(
            profile_score=2.0,
            ratings_score=4.0,
            stays=5
        )
        assert result == 3.0, "5 stays should be 50/50 weighted"

    def test_ten_or_more_stays_uses_ratings_only(self):
        """With 10+ stays, should return 100% ratings score."""
        result_10 = calculate_search_score(
            profile_score=2.0,
            ratings_score=4.5,
            stays=10
        )
        result_20 = calculate_search_score(
            profile_score=2.0,
            ratings_score=4.5,
            stays=20
        )
        assert result_10 == 4.5, "10 stays should use 100% ratings score"
        assert result_20 == 4.5, "20 stays should use 100% ratings score"

    def test_three_stays_weighting(self):
        """With 3 stays, should be 70% profile, 30% ratings."""
        result = calculate_search_score(
            profile_score=1.0,
            ratings_score=5.0,
            stays=3
        )
        # 1.0 * 0.7 + 5.0 * 0.3 = 0.7 + 1.5 = 2.2
        assert result == pytest.approx(2.2, abs=0.01)

    def test_nine_stays_weighting(self):
        """With 9 stays, should be 10% profile, 90% ratings."""
        result = calculate_search_score(
            profile_score=1.0,
            ratings_score=5.0,
            stays=9
        )
        # 1.0 * 0.1 + 5.0 * 0.9 = 0.1 + 4.5 = 4.6
        assert result == pytest.approx(4.6, abs=0.01)